# Python Standard Library

The standard library gives you useful modules and functions without installing third-party packages.

## In This Folder

- [Built_In_Functions.md](Built_In_Functions.md) — a practical overview of the built-ins beginners use most often

## Related Topic Folders

- [../fundamentals/core/MODULES.md](../fundamentals/core/MODULES.md) for import and package basics
- [../system/README.md](../system/README.md) for file handling and OS-focused modules
- [../regex/README.md](../regex/README.md) for text parsing with `re`

## Why the Standard Library Matters

Before installing a new dependency, it is worth checking whether Python already includes what you need. Files, JSON, dates, CSV, iterators, statistics, environment variables, and path handling are all covered surprisingly well.

## Quick Example

```python
from pathlib import Path
import json

config_path = Path("config.json")
settings = json.loads(config_path.read_text(encoding="utf-8"))
print(settings)
```
