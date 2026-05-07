# Python OS Module Guide

The `os` module provides operating-system level interfaces for paths, environment variables, processes, and filesystem operations.

## Key Areas

### Paths
```python
import os

cwd = os.getcwd()
joined = os.path.join(cwd, "data", "file.txt")
exists = os.path.exists(joined)
```

### Environment Variables
```python
import os

api_key = os.getenv("API_KEY")
os.environ["APP_MODE"] = "dev"
```

### Directory Operations
```python
import os

os.makedirs("logs/archive", exist_ok=True)
files = os.listdir(".")
```

### Process Information
```python
import os

pid = os.getpid()
uid = os.getuid() if hasattr(os, "getuid") else None
```

## Prefer pathlib for New Code

For most path operations, `pathlib` is more readable:

```python
from pathlib import Path

path = Path("data") / "file.txt"
if path.exists():
    print(path.read_text(encoding="utf-8"))
```

## Best Practices

1. Use `os.getenv()` with defaults for optional configuration.
2. Avoid hardcoded separators; use `os.path` or `pathlib`.
3. Use `exist_ok=True` to make directory creation idempotent.
4. Never trust environment variables as validated input.

## Related Docs

- [os docs](https://docs.python.org/3/library/os.html)
- [os.path docs](https://docs.python.org/3/library/os.path.html)

