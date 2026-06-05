/* Sport icons – line art with brand blue & gold accents */
const SPORT_ICONS = {
  soccer: `<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M25 65 L45 35 L55 40 L70 25" stroke="#1a1a1a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    <ellipse cx="72" cy="28" rx="12" ry="12" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M30 68 L20 78 L35 82 L42 72 Z" stroke="#1a1a1a" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="M32 70 L28 76" stroke="#1E3AFF" stroke-width="3" stroke-linecap="round"/>
    <circle cx="72" cy="28" r="3" fill="#FDC656"/>
  </svg>`,

  basketball: `<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="55" y="15" width="35" height="28" rx="2" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M55 43 L90 43 L82 75 L48 75 Z" stroke="#1a1a1a" stroke-width="2.5" stroke-linejoin="round"/>
    <circle cx="28" cy="55" r="18" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M20 48 Q28 55 20 62" stroke="#1a1a1a" stroke-width="1.5"/>
    <path d="M35 42 L42 55 L35 68" stroke="#1a1a1a" stroke-width="1.5"/>
    <path d="M58 18 L65 25" stroke="#1E3AFF" stroke-width="4" stroke-linecap="round"/>
    <path d="M15 50 L5 45 M15 60 L5 65" stroke="#1a1a1a" stroke-width="2" stroke-linecap="round"/>
  </svg>`,

  hockey: `<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M20 75 L35 25 L42 28 L27 78 Z" stroke="#1a1a1a" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="M35 25 L75 20" stroke="#1a1a1a" stroke-width="2.5" stroke-linecap="round"/>
    <ellipse cx="78" cy="22" rx="8" ry="5" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M22 72 L18 82 L32 85 L36 75 Z" stroke="#1a1a1a" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="M24 78 L20 84" stroke="#1E3AFF" stroke-width="4" stroke-linecap="round"/>
    <path d="M40 35 L50 32 L48 42 L38 45 Z" fill="#1E3AFF" opacity="0.9"/>
  </svg>`,

  baseball: `<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M25 55 Q20 30 45 25 Q70 20 75 45 Q80 70 55 75 Q30 80 25 55 Z" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M35 35 L40 50 L35 65 M50 30 L55 50 L50 70" stroke="#1a1a1a" stroke-width="1.5"/>
    <circle cx="68" cy="62" r="10" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M63 58 Q68 62 63 66" stroke="#1a1a1a" stroke-width="1.5"/>
    <ellipse cx="42" cy="42" rx="8" ry="6" fill="#FDC656"/>
  </svg>`,

  esports: `<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M15 45 Q15 30 30 28 L70 28 Q85 30 85 45 L82 55 Q80 65 70 65 L55 65 L52 72 L48 72 L45 65 L30 65 Q20 65 18 55 Z" stroke="#1a1a1a" stroke-width="2.5" stroke-linejoin="round"/>
    <circle cx="35" cy="48" r="6" stroke="#1a1a1a" stroke-width="2"/>
    <circle cx="65" cy="48" r="6" stroke="#1a1a1a" stroke-width="2"/>
    <circle cx="35" cy="48" r="3" fill="#1E3AFF"/>
    <circle cx="65" cy="48" r="3" fill="#1E3AFF"/>
    <path d="M42 58 L58 58" stroke="#1a1a1a" stroke-width="2" stroke-linecap="round"/>
  </svg>`,

  lacrosse: `<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <ellipse cx="35" cy="35" rx="18" ry="22" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M20 35 L50 35 M25 25 L45 25 M25 45 L45 45" stroke="#1a1a1a" stroke-width="1.5"/>
    <line x1="50" y1="35" x2="85" y2="70" stroke="#1a1a1a" stroke-width="2.5" stroke-linecap="round"/>
    <circle cx="72" cy="58" r="8" fill="#FDC656"/>
    <path d="M30 55 L40 75" stroke="#1a1a1a" stroke-width="2.5" stroke-linecap="round"/>
  </svg>`,

  rugby: `<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M30 75 L30 25 L70 25" stroke="#1a1a1a" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M30 25 L70 25 L70 45" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M45 25 L45 75" stroke="#1a1a1a" stroke-width="2.5"/>
    <ellipse cx="55" cy="68" rx="14" ry="10" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M48 68 Q55 62 62 68" stroke="#1a1a1a" stroke-width="1.5"/>
    <ellipse cx="55" cy="72" rx="4" ry="3" fill="#1E3AFF"/>
  </svg>`,

  football: `<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M35 70 Q30 50 50 35 Q70 25 75 45 Q78 60 65 68 Q50 78 35 70 Z" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M42 42 L50 55 L58 42" stroke="#1a1a1a" stroke-width="2" stroke-linejoin="round"/>
    <path d="M45 38 L55 38" stroke="#1a1a1a" stroke-width="2" stroke-linecap="round"/>
    <path d="M20 55 L10 48 L15 65 L25 62 Z" stroke="#1a1a1a" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="M48 62 Q55 68 52 74" stroke="#1E3AFF" stroke-width="4" stroke-linecap="round"/>
  </svg>`,

  volleyball: `<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="50" r="22" stroke="#1a1a1a" stroke-width="2.5"/>
    <path d="M50 28 L50 72 M28 50 L72 50 M35 35 L65 65 M65 35 L35 65" stroke="#1a1a1a" stroke-width="1.5"/>
    <path d="M30 75 L50 45 L70 75" stroke="#1a1a1a" stroke-width="2.5" stroke-linecap="round"/>
    <circle cx="50" cy="42" r="4" fill="#FDC656"/>
  </svg>`
};

const SPORTS = [
  { id: 'soccer', label: 'Soccer' },
  { id: 'basketball', label: 'Basketball' },
  { id: 'hockey', label: 'Hockey' },
  { id: 'baseball', label: 'Baseball' },
  { id: 'esports', label: 'Esports' },
  { id: 'lacrosse', label: 'Lacrosse' },
  { id: 'rugby', label: 'Rugby' },
  { id: 'football', label: 'Football' },
  { id: 'other', label: 'Other', isOther: true }
];
