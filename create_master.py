

from pathlib import Path
from datetime import datetime

# ── CONFIG ─────────────────────────────────────────────────────────────────────
TARGET_FOLDERS = ['app', 'core', 'pipelines', 'prompts', 'utils', 'vectorstore']

SKIP_DIRS = {"__pycache__", ".git", ".venv", "venv", "env",
             ".idea", ".vscode", ".pytest_cache", "archive", "output"}

CODE_OUTPUT      = "master_code_file.txt"
STRUCTURE_OUTPUT = "project_structure.txt"
# ───────────────────────────────────────────────────────────────────────────────


def read_file(path: Path) -> str:
    for enc in ("utf-8", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except Exception:
            continue
    return f"# ERROR: could not read {path}\n"


def is_important(path: Path) -> bool:
    """Skip empty files, test files, and migration scripts."""
    if path.stat().st_size == 0:
        return False
    if path.name.startswith("test_") or path.name.endswith("_test.py"):
        return False
    if "migration" in path.parts:
        return False
    return True


def collect_py_files(folder: Path, skip_script: Path) -> list[Path]:
    files = []
    for f in sorted(folder.rglob("*.py")):
        if any(part in SKIP_DIRS for part in f.parts):
            continue
        if f.resolve() == skip_script:
            continue
        if is_important(f):
            files.append(f)
    return files


# ── PROJECT STRUCTURE ──────────────────────────────────────────────────────────

def tree_lines(dir_path: Path, prefix: str = "") -> list[str]:
    lines = []
    try:
        items = sorted(
            [p for p in dir_path.iterdir() if p.name not in SKIP_DIRS],
            key=lambda p: (p.is_file(), p.name.lower())
        )
    except PermissionError:
        return [f"{prefix}└── [PERMISSION DENIED]"]

    for i, item in enumerate(items):
        connector = "└── " if i == len(items) - 1 else "├── "
        lines.append(f"{prefix}{connector}{item.name}{'/' if item.is_dir() else ''}")
        if item.is_dir():
            ext = "    " if i == len(items) - 1 else "│   "
            lines.extend(tree_lines(item, prefix + ext))
    return lines


def build_structure(root: Path):
    out_path = root / STRUCTURE_OUTPUT
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"PROJECT STRUCTURE: {root.name}\n")
        f.write(f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"{root.name}/\n")
        f.write("\n".join(tree_lines(root)))
        f.write("\n")
    print(f"[structure] -> {out_path}")


# ── MASTER CODE FILE ───────────────────────────────────────────────────────────

def write_section(f, file_path: Path, root: Path):
    rel = file_path.relative_to(root)
    f.write("\n" + "=" * 80 + "\n")
    f.write(f"FILE: {rel}\n")
    f.write("=" * 80 + "\n\n")
    f.write(read_file(file_path))
    f.write("\n")


def build_code(root: Path):
    this_script = Path(__file__).resolve()
    out_path = root / CODE_OUTPUT

    # Root-level .py files
    root_files = [
        f for f in sorted(root.glob("*.py"))
        if f.resolve() != this_script and is_important(f)
    ]

    # Files inside each target folder
    folder_files = {
        name: collect_py_files(root / name, this_script)
        for name in TARGET_FOLDERS
        if (root / name).is_dir()
    }
    folder_files = {k: v for k, v in folder_files.items() if v}  # drop empty

    total = len(root_files) + sum(len(v) for v in folder_files.values())

    with open(out_path, "w", encoding="utf-8") as f:
        # Header
        f.write(f"PROJECT : {root.name}\n")
        f.write(f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total files : {total}\n")
        f.write("=" * 80 + "\n")

        # Root files
        f.write(f"\n### ROOT FILES ({len(root_files)}) ###\n")
        for fp in root_files:
            write_section(f, fp, root)

        # Folder files
        for folder_name, files in folder_files.items():
            f.write(f"\n### {folder_name.upper()}/ ({len(files)} files) ###\n")
            for fp in files:
                write_section(f, fp, root)

        # Summary
        f.write("\n" + "=" * 80 + "\n")
        f.write("SUMMARY\n")
        f.write(f"  root/          : {len(root_files)} files\n")
        for folder_name, files in folder_files.items():
            f.write(f"  {folder_name + '/':<15}: {len(files)} files\n")
        f.write(f"  TOTAL          : {total} files\n")

    print(f"[code]      -> {out_path}  ({total} files)")


# ── MAIN ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    build_structure(root)
    build_code(root)