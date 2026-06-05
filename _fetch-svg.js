const https = require('https');
const url = 'https://s3.amazonaws.com/pf-form-assets-01/u-251292/assets/2026-04-07/kf43e4s/selectsoccer.svg';
https.get(url, (res) => {
  let data = '';
  res.on('data', (c) => (data += c));
  res.on('end', () => {
    console.log(data.slice(0, 3000));
    const reds = [...data.matchAll(/#[0-9a-fA-F]{3,8}|rgb\([^)]+\)/g)];
    console.log('\ncolors:', [...new Set(reds.map((m) => m[0]))]);
  });
}).on('error', console.error);
