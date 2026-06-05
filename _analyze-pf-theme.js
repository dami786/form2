const fs = require('fs');
const s = fs.readFileSync('_pf_page.html', 'utf8');
const i = s.indexOf('"themeForm":true');
console.log(s.slice(i, i + 1200));
