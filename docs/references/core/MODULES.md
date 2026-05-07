# Python Modules and Packages Reference

Modules and packages are Python's organization system for real projects. They let you split code into clear units, reuse functionality, and control import boundaries.

## Mental Model: File System ↔ Import Namespace

- A **module** is usually one `.py` file.
- A **package** is a directory that groups modules.
- Import paths map to directories/files (`package.subpackage.module`).
- Running a file directly is different from importing it.

## Why Modules Matter

| Problem | Without modules | With modules |
|---|---|---|
| Reuse | Copy-paste code | `import` once, reuse everywhere |
| Readability | One giant file | Domain-focused files |
| Testing | Hard to isolate behavior | Test per module |
| Collaboration | Merge conflicts everywhere | Team can work by module boundary |

## Module Basics

### Example module

```python
# file: math_utils.py

def add(a, b):
    return a + b

PI_NOTE = "Approximate circle constant"
```

### Import styles

```python
import math_utils
print(math_utils.add(2, 3))
```

```python
from math_utils import add
print(add(5, 7))
```

```python
import math_utils as mu
print(mu.add(1, 9))
```

## Import Style Comparison

| Style | Example | Pros | Cons |
|---|---|---|---|
| Module import | `import os` | Clear origin of names | Slightly longer calls |
| Selective import | `from os import path` | Concise for frequent symbols | Can hide symbol origin |
| Alias import | `import numpy as np` | Short and conventional | Requires team conventions |
| Wildcard import | `from m import *` | Fast in REPL | Pollutes namespace; avoid in production |

## `__name__` and Executable Modules

```python
# file: app.py

def main():
    print("Running app")

if __name__ == "__main__":
    main()
```

### Mental model

| Situation | `__name__` value |
|---|---|
| Imported as module | Module path (`app`) |
| Run directly (`python app.py`) | `"__main__"` |

Use this pattern for CLI entry points and local smoke tests.

## Package Structure

```text
project/
  src/
    shop/
      __init__.py
      pricing.py
      inventory.py
      services/
        __init__.py
        checkout.py
```

Typical imports:

```python
from shop.pricing import calculate_total
from shop.services.checkout import CheckoutService
```

## Absolute vs Relative Imports

| Type | Example | Good for |
|---|---|---|
| Absolute | `from shop.services.checkout import ...` | Large codebases, clarity |
| Relative | `from .pricing import calculate_total` | Internal package references |

Use absolute imports by default for readability.

## `__init__.py` and Package API Design

`__init__.py` can define package-level exports.

```python
# shop/__init__.py
from .pricing import calculate_total

__all__ = ["calculate_total"]
```

Now callers can do:

```python
from shop import calculate_total
```

## Search Path and `sys.path`

Python resolves imports using `sys.path` (script directory, environment paths, installed packages).

```python
import sys
for p in sys.path:
    print(p)
```

Avoid ad-hoc `sys.path` mutations in application code; prefer proper package layout and environment setup.

## Import Time Execution

Top-level module code executes on first import.

```python
# bad_module.py
print("This runs at import time")
```

Guideline: keep top-level code minimal (constants, definitions). Put side effects in functions.

## Standard Library, Third-party, Local Imports

Conventional import grouping:

1. Standard library
2. Third-party packages
3. Local application imports

```python
import json
from pathlib import Path

import requests

from shop.pricing import calculate_total
```

## Dynamic Imports

```python
module_name = "json"
mod = __import__(module_name)
print(mod.dumps({"ok": True}))
```

Prefer `importlib` in modern code:

```python
import importlib
mod = importlib.import_module("json")
```

## Caching and Reloading

Imports are cached in `sys.modules`.

```python
import importlib
import mymodule

importlib.reload(mymodule)
```

Useful for REPL workflows; avoid relying on reload behavior in production logic.

## Circular Imports

Circular dependencies happen when modules depend on each other during import.

### Symptoms
- `ImportError`
- partially initialized module attributes

### Fix strategies
- Move shared logic to a third module.
- Delay imports inside functions where necessary.
- Reduce coupling between modules.

## Module Design Checklist

| Rule | Why |
|---|---|
| One clear responsibility per module | Easier maintenance |
| Avoid heavy side effects at import time | Faster startup, fewer surprises |
| Prefer explicit imports | Better readability and tooling support |
| Keep public API deliberate (`__all__`, re-exports) | Stable external contracts |
| Separate domain logic from I/O edges | Easier testing |

## Practical Example: Mini Package

```python
# file: weather/formatters.py

def format_temp(celsius):
    return f"{celsius:.1f}°C"
```

```python
# file: weather/client.py
from .formatters import format_temp

def describe(temp):
    return f"Current temperature: {format_temp(temp)}"
```

```python
# file: weather/__init__.py
from .client import describe

__all__ = ["describe"]
```

Usage:

```python
from weather import describe
print(describe(23.456))
```

## Common Import Errors and Fixes

| Error | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError` | Package not installed / path incorrect | Install package, verify interpreter environment |
| `ImportError: cannot import name ...` | Symbol missing or circular import | Check symbol name, break dependency cycle |
| Relative import failure when running file directly | Package context missing | Run with `python -m package.module` |

## Recommended Learning Progression

1. Build and import simple modules.
2. Group modules into packages.
3. Practice absolute imports and public API exposure.
4. Understand runtime behavior (`__name__`, import caching).
5. Handle real-world pitfalls: circular imports, path issues, packaging boundaries.

Master modules and packages early—this skill scales from scripts to production systems.
