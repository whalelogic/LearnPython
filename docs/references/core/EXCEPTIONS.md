# Python Exceptions Reference

Exceptions are Python's structured mechanism for handling errors and exceptional situations. They let you separate **normal flow** from **failure flow**, making code safer and easier to debug.

## Mental Model: Exception Pipeline

1. Code runs in `try` block.
2. If an exception occurs, Python searches matching `except` blocks.
3. If no handler matches, exception propagates upward.
4. `finally` always runs for cleanup.

## Core Syntax

```python
try:
    risky_operation()
except ValueError as exc:
    print(f"Recoverable value error: {exc}")
else:
    print("Executed only if no exception occurred")
finally:
    print("Cleanup runs no matter what")
```

## Common Built-in Exceptions

| Exception | Typical cause |
|---|---|
| `TypeError` | Operation applied to wrong type |
| `ValueError` | Right type, invalid value |
| `IndexError` | Sequence index out of range |
| `KeyError` | Missing dictionary key |
| `ZeroDivisionError` | Division/modulo by zero |
| `FileNotFoundError` | Missing file path |
| `PermissionError` | Access denied |
| `ImportError` / `ModuleNotFoundError` | Import resolution issues |
| `AttributeError` | Missing attribute on object |
| `RuntimeError` | Generic runtime failure |

## Exception Hierarchy Snapshot

| Level | Examples |
|---|---|
| `BaseException` | `KeyboardInterrupt`, `SystemExit`, `GeneratorExit` |
| `Exception` | Most application errors |
| Subclasses of `Exception` | `ValueError`, `TypeError`, `OSError`, etc. |

In application code, catch subclasses of `Exception`, not `BaseException`, unless you have a very specific reason.

## Catching Specific Exceptions

```python
def parse_port(text):
    try:
        port = int(text)
        if not (1 <= port <= 65535):
            raise ValueError("Port must be between 1 and 65535")
        return port
    except ValueError as exc:
        raise ValueError(f"Invalid port input: {text!r}") from exc
```

Specific handlers prevent accidental masking of unrelated bugs.

## Multiple `except` Patterns

```python
try:
    value = int("abc")
except ValueError:
    print("Not a valid integer")
except TypeError:
    print("Wrong type provided")
```

Combined form:

```python
except (ValueError, TypeError) as exc:
    print(f"Input error: {exc}")
```

## `else` and `finally` Best Practices

- Use `else` for post-success logic (keeps `try` block small).
- Use `finally` for deterministic cleanup (files, locks, temporary states).

```python
file = None
try:
    file = open("data.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Missing file")
else:
    print(file.readline())
finally:
    if file:
        file.close()
```

(Prefer `with open(...)` where possible.)

## Raising Exceptions

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise RuntimeError("Insufficient funds")
    return balance - amount
```

Raise errors at boundaries where invalid state enters your system.

## Exception Chaining (`raise ... from ...`)

```python
def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError as exc:
        raise RuntimeError(f"Cannot load config from {path}") from exc
```

Chaining preserves root cause while adding domain context.

## Custom Exceptions

```python
class AppError(Exception):
    """Base class for application-specific errors."""

class ValidationError(AppError):
    pass

class AuthenticationError(AppError):
    pass
```

Custom hierarchy helps callers handle failures at the right abstraction level.

## Designing Error Boundaries

| Layer | Error strategy |
|---|---|
| Low-level utility | Raise specific built-in or local custom error |
| Domain/service layer | Translate technical errors into domain errors |
| API/CLI edge | Convert errors into user-friendly messages/status codes |

## Anti-patterns to Avoid

| Anti-pattern | Why harmful | Better approach |
|---|---|---|
| `except:` everywhere | Catches interrupts/system exits too | Catch explicit exceptions |
| Empty `except` body (`pass`) | Silently hides failures | Log, recover, or re-raise |
| Catching broad `Exception` too early | Masks bugs and debugging signals | Catch where recovery is meaningful |
| Control flow by exceptions in normal path | Harder to read/maintain | Prefer explicit checks when cheap |

## Logging and Re-raising

```python
import logging
logger = logging.getLogger(__name__)

try:
    process_order(order)
except ValidationError:
    raise
except Exception as exc:
    logger.exception("Unexpected order processing failure")
    raise RuntimeError("Order processing failed") from exc
```

Use `logger.exception` inside exception handlers to keep stack traces.

## Resource Safety with Context Managers

```python
from threading import Lock

lock = Lock()

with lock:
    update_shared_state()
```

`with` is often cleaner and safer than manual `try/finally` for resources.

## Exceptions in Loops and Batch Processing

```python
def parse_rows(rows):
    results = []
    errors = []
    for i, row in enumerate(rows, start=1):
        try:
            results.append(int(row))
        except ValueError as exc:
            errors.append((i, row, str(exc)))
    return results, errors
```

Process continues while preserving error diagnostics.

## Async Exception Handling

```python
import asyncio

async def might_fail(flag):
    if flag:
        raise ValueError("bad flag")
    return "ok"

async def main():
    try:
        result = await might_fail(True)
        print(result)
    except ValueError as exc:
        print(f"Handled async exception: {exc}")

asyncio.run(main())
```

Async code uses same principles, with `await` points where exceptions may surface.

## Practical Validation Pattern

```python
def validate_user_input(data):
    required = ["username", "email"]
    for key in required:
        if key not in data:
            raise ValidationError(f"Missing required field: {key}")

    email = data["email"]
    if "@" not in email:
        raise ValidationError("Invalid email format")
```

## Decision Table: What to Catch?

| Situation | Catch? | Rationale |
|---|---|---|
| You can recover and continue safely | Yes | Explicit handling is useful |
| You can add meaningful context for upstream | Yes | Re-raise with context |
| You cannot recover, and context is already clear | Usually no | Let it propagate |
| Programming bug (`AttributeError` from typo) | No (during development) | Fix root cause |

## Practice Goals

- Write `try/except/else/finally` blocks with minimal `try` scope.
- Build a custom exception hierarchy for a mini application.
- Use `raise ... from ...` to preserve root causes.
- Avoid broad catches unless at top-level boundaries.

Good exception handling turns failures into actionable signals rather than hidden bugs.
