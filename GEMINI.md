# Project: WhaleLogic's `LearnPython` Reference Library

## General Instructions

- When you generate new reference material and accompanying code, follow the style and structure below.
- Ensure all .md reference files are present in every directory, and begin with a large table of common functions (built-in or otherwise) related to the referenced topic.
- Prefer functional programming paradigms where appropriate.
- Each .md file should be self-contained and include:
  - A clear introduction to the topic
  - A table of common functions or methods with descriptions
  - Code examples demonstrating usage
  - Notes on best practices and when to use or avoid the topic

> Below is an example structure for a reference file on the `os` module, which can be adapted for other topics in the library.
> Another perfect format example is the /regex/REGEX_REFERENCE.md file. Try to follow that style as well, especially for the tables and technical content.

## Example Reference File Structure

## Deep Reference

### `os` Module Function Reference

#### Paths and directories

| Function | Description |
|---|---|
| `os.getcwd()` | Current working directory as a string |
| `os.chdir(path)` | Change working directory |
| `os.listdir(path='.')` | List names in a directory |
| `os.scandir(path='.')` | Iterator of `DirEntry` objects with stat info |
| `os.makedirs(path, exist_ok=False)` | Create directory tree |
| `os.removedirs(path)` | Remove empty directory tree |
| `os.rename(src, dst)` | Rename / move a file or directory |
| `os.replace(src, dst)` | Rename, atomically replacing destination |
| `os.remove(path)` | Delete a file |
| `os.rmdir(path)` | Remove an empty directory |
| `os.stat(path)` | File metadata: size, mtime, permissions |
| `os.walk(top)` | Recursive directory tree generator |

#### Path operations (`os.path`)

| Function | Description |
|---|---|
| `os.path.join(a, b, ...)` | Join path components (OS-appropriate separator) |
| `os.path.split(path)` | `(head, tail)` tuple |
| `os.path.splitext(path)` | `(root, ext)` tuple |
| `os.path.basename(path)` | Filename component |
| `os.path.dirname(path)` | Directory component |
| `os.path.exists(path)` | Whether path exists |
| `os.path.isfile(path)` | Whether path is a regular file |
| `os.path.isdir(path)` | Whether path is a directory |
| `os.path.abspath(path)` | Absolute path |
| `os.path.expanduser(path)` | Expand `~` to home directory |
| `os.path.getsize(path)` | File size in bytes |

### `os` vs `pathlib` — When to Use Each

| Task | Prefer `os` | Prefer `pathlib` |
|---|---|---|
| Environment variables | `os.getenv` | — |
| Process info | `os.getpid`, `os.cpu_count` | — |
| Interop with libraries that take strings | `str(path)` | — |
| Path building | — | `Path("a") / "b"` |
| Reading / writing files | — | `.read_text()`, `.write_text()` |
| Recursive glob | — | `.rglob("*.py")` |
| Existence / type checks | — | `.exists()`, `.is_file()` |
| Directory creation | — | `.mkdir(parents=True, exist_ok=True)` |

Use `pathlib.Path` for new path code; use `os` when you need environment variables, process details, or must produce plain strings for external APIs.

### `os.walk` — Recursive Tree Traversal

```python
import os

for root, dirs, files in os.walk("src"):
    # root  — current directory as a string
    # dirs  — list of subdirectory names (can modify to prune)
    # files — list of file names in root
    for name in files:
        if name.endswith(".py"):
            full = os.path.join(root, name)
            print(full)

# Skip hidden directories
for root, dirs, files in os.walk("project"):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        print(os.path.join(root, f))
```

### `os.scandir` — Efficient Directory Listing

`scandir` avoids extra `stat` calls compared to `listdir + stat`:

```python
import os

with os.scandir("data") as it:
    for entry in it:
        if entry.is_file() and entry.name.endswith(".csv"):
            info = entry.stat()
            print(f"{entry.name:30s}  {info.st_size:>10,} bytes")
```

### Environment Variables Patterns

```python
import os

# Safe read with typed defaults
debug  = os.getenv("DEBUG", "false").lower() == "true"
port   = int(os.getenv("PORT", "8080"))
db_url = os.environ["DATABASE_URL"]   # intentionally fail if missing

# Guard against missing required vars at startup
required = ["DATABASE_URL", "SECRET_KEY", "API_TOKEN"]
missing  = [k for k in required if not os.getenv(k)]
if missing:
    raise EnvironmentError(f"Missing required env vars: {missing}")
```

### `shutil` — High-Level File Operations

`shutil` builds on `os` for common file management tasks:

```python
import shutil
from pathlib import Path

# Copy file preserving metadata
shutil.copy2("src.txt", "dst.txt")

# Copy entire directory tree
shutil.copytree("src_dir", "dst_dir")

# Move / rename
shutil.move("old/path.txt", "new/path.txt")

# Delete entire directory tree
shutil.rmtree("temp_dir")

# Disk usage
total, used, free = shutil.disk_usage("/")
print(f"Free: {free // (1024**3)} GiB")

# Create a zip archive
shutil.make_archive("backup", "zip", "project")
```

### `tempfile` — Safe Temporary Files

```python
import tempfile
import os

# Temporary file — deleted when closed
with tempfile.NamedTemporaryFile(mode="w", suffix=".csv",
                                  delete=True, encoding="utf-8") as tf:
    tf.write("id,name\n1,Ava\n")
    print(tf.name)  # path available while open

# Temporary directory — cleaned up on exit
with tempfile.TemporaryDirectory() as tmpdir:
    path = os.path.join(tmpdir, "output.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("temp content")
```

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Read env vars with `os.getenv`, list a directory with `os.listdir`, build paths with `os.path.join` |
| **Developing** | Walk directory trees, validate required env vars at startup, prefer `pathlib` for new path code |
| **Proficient** | Use `os.scandir` efficiently, combine `os` and `shutil`, write cross-platform path code |
| **Advanced** | Manage process metadata, use `tempfile` safely, use `os.replace` for atomic file updates |

### Suggested Practice Projects

1. **File inventory** — Walk a directory tree with `os.walk`, collect file sizes, and print a summary sorted by size.
2. **Env-var validator** — Write a startup check that reads all required env vars and raises a descriptive error listing every missing one.
3. **Directory mirror** — Copy a directory structure to a backup location, skipping files that already exist and are unchanged (compare `os.stat().st_mtime`).
4. **Temp workspace** — Use `tempfile.TemporaryDirectory` as a scratch area; process files inside it, then move the results out before cleanup.
5. **Cross-platform path tool** — Accept a path string, resolve `~`, ensure it is absolute, create its parent directories, and report whether it is a file or directory.

### Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| String concatenation for paths | `dir + "/" + file` breaks on Windows | Use `os.path.join` or `Path / "subdir"` |
| `os.environ[key]` on missing key | Raises `KeyError` immediately | Use `os.getenv(key, default)` or `.get` |
| `os.listdir` returns filenames only | You must `os.path.join` to get full paths | Use `os.scandir` or `Path.iterdir()` |
| `os.makedirs` fails if dir exists | Raises `FileExistsError` by default | Pass `exist_ok=True` |
| `os.remove` on a directory | Raises `IsADirectoryError` | Use `os.rmdir` (empty) or `shutil.rmtree` |
| Platform `os.sep` assumptions | Hardcoding `/` breaks on Windows | Always use `os.path.join` or `pathlib` |


