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
path.write_text("read
practice
review
", encoding="utf-8")
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
