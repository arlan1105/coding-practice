import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import quote

LANGUAGES = {
    "python": "Python",
    "java": "Java",
    "cpp": "C++",
    "c": "C",
    "javascript": "JavaScript",
}

PLATFORMS = {
    "codeforces": "Codeforces",
    "codewars": "Codewars",
    "freecodecamp": "freeCodeCamp",
    "codechum": "CodeChum",
}

CODE_EXTENSIONS = {".py", ".java", ".cpp", ".c", ".js", ".ts", ".cs", ".go", ".rs"}
RECENT_LIMIT = 10
MONTHS_SHOWN = 6


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
    if file_path.stem.lower() == "solution" and file_path.parent.name not in PLATFORMS:
        return file_path.parent.name
    return file_path.stem


def link(path: Path) -> str:
    return quote(path.as_posix())


def bar(n: int, total: int, width: int = 20) -> str:
    filled = round(width * n / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def pct(n: int, total: int) -> str:
    return f"{(100 * n / total):.0f}%" if total else "0%"


def added_dates() -> dict[str, str]:
    """Map file path -> date it was added (newest add wins)."""
    try:
        out = subprocess.run(
            ["git", "-c", "core.quotepath=false", "log", "--no-renames",
             "--diff-filter=A", "--name-only", "--format=@@%as"],
            capture_output=True, text=True, check=True,
        ).stdout
    except Exception:
        return {}
    dates, current = {}, None
    for line in out.splitlines():
        if line.startswith("@@"):
            current = line[2:]
        elif line and line not in dates:
            dates[line] = current
    return dates


def badge(label: str, value: str, color: str) -> str:
    return (f"![{label}](https://img.shields.io/badge/"
            f"{quote(label)}-{quote(str(value))}-{color}?style=flat-square)")


def generate_readme():
    total = 0
    lang_totals = {name: 0 for name in LANGUAGES.values()}
    platform_data = {}
    all_files = []  # (path, platform, language)

    for plat_dir, plat_name in PLATFORMS.items():
        plat_total, plat_langs = 0, {}
        for lang_dir, lang_name in LANGUAGES.items():
            files = count_solutions(Path(lang_dir) / plat_dir)
            if files:
                plat_total += len(files)
                total += len(files)
                lang_totals[lang_name] += len(files)
                plat_langs[lang_name] = files
                all_files += [(f, plat_name, lang_name) for f in files]
        if plat_total:
            platform_data[plat_name] = {"total": plat_total, "languages": plat_langs}

    dates = added_dates()
    dated = [(dates[f.as_posix()], f, p, l) for f, p, l in all_files if f.as_posix() in dates]
    dated.sort(key=lambda x: x[0], reverse=True)
    last_date = dated[0][0] if dated else "n/a"
    active_langs = sum(1 for c in lang_totals.values() if c)

    lines = [
        "# Coding Practice",
        "",
        "Daily coding challenges and practice problems across multiple platforms.",
        "",
        " ".join([
            badge("Solutions", total, "2ea44f"),
            badge("Platforms", len(platform_data), "0969da"),
            badge("Languages", active_langs, "8250df"),
            badge("Last solved", last_date, "d29922"),
        ]),
        "",
        "## 📊 Overall Stats",
        "",
        "| Platform | Solutions | Share | |",
        "|---|---:|---:|---|",
    ]
    for name, data in sorted(platform_data.items(), key=lambda x: -x[1]["total"]):
        n = data["total"]
        lines.append(f"| {name} | {n} | {pct(n, total)} | `{bar(n, total)}` |")
    lines.append(f"| **Total** | **{total}** | | |")

    lines += ["", "| Language | Solutions | Share |", "|---|---:|---:|"]
    for name, n in sorted(lang_totals.items(), key=lambda x: -x[1]):
        if n:
            lines.append(f"| {name} | {n} | {pct(n, total)} |")

    if dated:
        lines += ["", f"## 🕒 Recent Activity (last {min(RECENT_LIMIT, len(dated))})", ""]
        for date, f, plat, lang in dated[:RECENT_LIMIT]:
            lines.append(f"- `{date}` [{format_label(f)}]({link(f)}) · {plat} · {lang}")

        months = Counter(d[:7] for d, *_ in dated)
        recent_months = sorted(months)[-MONTHS_SHOWN:]
        peak = max(months[m] for m in recent_months)
        lines += ["", "## 📈 Solutions per Month", "", "```"]
        for m in recent_months:
            lines.append(f"{m}  {bar(months[m], peak, 24)}  {months[m]}")
        lines.append("```")

    lines += ["", "## 📁 Platform Breakdown", ""]
    for plat_name, data in platform_data.items():
        lines.append(f"### {plat_name} ({data['total']})")
        lines.append("")
        for lang_name, files in data["languages"].items():
            lines.append("<details>")
            lines.append(f"<summary><b>{lang_name} ({len(files)} solutions)</b></summary>")
            lines.append("")
            for f in files:
                lines.append(f"- [{format_label(f)}]({link(f)})")
            lines += ["", "</details>", ""]

    Path("README.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    generate_readme()
