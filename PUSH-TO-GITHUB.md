# GitHub push – sirf `form` folder se

## Problem (10,000 changes)
Agar GitHub Desktop / Cursor **user folder** (`C:\Users\KhurshidComputers`) se push karo ge to poore PC ki files dikhen gi.

**Sahi folder:**
`C:\Users\KhurshidComputers\OneDrive\Desktop\form`

Is repo mein sirf **~71 project files** hain.

## Push steps

1. GitHub par **naya empty repo** banao (README mat add karo).
2. PowerShell:

```powershell
cd "C:\Users\KhurshidComputers\OneDrive\Desktop\form"
git status
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

3. `git status` clean hona chahiye; GitHub par ~71 files dikhen.

## GitHub Desktop
- **Add existing repository** → select `Desktop\form` folder only
- **Publish** / Push
- Repository path mein `form` hona chahiye, `KhurshidComputers` nahi
