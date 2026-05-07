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

## Lifecycle Internals

The `with` statement is conceptually expanded by Python into this shape:

```python
manager = EXPR
enter = manager.__enter__
exit = manager.__exit__
value = enter()
try:
    TARGET = value
    BODY
except Exception as exc:
    if not exit(type(exc), exc, exc.__traceback__):
        raise
else:
    exit(None, None, None)
```

Understanding this model helps when debugging advanced context manager behavior.

## Context Managers for Concurrency

### Thread synchronization

```python
from threading import Lock

lock = Lock()
shared = []

with lock:
    shared.append("safe write")
```

### Async semaphore management

```python
import asyncio

sem = asyncio.Semaphore(5)

async def worker(item):
    async with sem:
        await asyncio.sleep(0.1)
        return item * 2
```

## Context Managers for Temporary State

### Temporary decimal precision

```python
from decimal import Decimal, localcontext

with localcontext() as ctx:
    ctx.prec = 4
    print(Decimal("1") / Decimal("7"))
```

### Temporary warning policy

```python
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=DeprecationWarning)
    # run legacy call
```

## Nested Failure Handling Pattern

```python
class SafeResource:
    def __enter__(self):
        print("open")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("error path cleanup", exc_type.__name__)
        else:
            print("success path cleanup")
        return False

with SafeResource():
    pass
```

You can route metrics, logs, and rollback logic through this boundary.

## Robust Class-based Template

```python
class ManagedConnection:
    def __init__(self, factory):
        self.factory = factory
        self.conn = None

    def __enter__(self):
        self.conn = self.factory()
        # validate post-condition
        if self.conn is None:
            raise RuntimeError("Connection factory returned None")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.conn is not None:
                self.conn.close()
        finally:
            self.conn = None
        return False
```

Template principles:
- establish resource in `__enter__`
- guarantee cleanup in `__exit__`
- keep manager reusable or explicitly one-shot

## Reusable Utility Managers

### Timing block execution

```python
from contextlib import contextmanager
import time

@contextmanager
def timed(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.6f}s")

with timed("compute"):
    _ = sum(range(1_000_000))
```

### Capturing exceptions into result objects

```python
from contextlib import contextmanager

@contextmanager
def capture_error(store):
    try:
        yield
    except Exception as exc:
        store["error"] = str(exc)
        store["type"] = type(exc).__name__
```

## Composition with `ExitStack`

`ExitStack` shines when resources are optional or conditional:

```python
from contextlib import ExitStack

paths = ["a.txt", "b.txt"]
writers_enabled = True

with ExitStack() as stack:
    files = [stack.enter_context(open(p, "w", encoding="utf-8")) for p in paths]
    log = stack.enter_context(open("run.log", "a", encoding="utf-8")) if writers_enabled else None

    for f in files:
        f.write("ok\n")
    if log:
        log.write("all files written\n")
```

## Async Context Pattern for Network Clients

```python
class APIClient:
    async def __aenter__(self):
        # open pools/sessions
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # close pools/sessions
        return False

    async def get(self, path):
        return {"path": path}

async def fetch_profile():
    async with APIClient() as client:
        return await client.get("/profile")
```

## Decision Guide

| Need | Best approach |
|---|---|
| Simple setup/cleanup | `@contextmanager` |
| Stateful reusable manager | Class with `__enter__/__exit__` |
| Dynamic number of resources | `ExitStack` |
| Async resource lifecycle | `async with` + `__aenter__/__aexit__` |

## Testing Context Managers Directly

```python
def test_timer_context_runs_without_suppression():
    class NoSuppress:
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            return False

    try:
        with NoSuppress():
            raise ValueError("boom")
    except ValueError:
        assert True
```

## Production Checklist

- Does `__exit__` always release resources?
- Are exceptions intentionally propagated or intentionally suppressed?
- Is cleanup idempotent?
- Are async resources closed in `__aexit__`?
- Is manager scope as small as possible?

Context managers make failure-safe programming habitual, which is one of the biggest quality multipliers in Python codebases.

## Context Managers in System Workflows

## File transformation pipeline

```python
from contextlib import ExitStack

sources = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:
    readers = [stack.enter_context(open(p, "r", encoding="utf-8")) for p in sources]
    writer = stack.enter_context(open("merged.txt", "w", encoding="utf-8"))

    for r in readers:
        writer.write(r.read())
        writer.write("\n")
```

## Temporary monkey patch pattern

```python
from contextlib import contextmanager

@contextmanager
def patch_attr(obj, name, value):
    original = getattr(obj, name)
    setattr(obj, name, value)
    try:
        yield
    finally:
        setattr(obj, name, original)
```

Useful in tests where behavior must be overridden briefly.

## Resource dependency graph pattern

Sometimes one resource depends on another (e.g., transaction depends on open connection). Context managers enforce ordering:

1. enter connection
2. enter transaction
3. perform operations
4. exit transaction
5. exit connection

This explicit ordering prevents partial cleanup bugs.

## Context Manager Error Semantics Table

| Phase | Error behavior |
|---|---|
| `__enter__` raises | Body never executes; already-entered outer managers unwind |
| Body raises | `__exit__` receives exception details |
| `__exit__` raises | New exception may replace original unless chained properly |

## Practical Logging Wrapper

```python
from contextlib import contextmanager
import logging
import time

logger = logging.getLogger(__name__)

@contextmanager
def logged_block(name):
    start = time.perf_counter()
    logger.info("start %s", name)
    try:
        yield
    except Exception:
        logger.exception("failed %s", name)
        raise
    finally:
        logger.info("end %s in %.4fs", name, time.perf_counter() - start)
```

## Comparison: Decorators vs Context Managers

| Tool | Best for |
|---|---|
| Decorator | Cross-cutting behavior around function call boundaries |
| Context manager | Temporary behavior/resource state inside code block |

You can combine both for clean architecture.

## Advanced Async Manager Composition

```python
from contextlib import AsyncExitStack

async def handle_request(resources):
    async with AsyncExitStack() as stack:
        conns = [await stack.enter_async_context(r) for r in resources]
        # use all async resources safely
        return len(conns)
```

## Field Guide: Replace Try/Finally with Context Manager

| If you currently do... | Prefer |
|---|---|
| Open/close file manually | `with open(...)` |
| Acquire/release lock manually | `with lock:` |
| Set/reset temp env var | custom `@contextmanager` |
| Begin/commit/rollback transaction | transaction context manager |

Context managers reduce incidental complexity and make correctness the default.
