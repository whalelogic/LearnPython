# Context Managers in Python

Context managers provide deterministic setup/teardown around a block of code. They are used with `with` (and `async with`) to manage resources safely and cleanly.

## Mental Model

A context manager is a **scope guard**:

1. Enter scope (`__enter__` / `__aenter__`)
2. Run block
3. Exit scope (`__exit__` / `__aexit__`) even if errors occur

This makes context managers ideal for files, locks, network connections, transactions, and temporary state changes.

## Why `with` Matters

| Without `with` | With `with` |
|---|---|
| Manual cleanup in `finally` | Automatic cleanup |
| Easy to forget resource release | Safe by default |
| More boilerplate | Readable and compact |

## Basic `with` Example

```python
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# file closed automatically
```

Equivalent manual pattern:

```python
file = open("example.txt", "r", encoding="utf-8")
try:
    content = file.read()
finally:
    file.close()
```

## Implementing Class-based Context Managers

```python
class Timer:
    def __enter__(self):
        import time
        self._time = time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = self._time.perf_counter()
        self.elapsed = end - self.start
        print(f"Elapsed: {self.elapsed:.6f}s")
        return False  # do not suppress exceptions

with Timer() as t:
    total = sum(range(100_000))
```

## `__exit__` Return Value and Exception Suppression

| Return from `__exit__` | Behavior |
|---|---|
| `False` / `None` | Exception propagates |
| `True` | Exception suppressed |

Use suppression sparingly and only when intentionally converting failure into alternate control flow.

## Function-based Context Managers (`contextlib.contextmanager`)

```python
from contextlib import contextmanager

@contextmanager
def temporary_env(key, value):
    import os
    old = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if old is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = old

with temporary_env("APP_MODE", "debug"):
    pass
```

This style is concise and ideal for simple setup/cleanup logic.

## Multiple Context Managers

```python
with open("input.txt", "r", encoding="utf-8") as src, \
     open("output.txt", "w", encoding="utf-8") as dst:
    dst.write(src.read())
```

All entered managers are unwound in reverse order on exit.

## Dynamic Resource Management with `ExitStack`

```python
from contextlib import ExitStack

filenames = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:
    files = [stack.enter_context(open(name, "r", encoding="utf-8")) for name in filenames]
    for f in files:
        print(f.readline().strip())
```

`ExitStack` is useful when you don't know resource count at coding time.

## Async Context Managers

```python
class AsyncConnection:
    async def __aenter__(self):
        print("opening async connection")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("closing async connection")
        return False

async def use_conn():
    async with AsyncConnection() as conn:
        pass
```

For function-based async managers:

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_timer(label):
    import asyncio
    start = asyncio.get_running_loop().time()
    try:
        yield
    finally:
        end = asyncio.get_running_loop().time()
        print(f"{label}: {end - start:.3f}s")
```

## Standard Library Context Managers You Should Know

| Tool | Module | Use case |
|---|---|---|
| `open(...)` | built-in | File handling |
| `threading.Lock()` | `threading` | Protect critical sections |
| `contextlib.suppress(...)` | `contextlib` | Ignore specific expected exceptions |
| `contextlib.redirect_stdout(...)` | `contextlib` | Capture or redirect printed output |
| `tempfile.TemporaryDirectory()` | `tempfile` | Auto-clean temporary directories |
| `decimal.localcontext()` | `decimal` | Temporary decimal precision/rounding |

## `contextlib` Utilities in Practice

### Suppress expected error

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    import os
    os.remove("optional-cache.tmp")
```

### Redirect stdout

```python
from contextlib import redirect_stdout
from io import StringIO

buffer = StringIO()
with redirect_stdout(buffer):
    print("captured text")

print(buffer.getvalue())
```

## Transaction-like Pattern

```python
from contextlib import contextmanager

@contextmanager
def transaction(conn):
    conn.begin()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
```

This pattern centralizes success/rollback behavior and reduces duplicated error handling.

## Testing with Context Managers

Use context managers in tests for deterministic setup and teardown:

```python
from tempfile import TemporaryDirectory
from pathlib import Path

with TemporaryDirectory() as tmp:
    path = Path(tmp) / "data.txt"
    path.write_text("hello", encoding="utf-8")
    assert path.read_text(encoding="utf-8") == "hello"
```

## Common Mistakes

| Mistake | Problem | Better practice |
|---|---|---|
| Doing heavy logic in `__enter__` with no failure plan | Partial setup risk | Keep setup atomic or roll back safely |
| Returning `True` from `__exit__` indiscriminately | Hides real bugs | Suppress only specific expected exceptions |
| Forgetting to yield in `@contextmanager` function | Runtime error | Ensure exactly one `yield` |
| Using context manager where plain function is enough | Overengineering | Use `with` only for scoped resources/state |

## Building Intuition: When to Reach for a Context Manager

Use a context manager when you see this sentence:

> "I must always undo/release/reset this thing, even if an exception occurs."

Typical examples:
- file handles
- locks
- DB transactions
- temporary env vars
- temporary cwd changes

## Advanced Example: Temporary Working Directory

```python
from contextlib import contextmanager
from pathlib import Path
import os

@contextmanager
def working_directory(path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield Path(path)
    finally:
        os.chdir(previous)
```

## Practice Goals

- Implement one class-based and one function-based context manager.
- Explain exactly when `__exit__` runs.
- Use `ExitStack` for dynamic resources.
- Use `async with` in coroutine workflows.

Context managers are one of Python's highest-leverage features for writing safe, clean, and maintainable code.
