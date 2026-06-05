const fs = require('fs');
const s = fs.readFileSync('_pf_page.html', 'utf8');

const idx = s.indexOf('Select your sport');
console.log('sport section:', s.slice(idx, idx + 2500));

const colors = [...s.matchAll(/#[0-9a-fA-F]{3,8}/g)].map((m) => m[0]);
const counts = {};
colors.forEach((c) => {
  const k = c.toLowerCase();
  counts[k] = (counts[k] || 0) + 1;
});
console.log('\nhex colors:', Object.entries(counts).sort((a, b) => b[1] - a[1]).slice(0, 30));

['styling', 'customCss', 'custom_css', 'theme', 'primary', 'accent', 'navigation', 'button'].forEach((term) => {
  let i = 0;
  let n = 0;
  while ((i = s.indexOf(term, i)) !== -1 && n < 3) {
    console.log('\n---', term, '---');
    console.log(s.slice(i, i + 180));
    i++;
    n++;
  }
});
