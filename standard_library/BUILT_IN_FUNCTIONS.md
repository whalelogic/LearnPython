# Built-in Functions in Practice

Built-in functions are the shortest path from a problem to a working solution. They are fast, well-tested, and available everywhere.

## High-Value Functions

### Inspect and Convert
```python
value = "42"
print(type(value))
print(int(value) + 8)
```

### Iterate Cleanly
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

### Aggregate
```python
numbers = [5, 8, 2, 9]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

### Sort Complex Data
```python
files = [
    {"name": "report.txt", "size": 1200},
    {"name": "notes.md", "size": 300},
]

smallest_first = sorted(files, key=lambda item: item["size"])
print(smallest_first)
```

## Common Pairs to Remember

| Pair | Typical use |
|---|---|
| `iter()` + `next()` | Manual iteration |
| `open()` + `with` | Safe file handling |
| `zip()` + unpacking | Combine related sequences |
| `any()` / `all()` | Boolean checks over many values |

## Related Context

Built-ins usually work best together with standard-library modules. For example, `open()` pairs naturally with `json`, `csv`, and `pathlib`, while `sorted()` often appears before output or reporting.

---

## Deep Reference

### Complete Built-in Function Table

| Function | Category | Short description |
|---|---|---|
| `abs(x)` | Numeric | Absolute value |
| `all(iterable)` | Iteration | `True` if every element is truthy (vacuously true for empty) |
| `any(iterable)` | Iteration | `True` if at least one element is truthy |
| `ascii(obj)` | Representation | Like `repr` but escapes non-ASCII characters |
| `bin(x)` | Numeric | Binary string e.g. `'0b1010'` |
| `bool(x)` | Type conversion | Convert to `True` or `False` |
| `breakpoint()` | Debugging | Drop into `pdb` (or `PYTHONBREAKPOINT` override) |
| `bytearray(...)` | Type conversion | Mutable bytes sequence |
| `bytes(...)` | Type conversion | Immutable bytes sequence |
| `callable(obj)` | Introspection | Whether object can be called |
| `chr(i)` | Representation | Character for Unicode code point |
| `classmethod(fn)` | OOP | Class-bound method descriptor |
| `compile(src, file, mode)` | Execution | Compile source to code object |
| `complex(...)` | Type conversion | Create complex number |
| `delattr(obj, name)` | Attribute ops | Delete named attribute |
| `dict(...)` | Type conversion | Create dictionary |
| `dir(obj)` | Introspection | List attributes |
| `divmod(a, b)` | Numeric | `(a // b, a % b)` in one call |
| `enumerate(iter, start=0)` | Iteration | `(index, value)` pairs |
| `eval(expr)` | Execution | Evaluate expression string |
| `exec(code)` | Execution | Execute statements |
| `filter(fn, iter)` | Iteration | Keep elements where predicate is truthy |
| `float(x)` | Type conversion | Convert to float |
| `format(value, spec='')` | Representation | Format using mini-language spec |
| `frozenset(iter)` | Type conversion | Immutable set |
| `getattr(obj, name[, default])` | Attribute ops | Read attribute dynamically |
| `globals()` | Introspection | Global namespace dict |
| `hasattr(obj, name)` | Introspection | Check attribute existence |
| `hash(obj)` | Introspection | Hash value (must be hashable) |
| `help(obj)` | Introspection | Interactive help |
| `hex(x)` | Numeric | Hex string e.g. `'0xff'` |
| `id(obj)` | Introspection | Identity (memory address) |
| `input(prompt='')` | I/O | Read a line from stdin |
| `int(x=0, base=10)` | Type conversion | Convert to integer |
| `isinstance(obj, classinfo)` | Introspection | Runtime type check (supports tuple of types) |
| `issubclass(cls, classinfo)` | Introspection | Subclass relationship check |
| `iter(obj[, sentinel])` | Iteration | Get iterator from iterable or callable |
| `len(obj)` | Sequence | Number of items |
| `list(iter)` | Type conversion | Create list |
| `locals()` | Introspection | Local namespace dict |
| `map(fn, *iters)` | Iteration | Apply function element-wise |
| `max(*args or iter, key=, default=)` | Numeric | Largest item |
| `memoryview(obj)` | Type conversion | Zero-copy buffer view |
| `min(*args or iter, key=, default=)` | Numeric | Smallest item |
| `next(iter[, default])` | Iteration | Next element from iterator |
| `object()` | OOP | Base object instance |
| `oct(x)` | Numeric | Octal string e.g. `'0o17'` |
| `open(file, mode='r', ...)` | I/O | Open file |
| `ord(c)` | Representation | Unicode code point for one-char string |
| `pow(x, y[, mod])` | Numeric | Exponentiation; `pow(x,y,mod)` is modular |
| `print(*args, sep=' ', end='\n', file=, flush=)` | I/O | Print values |
| `property(fget, fset, fdel, doc)` | OOP | Managed attribute descriptor |
| `range(stop)` / `range(start, stop, step)` | Iteration | Arithmetic integer sequence |
| `repr(obj)` | Representation | Developer-oriented string |
| `reversed(seq)` | Iteration | Reverse iterator |
| `round(number[, ndigits])` | Numeric | Rounded value (banker's rounding) |
| `set(iter)` | Type conversion | Create set |
| `setattr(obj, name, value)` | Attribute ops | Set attribute dynamically |
| `slice(stop)` / `slice(start, stop, step)` | Sequence | Slice object |
| `sorted(iter, key=None, reverse=False)` | Iteration | New sorted list |
| `staticmethod(fn)` | OOP | Static method descriptor |
| `str(obj='')` | Type conversion | Convert to string |
| `sum(iter, start=0)` | Numeric | Sum values |
| `super([type[, obj]])` | OOP | Proxy to parent class |
| `tuple(iter)` | Type conversion | Create tuple |
| `type(obj)` / `type(name, bases, ns)` | Introspection / OOP | Inspect or create type |
| `vars([obj])` | Introspection | `__dict__` of object |
| `zip(*iters, strict=False)` | Iteration | Combine iterables element-wise |
| `__import__(name, ...)` | Execution | Low-level import |

### Function Families by Task

| Task | Best built-ins |
|---|---|
| Convert user input | `int`, `float`, `bool`, `str`, `list`, `tuple`, `set`, `dict` |
| Iterate with index | `enumerate` |
| Pair multiple sequences | `zip` (add `strict=True` to catch length mismatches) |
| Filter and transform | `filter`, `map`, or list/generator comprehensions |
| Boolean checks | `all`, `any` |
| Sorting | `sorted(key=...)`, `min(key=...)`, `max(key=...)` |
| Aggregation | `sum`, `min`, `max`, `len` |
| File I/O | `open` inside a `with` block |
| Inspect unknown objects | `type`, `isinstance`, `dir`, `vars`, `hasattr`, `callable` |
| Dynamic attribute access | `getattr`, `setattr`, `delattr` |
| Format output | `print`, `format`, `repr`, `str`, `chr`, `ord` |
| Number bases | `bin`, `oct`, `hex` |

### Annotated Patterns

#### Validate all/any conditions

```python
def validate_user(user: dict) -> bool:
    return all([
        isinstance(user.get("username"), str),
        len(user.get("username", "")) >= 3,
        "@" in user.get("email", ""),
        any(ch.isdigit() for ch in user.get("password", "")),
    ])
```

#### Sort complex data

```python
products = [
    {"name": "Laptop", "price": 1200, "rating": 4.8},
    {"name": "Mouse",  "price": 25,   "rating": 4.3},
]

cheapest    = min(products, key=lambda p: p["price"])
best_rated  = max(products, key=lambda p: p["rating"])
by_price    = sorted(products, key=lambda p: p["price"])
```

#### Lazy pipeline with `map` and `filter`

```python
records = [{"name": "Ava", "active": True, "score": 91},
           {"name": "Noah", "active": False, "score": 77}]

active_scores = list(map(
    lambda r: r["score"],
    filter(lambda r: r["active"], records)
))
# Equivalent comprehension (often preferred):
active_scores = [r["score"] for r in records if r["active"]]
```

#### Safe iterator consumption

```python
it = iter([10, 20, 30])
print(next(it))          # 10
print(next(it, "DONE"))  # 20
print(next(it, "DONE"))  # 30
print(next(it, "DONE"))  # DONE  — no StopIteration
```

#### `zip` with strict length enforcement

```python
headers = ["id", "name", "age"]
row     = [101, "Ava", 30]
record  = dict(zip(headers, row, strict=True))
# strict=True raises ValueError if lengths differ
```

#### Dynamic attribute access pattern

```python
class Config:
    timeout = 30

cfg = Config()
for key in ("timeout", "retries", "debug"):
    print(key, getattr(cfg, key, None))   # no AttributeError
```

### `open()` Modes Reference

| Mode | Meaning |
|---|---|
| `r` | Read text (default) |
| `w` | Write text, truncate existing |
| `a` | Append text |
| `x` | Create new file; fail if exists |
| `b` | Binary modifier (combine with above) |
| `t` | Text modifier (default) |
| `+` | Update (read + write) |

### Subtle Behaviors

| Function | Gotcha | Fix |
|---|---|---|
| `bool("False")` | Any non-empty string is truthy | Parse explicitly: `s.lower() == "true"` |
| `round(2.675, 2)` | Floating-point surprises; may return `2.67` | Use `decimal.Decimal` for money |
| `max([])` | Raises `ValueError` on empty input | Use `default=` keyword |
| `zip(a, b)` | Silently stops at shortest | Add `strict=True` to catch mismatches |
| `sum` on strings | `TypeError` — not supported | Use `"".join(strings)` |
| `eval` / `exec` | Security risk on untrusted input | Avoid; use `json.loads` or `ast.literal_eval` |
| `sorted` returns a list | Does not sort the original | Use `.sort()` to sort in place |

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Convert types, iterate with `range` and `enumerate`, use `print` and `len` |
| **Developing** | Use `zip`, `sorted(key=)`, `map`, `filter`, `all`, `any` in real problems |
| **Proficient** | Apply `min`/`max` with keys, use introspection tools, handle `iter`/`next` protocol |
| **Advanced** | Replace loops with built-in pipelines, use `getattr`/`setattr` in dynamic code, understand `property` and descriptor protocol |

### Suggested Practice Projects

1. **Data normalizer** — Read a list of dicts, validate all required fields with `all`/`any`, sort by a field, and print a formatted report.
2. **Type converter** — Accept a string from input and convert to int/float/bool with proper error handling.
3. **Record merger** — Use `zip(strict=True)` to combine two lists of equal length into a list of dicts.
4. **Object inspector** — Write a function using `dir`, `getattr`, `callable`, and `isinstance` to print a human-readable summary of any object.
5. **Custom sort** — Sort a list of tuples by the second element descending, then by the first element ascending.

