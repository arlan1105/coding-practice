import os
from collections import defaultdict

# Folders to ignore when scanning
IGNORE_DIRS = {'.git', '.github'}
# File extensions to count as solutions
CODE_EXTS = {'.py': 'Python', '.java': 'Java', '.cpp': 'C++', '.c': 'C', '.js': 'JavaScript', '.html': 'HTML/CSS', '.css': 'HTML/CSS'}

# Platform keywords to match folder names (case-insensitive)
PLATFORMS = {
    'codeforces': 'Codeforces',
    'codewars': 'Codewars',
    'fcc': 'freeCodeCamp',
    'freecodecamp': 'freeCodeCamp',
    'codechum': 'CodeChum',
}

stats = defaultdict(lambda: defaultdict(list))
lang_counts = defaultdict(int)
total_solutions = 0

for root, dirs, files in os.walk('.'):
    # Skip hidden/system folders
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
    
    for file in sorted(files):
        ext = os.path.splitext(file)[1].lower()
        if ext not in CODE_EXTS:
            continue
            
        filepath = os.path.join(root, file).lstrip('./').replace('\\', '/')
        parts = filepath.lower().split('/')
        
        # Detect platform from folder path
        platform_name = 'Other'
        for part in parts:
            for key, label in PLATFORMS.items():
                if key in part:
                    platform_name = label
                    break
            if platform_name != 'Other':
                break
                
        lang = CODE_EXTS[ext]
        stats[platform_name][lang].append((file, filepath))
        lang_counts[lang] += 1
        total_solutions += 1

# Build Markdown content
lines = [
    "# 💻 Coding Practice",
    "",
    "Automated archive of my programming solutions across **Codeforces**, **Codewars**, **freeCodeCamp**, and **CodeChum**.",
    "",
    "## 📊 Overall Stats",
    "",
    f"- **Total Solutions:** `{total_solutions}`",
]

for lang, count in sorted(lang_counts.items(), key=lambda x: -x[1]):
    lines.append(f"- **{lang}:** `{count}`")

lines.extend(["", "## 🗂️ Platform Breakdown", ""])

for platform in ['Codeforces', 'Codewars', 'freeCodeCamp', 'CodeChum', 'Other']:
    if platform not in stats:
        continue
    plat_total = sum(len(v) for v in stats[platform].values())
    lines.append(f"### {platform} ({plat_total})")
    lines.append("")
    for lang, items in sorted(stats[platform].items()):
        lines.append(f"<details><summary><b>{lang}</b> ({len(items)} solutions)</summary>\n")
        for filename, path in items:
            # URL-encode spaces for clickable GitHub links
            safe_path = path.replace(' ', '%20')
            lines.append(f"- [{filename}]({safe_path})")
        lines.append("\n</details>\n")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines).strip() + "\n")
