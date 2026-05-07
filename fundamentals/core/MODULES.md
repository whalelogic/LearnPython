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

## Advanced Import Mechanics

## Import resolution order (high-level)

1. Check `sys.modules` cache.
2. If not loaded, consult import finders/loaders.
3. Load module object and execute top-level code.
4. Cache loaded module in `sys.modules`.

This explains why expensive top-level statements impact startup time.

## Relative import examples

```python
# package layout:
# app/
#   __init__.py
#   db.py
#   services/
#     __init__.py
#     users.py

# file: app/services/users.py
from ..db import get_session
```

Run package modules using `python -m app.services.users` when needed.

## Public API Design Pattern

```python
# app/services/__init__.py
from .users import create_user, get_user

__all__ = ["create_user", "get_user"]
```

This creates a stable import surface for callers while keeping internal modules flexible.

## Module-level constants and configuration

```python
# settings.py
DEFAULT_TIMEOUT_SECONDS = 30
SUPPORTED_FORMATS = {"json", "csv"}
```

Keep configuration names uppercase and immutable where possible.

## Lightweight plugin loading

```python
import importlib

PLUGIN_NAMES = ["plugins.auth", "plugins.audit"]
loaded = [importlib.import_module(name) for name in PLUGIN_NAMES]
```

Dynamic import is useful for extensibility, but validate plugin names from trusted sources.

## Refactoring Monolith Files into Modules

| Step | Action |
|---|---|
| 1 | Identify cohesive responsibilities in one large file |
| 2 | Move each responsibility to dedicated module |
| 3 | Re-export stable API in package `__init__.py` |
| 4 | Update imports incrementally |
| 5 | Keep tests green across each move |

## Packaging-ready layout recommendation

```text
project/
  pyproject.toml
  src/
    mypkg/
      __init__.py
      ...
  tests/
```

This reduces accidental local-import shadowing and improves reliability in CI.

## Real Project Module Architecture Patterns

## Layered module architecture

```text
app/
  domain/          # business rules
  services/        # orchestration
  adapters/        # external integrations (db, api)
  api/             # HTTP/CLI interfaces
```

Keep dependencies flowing inward (api/adapters -> services -> domain), not randomly across layers.

## Import hygiene checklist

- Avoid wildcard imports in application code.
- Keep import order consistent.
- Prefer explicit symbols for local readability.
- Keep import side effects minimal.
- Resolve circular references by extracting shared contracts.

## Preventing name collisions

```python
import datetime as dt
import zoneinfo

# clear names, no ambiguity with local variable "datetime"
now = dt.datetime.now(zoneinfo.ZoneInfo("UTC"))
```

## Optional dependency imports

```python
try:
    import ujson as json_impl
except ImportError:
    import json as json_impl
```

This pattern allows graceful fallback across environments.

## Module-level singleton pattern (use carefully)

```python
# cache.py
_cache = {}

def get_cache():
    return _cache
```

Document shared mutable singletons clearly to avoid hidden coupling.

## Lazy imports for heavy dependencies

```python
def parse_large_dataframe(path):
    import pandas as pd  # local import defers heavy startup cost
    return pd.read_csv(path)
```

Use sparingly when startup latency matters.

## Type-checking-only imports

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import User
```

Helps avoid runtime import cycles while preserving static typing support.

## Package boundary contracts

Define what external modules may rely on:

- stable public functions/classes in package root,
- internal details under private modules (`_internal.py` naming style),
- changelog when public API changes.

## Mini refactor plan for tangled imports

1. Map current dependency graph.
2. Detect cycles.
3. Move shared abstractions to neutral module.
4. Replace back-edge imports with injected dependencies.
5. Re-run tests after each small move.

## Module Review Checklist

| Question | Why it matters |
|---|---|
| Is this module cohesive? | Easier maintenance and reuse |
| Are imports explicit and acyclic? | Fewer runtime surprises |
| Is top-level execution lightweight? | Faster startup and cleaner tests |
| Is public API clear? | Stable contracts for callers |
| Are side effects isolated to entry points? | Predictable behavior |

Strong module boundaries are the difference between script-scale code and long-lived maintainable software.

## Import Debugging Toolkit

```python
import importlib.util

spec = importlib.util.find_spec("json")
print(spec)
```

Useful for diagnosing why a module cannot be imported in a given environment.

## Common Refactoring Smells in Module Design

| Smell | Symptom | Fix |
|---|---|---|
| God module | Huge file with mixed responsibilities | Split by domain concerns |
| Cyclic imports | Import errors at startup | Extract shared interfaces/module |
| Hidden side effects | Import triggers network/file I/O | Move side effects behind functions |
| Leaky internals | Callers import private helpers directly | Re-export stable API only |

## Versioning Public Modules

If others consume your package:

- add semantic versioning discipline,
- document deprecations,
- maintain backward-compatible import paths where possible,
- provide migration notes for renamed modules.

## Final Modules Mastery Checklist

- Can you explain absolute vs relative imports from memory?
- Can you design package boundaries for a medium-size app?
- Can you detect and break import cycles safely?
- Can you expose a clean package-level API with `__init__.py`?
- Can you keep import side effects minimal?

Module fluency enables scalable code organization, dependable tooling, and maintainable team workflows.


## Related Context in This Repository

- Follow this module reference with [../../standard_library/README.md](../../standard_library/README.md) to see which batteries-included modules are worth learning first.
- The `web/` examples in this repository are useful for seeing why imports, package layout, and `python -m` matter in real projects.
- A practical exercise is to split one script into `helpers.py` and `main.py`, import the helper functions, and then run the package both directly and with `python -m` to observe the difference.
