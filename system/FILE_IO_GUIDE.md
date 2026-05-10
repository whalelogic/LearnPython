# Python File I/O Guide

File I/O is how programs persist data between runs. Python keeps it simple, but a few habits make a big difference.

## Core Concepts

- Use `with` so files close automatically
- Pick a mode that matches your intent: `r`, `w`, `a`, `x`, plus `b` for binary
- Use `encoding="utf-8"` for text unless you have a strong reason not to

## Common Patterns

### Read a File
```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

### Stream Line by Line
```python
with open("server.log", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

### Write Structured JSON
```python
import json

report = {"name": "Alice", "score": 95}
with open("report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=2)
```

## A Practical Example

```python
from pathlib import Path

path = Path("todos.txt")
path.write_text("read\npractice\nreview\n", encoding="utf-8")
items = path.read_text(encoding="utf-8").splitlines()
print(items)
```

## Common Mistakes

- Opening a file in `w` mode when you meant to append
- Reading huge files fully into memory unnecessarily
- Forgetting to handle `FileNotFoundError` or invalid file contents

## Related Reading

- [OS_GUIDE.md](OS_GUIDE.md)
- [../fundamentals/core/CONTEXTS.md](../fundamentals/core/CONTEXTS.md)

---

## Deep Reference

### `open()` Complete Reference

```python
open(
    file,                     # path string or Path object
    mode='r',                 # see mode table below
    buffering=-1,             # -1 = system default
    encoding=None,            # e.g. 'utf-8' for text mode
    errors=None,              # 'strict', 'replace', 'ignore'
    newline=None,             # None = universal newlines
    closefd=True,
    opener=None,
)
```

#### Mode strings

| Mode | Meaning | File must exist? |
|---|---|---|
| `r` | Read text (default) | Yes |
| `w` | Write text, truncate | No |
| `a` | Append text | No |
| `x` | Create new file exclusively | No (fails if exists) |
| `rb` | Read binary | Yes |
| `wb` | Write binary, truncate | No |
| `r+` | Read and write text | Yes |
| `w+` | Write and read, truncate | No |
| `a+` | Append and read | No |

Always specify `encoding="utf-8"` for text mode unless you have a concrete reason not to.

### File Object Method Reference

| Method | Description |
|---|---|
| `.read(size=-1)` | Read entire file (or `size` bytes/chars) |
| `.readline()` | Read one line including the trailing `\n` |
| `.readlines()` | Read all lines into a list |
| `.write(s)` | Write string and return characters written |
| `.writelines(lines)` | Write a sequence of strings (no separator added) |
| `.seek(pos)` | Move file pointer to byte position |
| `.tell()` | Return current byte position |
| `.flush()` | Flush write buffer to OS |
| `.close()` | Close the file (done automatically in `with`) |
| `.truncate(size=None)` | Shrink file to `size` bytes |
| Iteration | `for line in f:` — memory-efficient line iteration |

### Reading Patterns

```python
# Full content (small files only)
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Line-by-line — constant memory regardless of file size
with open("server.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            print(line.rstrip())

# Read all lines into a list
with open("config.ini", "r", encoding="utf-8") as f:
    lines = f.readlines()    # includes '\n'
    lines = [l.rstrip() for l in lines]
```

### Writing Patterns

```python
# Plain text
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world\n")

# Append without overwriting
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Session started\n")

# Write multiple lines at once
rows = ["Alice,92", "Bob,78", "Cara,88"]
with open("scores.csv", "w", encoding="utf-8") as f:
    f.writelines(row + "\n" for row in rows)
```

### JSON and CSV Patterns

```python
import json
import csv

# --- JSON ---
data = {"name": "Ava", "score": 91}

with open("record.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("record.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

# --- CSV (DictWriter / DictReader) ---
rows = [{"name": "Ava", "score": 91}, {"name": "Ben", "score": 78}]

with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)

with open("scores.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    records = list(reader)  # [{'name': 'Ava', 'score': '91'}, ...]
```

### `pathlib` — The Modern Path API

Prefer `pathlib.Path` for all new path code. It composes naturally and works cross-platform.

```python
from pathlib import Path

# Building paths safely
base = Path("data")
file = base / "input" / "scores.csv"

# Common operations
print(file.name)        # 'scores.csv'
print(file.stem)        # 'scores'
print(file.suffix)      # '.csv'
print(file.parent)      # data/input
print(file.exists())

# Read / write without open()
Path("notes.txt").write_text("hello\n", encoding="utf-8")
content = Path("notes.txt").read_text(encoding="utf-8")

# List files
for p in Path("data").glob("**/*.csv"):
    print(p)

# Create directories
Path("output/reports").mkdir(parents=True, exist_ok=True)
```

#### `pathlib.Path` Method Reference

| Method / Property | Purpose |
|---|---|
| `Path(str)` | Create a path object |
| `p / "subdir"` | Join path segments |
| `p.name` | Filename including extension |
| `p.stem` | Filename without extension |
| `p.suffix` | Extension including dot |
| `p.parent` | Parent directory |
| `p.parts` | Tuple of all path components |
| `p.exists()` | Whether path exists |
| `p.is_file()` / `p.is_dir()` | Type check |
| `p.stat()` | Size, mtime, permissions |
| `p.read_text(encoding=)` | Read entire file as string |
| `p.write_text(s, encoding=)` | Write string to file |
| `p.read_bytes()` | Read binary content |
| `p.write_bytes(b)` | Write bytes to file |
| `p.mkdir(parents=, exist_ok=)` | Create directory |
| `p.unlink(missing_ok=)` | Delete file |
| `p.rename(target)` | Rename / move |
| `p.glob(pattern)` | Iterator of matching paths |
| `p.rglob(pattern)` | Recursive glob |
| `p.resolve()` | Absolute path |

### Error Handling Patterns

```python
from pathlib import Path

def safe_read(path: str) -> str | None:
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except PermissionError:
        print(f"No permission to read: {path}")
        return None
    except UnicodeDecodeError:
        print(f"Not valid UTF-8: {path}")
        return None
```

### Binary File Patterns

```python
# Read binary exactly
with open("image.png", "rb") as f:
    header = f.read(8)       # first 8 bytes
    rest   = f.read()        # everything else

# Write binary
with open("copy.png", "wb") as f:
    f.write(header + rest)

# Stream large binary file in chunks
CHUNK = 65_536  # 64 KiB
with open("large.bin", "rb") as src, open("out.bin", "wb") as dst:
    while chunk := src.read(CHUNK):
        dst.write(chunk)
```

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Open, read, and write text files using `with`; specify `encoding="utf-8"` |
| **Developing** | Stream files line-by-line, use `json` and `csv` modules, use `pathlib.Path` for paths |
| **Proficient** | Handle all common I/O exceptions, read/write binary, list files with `glob` |
| **Advanced** | Stream large files in chunks, use `seek`/`tell` for random access, compose `pathlib` and `shutil` for file-system operations |

### Suggested Practice Projects

1. **Log analyzer** — Stream a large log file line by line, count occurrences of each log level, and print a summary.
2. **CSV merger** — Read multiple CSV files from a directory, combine all rows, deduplicate by ID, and write a single output file.
3. **Config reader** — Parse a `key=value` config file into a dict, with defaults for missing keys.
4. **File backup tool** — Copy files matching a glob pattern to a timestamped backup directory using `pathlib` and `shutil.copy2`.
5. **JSON log rotator** — Append structured JSON records to a log file, and when it exceeds 1 MB, rotate it to `log.1.json`.

### Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Missing `encoding` | Default encoding is platform-dependent (`cp1252` on Windows) | Always pass `encoding="utf-8"` |
| `w` mode deletes content | Opening an existing file in `w` truncates it immediately | Use `a` to append or `r+` to update |
| Forgetting `newline=""` with `csv` | Extra blank lines appear in CSV output on Windows | Pass `newline=""` to `open()` when using `csv` |
| Reading huge files with `.read()` | Loads entire file into memory | Iterate line-by-line or read in chunks |
| File not closed on exception | Without `with`, an exception leaks the file handle | Always use `with open(...) as f:` |
| String vs bytes mode | Writing a `str` to a binary file raises `TypeError` | Match your mode (`r`/`w` for text, `rb`/`wb` for bytes) |

