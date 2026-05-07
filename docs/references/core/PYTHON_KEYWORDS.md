# Python Keywords Reference

Keywords are reserved words with special meaning in Python syntax. You cannot use them as variable, function, or class names.

## Quick Mental Model

Think in **grammar roles**:

1. **Values & logic**: `True`, `False`, `None`, `and`, `or`, `not`, `is`, `in`
2. **Control flow**: `if`, `elif`, `else`, `match`, `case`, `for`, `while`, `break`, `continue`, `pass`
3. **Definition & structure**: `def`, `return`, `yield`, `class`, `lambda`
4. **Errors & assertions**: `try`, `except`, `finally`, `raise`, `assert`
5. **Imports & scope**: `import`, `from`, `as`, `global`, `nonlocal`
6. **Resource and async flow**: `with`, `async`, `await`
7. **Binding/deletion**: `del`

## Full Keyword Table

| Keyword | Category | Meaning | Example |
|---|---|---|---|
| `False` | Value | Boolean false literal | `flag = False` |
| `None` | Value | Absence of value | `result = None` |
| `True` | Value | Boolean true literal | `enabled = True` |
| `and` | Logic | Logical conjunction | `if a and b:` |
| `as` | Import/context | Alias binding | `import math as m` |
| `assert` | Error/debug | Runtime assertion check | `assert x > 0` |
| `async` | Async | Declares async function/context | `async def fetch(): ...` |
| `await` | Async | Waits for awaitable result | `data = await fetch()` |
| `break` | Loop control | Exit nearest loop | `break` |
| `case` | Pattern matching | Branch in `match` statement | `case 404:` |
| `class` | Definition | Class declaration | `class User: ...` |
| `continue` | Loop control | Skip to next iteration | `continue` |
| `def` | Definition | Function declaration | `def add(a, b): ...` |
| `del` | Binding | Delete name/item/attribute | `del items[0]` |
| `elif` | Control flow | Additional conditional branch | `elif score > 80:` |
| `else` | Control flow | Fallback branch | `else:` |
| `except` | Error handling | Catch exception branch | `except ValueError:` |
| `finally` | Error handling | Always-run cleanup branch | `finally: close()` |
| `for` | Loop | Iterate over iterable | `for x in nums:` |
| `from` | Import | Selective import | `from os import path` |
| `global` | Scope | Use module-level binding | `global total` |
| `if` | Control flow | Conditional branch | `if ready:` |
| `import` | Import | Import module/package | `import json` |
| `in` | Membership/loop | Membership test or loop syntax | `if x in data:` |
| `is` | Identity | Object identity comparison | `if x is None:` |
| `lambda` | Definition | Anonymous function expression | `lambda x: x * 2` |
| `match` | Pattern matching | Structural matching statement | `match value:` |
| `nonlocal` | Scope | Use enclosing function binding | `nonlocal count` |
| `not` | Logic | Logical negation | `if not items:` |
| `or` | Logic | Logical disjunction | `if a or b:` |
| `pass` | Placeholder | No-op statement | `pass` |
| `raise` | Error handling | Raise exception | `raise ValueError("bad")` |
| `return` | Function flow | Return function result | `return total` |
| `try` | Error handling | Start exception block | `try:` |
| `while` | Loop | Condition-based loop | `while n > 0:` |
| `with` | Resource management | Context manager scope | `with open(path) as f:` |
| `yield` | Generator flow | Produce lazy sequence value | `yield item` |

## Category Deep Dive

## 1) Values and Boolean Logic

```python
is_admin = True
is_active = False
user = None

if is_admin and not is_active:
    print("Admin exists but account is inactive")

if user is None:
    print("No user object yet")
```

### `is` vs `==`

| Operator | Meaning |
|---|---|
| `==` | Value equality |
| `is` | Identity (same object in memory) |

Use `is None` and `is not None` for sentinel checks.

## 2) Control Flow and Branching

```python
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

### Pattern matching (`match` / `case`)

```python
def describe_http(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Other"
```

Pattern matching is ideal when you would otherwise chain many `if/elif` branches on a known structure.

## 3) Loop Control Keywords

```python
for n in range(1, 8):
    if n % 2 == 0:
        continue
    if n > 5:
        break
    print(n)  # 1, 3, 5
```

Use `pass` as a temporary placeholder during development:

```python
def todo_handler(event):
    pass
```

## 4) Function and Class Structure

```python
def area(width, height):
    return width * height

square = lambda x: x * x

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value
```

### Generator with `yield`

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1
```

`yield` turns a function into a lazy generator, which is memory efficient for large data streams.

## 5) Exception Flow Keywords

```python
def parse_int(text):
    try:
        value = int(text)
    except ValueError:
        raise ValueError(f"Cannot parse integer from: {text!r}")
    else:
        return value
    finally:
        print("parse_int completed")
```

### Error-handling mental model

- **`try`**: risky operation
- **`except`**: known failure path
- **`else`**: success-only path
- **`finally`**: cleanup that must always run

## 6) Scope Keywords (`global`, `nonlocal`)

```python
total_calls = 0

def ping_global():
    global total_calls
    total_calls += 1


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

Prefer passing values and returning results before reaching for `global`.

## 7) Imports and Aliases

```python
import math as m
from datetime import datetime as dt

print(m.sqrt(16))
print(dt.now())
```

Guideline: use `import module` for clarity in larger files; use `from ... import ...` for tight, frequently used symbols.

## 8) Async Keywords

```python
import asyncio

async def fetch_value():
    await asyncio.sleep(0.1)
    return 42

async def main():
    value = await fetch_value()
    print(value)
```

`async` marks coroutine definitions; `await` yields control until awaited work completes.

## Common Mistakes and Fixes

| Mistake | Why it happens | Correct approach |
|---|---|---|
| `if value == None:` | Confusing equality with identity for singleton | Use `if value is None:` |
| Shadowing keyword (`class = 1`) | Using reserved words as names | Rename variable (`class_name`) |
| Broad `except:` everywhere | Hides programming errors | Catch specific exceptions |
| Overusing `global` | Makes state hard to reason about | Prefer function args/returns or objects |
| Using `lambda` for complex logic | Hurts readability | Use `def` with a proper name |

## Practice Drills

- Rewrite nested `if/elif` status code logic using `match/case`.
- Implement a generator (`yield`) that streams filtered lines from a file.
- Refactor a function that uses global state into closure with `nonlocal`.
- Write `try/except/else/finally` for a file parse workflow.

Keywords define Python's grammar; mastering them makes code more readable, maintainable, and idiomatic.

## Keyword Interactions and Patterns

## Loop `else` with `for`/`while`

Python loops support an `else` clause that runs only if loop did **not** exit via `break`.

```python
def contains_prime(nums):
    for n in nums:
        if n > 1 and all(n % d for d in range(2, int(n**0.5) + 1)):
            break
    else:
        return False
    return True
```

## `try` + `else` for clarity

```python
def read_int(text):
    try:
        value = int(text)
    except ValueError:
        return None
    else:
        return value
```

Use `else` to separate success path from exception handling path.

## `with` + `as`

```python
with open("data.txt", "r", encoding="utf-8") as f:
    first_line = f.readline()
```

`as` binds context-managed value cleanly.

## `from ... import ... as ...`

```python
from collections import defaultdict as dd
counts = dd(int)
```

## Pattern Matching Features with `match/case`

```python
def classify(obj):
    match obj:
        case {"type": "point", "x": x, "y": y}:
            return f"Point({x}, {y})"
        case [first, *rest]:
            return f"List start={first}, rest={rest}"
        case _:
            return "Unknown"
```

## Scope Strategy Summary

| Keyword | Scope it affects | Typical use |
|---|---|---|
| `global` | Module scope | Mutating module-level state |
| `nonlocal` | Enclosing function scope | Closures with state |

## Reserved Words Checklist

Before naming variables/functions/classes, avoid keyword collisions (`class`, `def`, `return`, etc.).
Use suffix alternatives:
- `class_`
- `from_`
- `lambda_fn`

## Keyword Fluency Drill

- Convert a procedural script into functions with `def`, `return`, and explicit `raise`.
- Replace a long `if/elif` chain with `match/case`.
- Add `try/except/else/finally` around parsing I/O boundary.
- Refactor mutable closure state using `nonlocal`.

Keywords are small but compositional; mastery comes from understanding how they interact inside complete program flows.

## Keyword-by-Keyword Micro-examples

```python
# assert
value = 10
assert value > 0

# del
items = [1, 2, 3]
del items[0]

# lambda
double = lambda x: x * 2

# raise
if value < 0:
    raise ValueError("negative")
```

## Decision Cheatsheet

| You need to... | Keyword(s) |
|---|---|
| Branch by condition | `if` / `elif` / `else` |
| Loop while condition true | `while` |
| Iterate over collection | `for` / `in` |
| Exit current loop | `break` |
| Skip current iteration | `continue` |
| Define reusable behavior | `def` / `return` |
| Produce lazy stream | `yield` |
| Handle failures | `try` / `except` / `finally` / `raise` |
| Manage resource scope | `with` / `as` |
| Do async operations | `async` / `await` |

## From Beginner to Advanced Keyword Mastery

1. Learn control flow and function keywords first.
2. Add exception and resource management keywords.
3. Add scope (`global`, `nonlocal`) and import organization.
4. Add pattern matching (`match`, `case`) for structured branching.
5. Practice combining keywords in realistic workflows.

Keywords are most powerful when used as composable grammar pieces rather than isolated syntax facts.
