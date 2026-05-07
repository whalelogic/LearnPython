# Python Built-in Functions

Python ships with a large set of built-in functions that are always available. Think of built-ins as your **standard toolkit**: before writing custom utility code, check whether a built-in already solves the problem clearly and efficiently.

## Mental Model: How to Learn Built-ins

Use these buckets to remember what each function family does:

| Bucket | Purpose | Typical Functions |
|---|---|---|
| Type conversion | Convert data into a target type | `int`, `float`, `str`, `list`, `tuple`, `set`, `dict`, `bool`, `bytes`, `bytearray`, `memoryview` |
| Numeric operations | Arithmetic helpers and number representation | `abs`, `round`, `pow`, `divmod`, `sum`, `min`, `max`, `bin`, `oct`, `hex` |
| Iteration & sequence utilities | Work with iterables and loops | `len`, `range`, `enumerate`, `zip`, `iter`, `next`, `reversed`, `sorted`, `map`, `filter`, `all`, `any` |
| Introspection | Inspect objects and runtime state | `type`, `isinstance`, `issubclass`, `dir`, `vars`, `id`, `hash`, `callable`, `help` |
| Attribute/object helpers | Dynamic attribute access and object behavior | `getattr`, `setattr`, `hasattr`, `delattr`, `property`, `classmethod`, `staticmethod`, `super`, `object` |
| I/O & execution | Input/output and dynamic code execution | `print`, `input`, `open`, `compile`, `eval`, `exec`, `breakpoint`, `__import__` |
| Representation | Human- and developer-facing text representations | `repr`, `format`, `ascii`, `chr`, `ord` |

## Complete Built-in Function Table

| Function | Short description |
|---|---|
| `abs(x)` | Absolute value |
| `all(iterable)` | `True` if every element is truthy |
| `any(iterable)` | `True` if at least one element is truthy |
| `ascii(obj)` | ASCII-only representation string |
| `bin(x)` | Binary string for an integer |
| `bool(x)` | Convert to Boolean |
| `breakpoint()` | Enter debugger |
| `bytearray(...)` | Mutable bytes sequence |
| `bytes(...)` | Immutable bytes sequence |
| `callable(obj)` | Whether object can be called |
| `chr(i)` | Character for Unicode code point |
| `classmethod(func)` | Class-bound method descriptor |
| `compile(src, filename, mode)` | Compile source to code object |
| `complex(...)` | Create complex number |
| `delattr(obj, name)` | Delete attribute |
| `dict(...)` | Create dictionary |
| `dir(obj)` | List attributes |
| `divmod(a, b)` | Quotient and remainder tuple |
| `enumerate(iterable, start=0)` | Indexed iteration |
| `eval(expr)` | Evaluate expression string |
| `exec(code)` | Execute statements |
| `filter(func, iterable)` | Keep elements where predicate is true |
| `float(x)` | Convert to float |
| `format(value, spec='')` | Format using format spec mini-language |
| `frozenset(iterable)` | Immutable set |
| `getattr(obj, name[, default])` | Read attribute dynamically |
| `globals()` | Global namespace dict |
| `hasattr(obj, name)` | Check if attribute exists |
| `hash(obj)` | Hash value |
| `help(obj)` | Interactive help |
| `hex(x)` | Hex string for integer |
| `id(obj)` | Identity value |
| `input(prompt='')` | Read text from stdin |
| `int(x=0, base=10)` | Convert to integer |
| `isinstance(obj, classinfo)` | Runtime type check |
| `issubclass(cls, classinfo)` | Subclass check |
| `iter(obj[, sentinel])` | Iterator from iterable/callable |
| `len(obj)` | Number of items |
| `list(iterable)` | Create list |
| `locals()` | Local namespace dict |
| `map(func, *iterables)` | Apply function across iterables |
| `max(...)` | Largest item |
| `memoryview(obj)` | View bytes-like object without copying |
| `min(...)` | Smallest item |
| `next(iterator[, default])` | Next iterator element |
| `object()` | Base object |
| `oct(x)` | Octal string for integer |
| `open(file, mode='r', ...)` | Open file |
| `ord(c)` | Unicode code point for one-character string |
| `pow(x, y[, mod])` | Exponentiation (or modular exponentiation) |
| `print(*args, sep=' ', end='\n', ...)` | Print values |
| `property(...)` | Managed attribute descriptor |
| `range(...)` | Arithmetic progression sequence |
| `repr(obj)` | Developer-oriented representation |
| `reversed(seq)` | Reverse iterator |
| `round(number[, ndigits])` | Rounded value |
| `set(iterable)` | Create set |
| `setattr(obj, name, value)` | Set attribute dynamically |
| `slice(stop)` / `slice(start, stop, step)` | Slice object |
| `sorted(iterable, key=None, reverse=False)` | Return sorted list |
| `staticmethod(func)` | Static method descriptor |
| `str(obj='')` | Convert to string |
| `sum(iterable, start=0)` | Sum values |
| `super([type[, object]])` | Proxy to parent class methods |
| `tuple(iterable)` | Create tuple |
| `type(obj)` / `type(name, bases, ns)` | Inspect/create type |
| `vars([obj])` | Namespace dictionary |
| `zip(*iterables, strict=False)` | Combine iterables elementwise |
| `__import__(name, ...)` | Low-level import function |

## Core Usage Patterns (with Examples)

### 1) Transform then aggregate

```python
prices = [19.99, 5.25, 12.40]
rounded_total = round(sum(prices), 2)
print(rounded_total)  # 37.64
```

### 2) Validate all/any conditions

```python
password_checks = [len("MyPass123!") >= 8, any(c.isdigit() for c in "MyPass123!")]
print(all(password_checks))  # True
```

### 3) Iterate with index safely

```python
for i, item in enumerate(["apple", "banana", "pear"], start=1):
    print(i, item)
```

### 4) Sort by custom key

```python
students = [("Ana", 92), ("Sam", 85), ("Lee", 98)]
by_score_desc = sorted(students, key=lambda pair: pair[1], reverse=True)
print(by_score_desc)
```

### 5) Parallel iteration

```python
names = ["A", "B", "C"]
scores = [10, 20, 30]
for name, score in zip(names, scores, strict=True):
    print(name, score)
```

## High-Value Built-ins by Real Use Case

| Task | Best built-ins |
|---|---|
| Convert user input to typed values | `int`, `float`, `bool`, `str` |
| Generate loop counters and ranges | `range`, `enumerate` |
| Combine and split iteration streams | `zip`, `iter`, `next` |
| Filter and transform collections | `filter`, `map`, list comprehensions |
| Quick checks on data quality | `all`, `any`, `isinstance`, `len` |
| Format user-facing output | `print`, `format`, `round`, `repr` |
| Read/write files | `open` with `with` context manager |
| Runtime object inspection | `dir`, `vars`, `type`, `getattr` |

## Subtle Behaviors to Know

| Function | Gotcha | Better practice |
|---|---|---|
| `bool("False")` | Non-empty strings are truthy | Parse text explicitly (`s.lower() == "true"`) |
| `round(2.675, 2)` | Floating-point representation surprises | Use `decimal.Decimal` for financial values |
| `max([])` / `min([])` | Raises `ValueError` on empty input | Use `default=` when appropriate |
| `zip(a, b)` | Stops at shortest iterable | Use `strict=True` to catch length mismatches |
| `sum()` on strings | Not supported for concatenation | Use `"".join(strings)` |
| `eval` / `exec` | Security risk on untrusted input | Avoid unless source is fully trusted |

## File I/O Reference (`open`)

| Mode | Meaning |
|---|---|
| `r` | Read text (default) |
| `w` | Write text, truncate existing |
| `a` | Append text |
| `x` | Create new file, fail if exists |
| `b` | Binary mode modifier |
| `t` | Text mode modifier (default) |
| `+` | Update mode (read/write) modifier |

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Built-ins reduce boilerplate.\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

## Introspection and Metaprogramming Example

```python
class User:
    def __init__(self, name):
        self.name = name

u = User("Iris")
print(type(u))
print(hasattr(u, "name"))
print(getattr(u, "name"))
setattr(u, "active", True)
print(vars(u))
```

## Security Notes

- Never use `eval` or `exec` with user-controlled input.
- Prefer explicit parsers (`json.loads`, `ast.literal_eval` for safe literals where appropriate).
- Validate file paths and permissions before `open` in sensitive applications.

## Practice Checklist

Use this checklist to verify built-in fluency:

- Convert among `str`, `int`, `float`, `list`, `tuple`, `set`, and `dict`.
- Use `enumerate`, `zip`, and `sorted(key=...)` in real loops.
- Apply `all` and `any` for concise validation.
- Inspect unknown objects with `type`, `dir`, and `vars`.
- Use `open(..., encoding="utf-8")` and `with` blocks consistently.

Mastering these built-ins gives you strong leverage across the entire language.
