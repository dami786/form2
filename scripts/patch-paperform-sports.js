/**
 * Download Paperform sport SVGs, replace red accents with brand colors,
 * save to assets/paperform-sports/ for re-upload in Paperform or custom CSS.
 */
const https = require('https');
const fs = require('fs');
const path = require('path');

const BASE =
  'https://s3.amazonaws.com/pf-form-assets-01/u-251292/assets/2026-04-07/kf43e4s/';
const SPORTS = [
  'selectsoccer',
  'selectbasketball',
  'selecthockey',
  'selectbaseball',
  'selectesports',
  'selectlacrosse',
  'selectrugby',
  'selectfootball',
  'selectvolleyball',
];

const REPLACEMENTS = [
  [/#ef4142/gi, '#FDC656'],
  [/#ff3b3b/gi, '#1E3A5F'],
  [/#e62e2e/gi, '#1E3A5F'],
  [/#ff2121/gi, '#1E3A5F'],
  [/#990000/gi, '#1528cc'],
];

const outDir = path.join(__dirname, '..', 'assets', 'paperform-sports');
fs.mkdirSync(outDir, { recursive: true });

function get(url) {
  return new Promise((resolve, reject) => {
    https
      .get(url, (res) => {
        if (res.statusCode === 301 || res.statusCode === 302) {
          return get(res.headers.location).then(resolve, reject);
        }
        let data = '';
        res.on('data', (c) => (data += c));
        res.on('end', () => {
          if (res.statusCode !== 200) reject(new Error(`${url} -> ${res.statusCode}`));
          else resolve(data);
        });
      })
      .on('error', reject);
  });
}

(async () => {
  const found = [];
  for (const name of SPORTS) {
    const url = BASE + name + '.svg';
    try {
      let svg = await get(url);
      for (const [re, rep] of REPLACEMENTS) svg = svg.replace(re, rep);
      const file = path.join(outDir, name + '.svg');
      fs.writeFileSync(file, svg);
      found.push(name);
      console.log('OK', name);
    } catch (e) {
      console.log('SKIP', name, e.message);
    }
  }
  console.log('\nPatched', found.length, 'SVGs ->', outDir);
})();
