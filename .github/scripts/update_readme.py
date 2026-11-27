from pathlib import Path

# Supported languages (folder name -> display name)
LANGUAGES = {
    "python": "Python",
    "java": "Java",
    "cpp": "C++",
    "c": "C",
    "javascript": "JavaScript",
}

# Supported platforms (folder name -> display name)
PLATFORMS = {
    "codeforces": "Codeforces",
    "codewars": "Codewars",
    "freecodecamp": "freeCodeCamp",
    "codechum": "CodeChum",
}

# Only count actual solution code files (ignores README.md, etc.)
CODE_EXTENSIONS = {".py", ".java", ".cpp", ".c", ".js", ".ts", ".cs", ".go", ".rs"}


def count_solutions(base_path: Path) -> list[Path]:
    if not base_path.exists():
        return []
    return sorted(
        f for f in base_path.rglob("*")
        if f.is_file() and (
            f.suffix.lower() in CODE_EXTENSIONS
            or (f.name == "solution.txt" and "codeforces" in base_path.parts)
        )
    )


def format_label(file_path: Path) -> str:
    # If CFPusher named the file "solution.py" / "solution.txt", use its parent folder name (e.g., "A - Way Too Long Words")
    if file_path.stem.lower() == "solution" and file_path.parent.name not in PLATFORMS:
        return file_path.parent.name
    return file_path.stem


def generate_readme():
    total_solutions = 0
    lang_totals = {lang_name: 0 for lang_name in LANGUAGES.values()}
    platform_data = {}

    for plat_dir, plat_name in PLATFORMS.items():
        plat_total = 0
        plat_langs = {}

        for lang_dir, lang_name in LANGUAGES.items():
            target = Path(lang_dir) / plat_dir
            files = count_solutions(target)
            if files:
                count = len(files)
                plat_total += count
                total_solutions += count
                lang_totals[lang_name] += count
                plat_langs[lang_name] = files

        if plat_total > 0:
            platform_data[plat_name] = {
                "total": plat_total,
                "languages": plat_langs,
            }

    lines = [
        "# Coding Practice",
        "",
        "Daily coding challenges and practice problems across multiple platforms.",
        "",
        "## 📊 Overall Stats",
        "",
        f"- **Total Solutions:** `{total_solutions}`",
    ]

    for lang_name, count in lang_totals.items():
        if count > 0:
            lines.append(f"- **{lang_name}:** `{count}`")

    lines.extend([
        "",
        "## 📁 Platform Breakdown",
        "",
    ])

    for plat_name, data in platform_data.items():
        lines.append(f"### {plat_name} ({data['total']})")
        lines.append("")
        for lang_name, files in data["languages"].items():
            lines.append("<details>")
            lines.append(f"<summary><b>{lang_name} ({len(files)} solutions)</b></summary>")
            lines.append("")
            for f in files:
                rel_path = f.as_posix().replace(" ", "%20")
                label = format_label(f)
                lines.append(f"- [{label}]({rel_path})")
            lines.append("")
            lines.append("</details>")
            lines.append("")

    Path("README.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    generate_readme()
