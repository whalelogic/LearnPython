# Python File I/O Guide

## Core Concepts

- Use `open()` with context managers (`with`) to ensure files are closed.
- Pick the correct mode:
  - `r`: read
  - `w`: write (overwrite)
  - `a`: append
  - `x`: create only if missing
  - Add `b` for binary and `+` for read/write.

## Common Patterns

### Read Entire File
```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### Read Line by Line
```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### Write Text
```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, File I/O!\n")
```

### Append Text
```python
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Another line\n")
```

### JSON Files
```python
import json

with open("data.json", "w", encoding="utf-8") as f:
    json.dump({"name": "Alice", "score": 95}, f, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

## Best Practices

1. Prefer `pathlib.Path` for cleaner path handling.
2. Always specify `encoding="utf-8"` for text files.
3. Handle exceptions (`FileNotFoundError`, `PermissionError`).
4. Avoid loading huge files fully into memory when streaming works.

## Related Docs

- [Python open() docs](https://docs.python.org/3/library/functions.html#open)
- [pathlib docs](https://docs.python.org/3/library/pathlib.html)

