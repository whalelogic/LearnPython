# Python OS Module Guide

The `os` module exposes operating-system level tasks such as environment variables, directories, process information, and path helpers.

## Common Uses

### Paths and Directories
```python
import os

cwd = os.getcwd()
os.makedirs("logs/archive", exist_ok=True)
print(os.listdir(cwd))
```

### Environment Variables
```python
import os

mode = os.getenv("APP_MODE", "dev")
os.environ["FEATURE_FLAG"] = "on"
print(mode)
```

### Process Information
```python
import os

print(os.getpid())
```

## Prefer `pathlib` for New Path Code

```python
from pathlib import Path

path = Path("data") / "input.txt"
if path.exists():
    print(path.read_text(encoding="utf-8"))
```

`os` is still important because many libraries and deployment environments use it directly, especially for environment variables and process-level details.

## Related Reading

- [FILE_IO_GUIDE.md](FILE_IO_GUIDE.md)
- [../standard_library/README.md](../standard_library/README.md)
