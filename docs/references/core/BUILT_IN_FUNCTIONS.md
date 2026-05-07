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

## Extended Built-ins Cookbook

## Iterable Processing Pipelines

```python
records = [
    {"name": "Ava", "active": True, "score": 91},
    {"name": "Noah", "active": False, "score": 77},
    {"name": "Liam", "active": True, "score": 84},
]

active_scores = list(map(lambda r: r["score"], filter(lambda r: r["active"], records)))
print(active_scores)  # [91, 84]
print(sum(active_scores) / len(active_scores))
```

Equivalent comprehension form (often preferred for readability):

```python
active_scores = [r["score"] for r in records if r["active"]]
```

## Iterator Protocol in Practice (`iter`, `next`)

```python
it = iter([10, 20, 30])
print(next(it))  # 10
print(next(it))  # 20
print(next(it, "END"))  # 30
print(next(it, "END"))  # END
```

Sentinel form:

```python
# Read lines until blank line is encountered
with open("config.txt", "r", encoding="utf-8") as f:
    for line in iter(f.readline, ""):
        print(line.rstrip())
```

## Validation Recipes with `all` and `any`

```python
def validate_user(user):
    checks = [
        isinstance(user.get("username"), str),
        len(user.get("username", "")) >= 3,
        "@" in user.get("email", ""),
        any(ch.isdigit() for ch in user.get("password", "")),
    ]
    return all(checks)
```

## Numeric Built-ins Deep Dive

| Function | Advanced note |
|---|---|
| `pow(a, b, mod)` | Efficient modular exponentiation |
| `divmod(a, b)` | Better than separate `//` and `%` in intent |
| `round(x, n)` | Uses bankers rounding for halves |
| `sum(values, start)` | `start` can shift initial accumulator |

```python
print(pow(7, 256, 13))  # modular exponentiation
print(divmod(23, 5))    # (4, 3)
```

## Representation and Formatting

```python
value = 255
print(bin(value), oct(value), hex(value))
print(format(value, "08b"))   # binary padded to width 8
print(format(12345.6789, ",.2f"))
```

Useful format specifiers:

| Specifier | Meaning | Example |
|---|---|---|
| `.2f` | 2 decimal places | `3.14` |
| `,` | Thousands separator | `12,345` |
| `>10` | Right-align width 10 | padded text |
| `<10` | Left-align width 10 | padded text |
| `^10` | Center width 10 | padded text |
| `08b` | Binary with zero-padding to 8 | `00001111` |

## Sorting and Selection Patterns

```python
products = [
    {"name": "Laptop", "price": 1200, "rating": 4.8},
    {"name": "Mouse", "price": 25, "rating": 4.3},
    {"name": "Keyboard", "price": 80, "rating": 4.6},
]

cheapest = min(products, key=lambda p: p["price"])
best_rated = max(products, key=lambda p: p["rating"])
by_price = sorted(products, key=lambda p: p["price"])
```

## Type-checking and Reflection Patterns

```python
def describe_object(obj):
    print("type:", type(obj).__name__)
    print("callable:", callable(obj))
    print("id:", id(obj))
    if hasattr(obj, "__dict__"):
        print("vars:", vars(obj))
```

`isinstance` supports tuples of types:

```python
if isinstance(value, (int, float)):
    print("numeric")
```

## Dynamic Attributes (`getattr`, `setattr`, `delattr`)

```python
class Config:
    timeout = 30

cfg = Config()
print(getattr(cfg, "timeout"))
setattr(cfg, "retries", 5)
print(cfg.retries)
delattr(cfg, "retries")
```

Use dynamic access in serializers, adapters, and plugin systems.

## `property`, `classmethod`, `staticmethod`, `super`

```python
class Temperature:
    def __init__(self, c):
        self._celsius = c

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def is_valid_unit(unit):
        return unit in {"C", "F", "K"}
```

`classmethod` is constructor-like; `staticmethod` is namespace utility.

## `open` Patterns Beyond Basics

```python
# Read line-by-line to avoid loading huge files into memory
with open("large.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            print(line.rstrip())
```

```python
# Write CSV manually
rows = [("id", "name"), (1, "Ava"), (2, "Noah")]
with open("users.csv", "w", encoding="utf-8") as f:
    for row in rows:
        f.write(",".join(map(str, row)) + "\n")
```

## Dangerous Built-ins: `eval` and `exec`

Avoid them for untrusted data:

```python
expr = "2 + 2"
print(eval(expr))  # okay only for trusted constant input
```

Safer alternatives:
- data parsing: `json.loads`
- literals: `ast.literal_eval`
- dispatch maps: `{"add": add_fn}` instead of dynamic exec

## Built-ins and Performance Notes

| Scenario | Better choice |
|---|---|
| String concatenation in loop | `"".join(parts)` instead of repeated `+` |
| Manual counter loop | `enumerate` |
| Existence check in iterable repeatedly | Convert to `set` for O(1) membership |
| Sorting custom objects repeatedly | Precompute sort key when possible |

## Learning Roadmap for Built-ins

1. Master conversion + iteration built-ins.
2. Use sorting, min/max with keys on real data.
3. Learn introspection tools for debugging.
4. Use file and formatting built-ins in small utilities.
5. Understand advanced descriptors (`property`, class/static methods).

Built-ins are not just convenience—they encode Pythonic patterns used throughout professional codebases.

## Scenario-driven Built-ins Reference

## Data Cleaning Workflow

```python
def clean_and_score(rows):
    # rows: [(name, score_text), ...]
    cleaned = []
    for name, score_text in rows:
        if not name:
            continue
        try:
            score = int(score_text)
        except ValueError:
            continue
        cleaned.append((name.strip().title(), score))

    cleaned = sorted(cleaned, key=lambda r: r[1], reverse=True)
    return cleaned, sum(score for _, score in cleaned)
```

Built-ins used together: `int`, `sorted`, `sum`, `lambda`, and basic iteration.

## `zip` and `enumerate` Composition

```python
headers = ["id", "name", "age"]
row = [101, "Ava", 30]
record = dict(zip(headers, row, strict=True))

for idx, (k, v) in enumerate(record.items(), start=1):
    print(idx, k, v)
```

## Working with `range` Precisely

| Form | Meaning |
|---|---|
| `range(stop)` | `0..stop-1` |
| `range(start, stop)` | `start..stop-1` |
| `range(start, stop, step)` | Step progression |

```python
print(list(range(5)))         # [0,1,2,3,4]
print(list(range(2, 8)))      # [2,3,4,5,6,7]
print(list(range(10, 0, -2))) # [10,8,6,4,2]
```

## `slice` Objects for Reusable Slicing

```python
data = ["id", "name", "email", "role", "created_at"]
identity_fields = slice(0, 3)
print(data[identity_fields])
```

## Byte and Memory Built-ins

```python
payload = bytes([72, 73])
mutable = bytearray(payload)
mutable.append(33)
view = memoryview(mutable)
view[0] = ord("h")
print(bytes(mutable))  # b'hi!'
```

These are useful in networking, binary protocols, and high-throughput data paths.

## `globals()` and `locals()` (Introspection Notes)

```python
x = 10


def demo():
    y = 20
    print("locals keys:", sorted(locals().keys()))

print("globals has x:", "x" in globals())
demo()
```

Use for debugging and metaprogramming; avoid heavy production reliance.

## Interactive Debugging with `breakpoint`

```python
def compute(a, b):
    breakpoint()  # inspect variables in debugger
    return a + b
```

Great for local debugging sessions when stepping through real runtime state.

## Built-in Selection Matrix

| Need | Choose |
|---|---|
| Fast yes/no existence of any condition | `any(...)` |
| Require all checks pass | `all(...)` |
| Transform every element lazily | `map(...)` |
| Keep elements by predicate lazily | `filter(...)` |
| Pair multiple iterables safely | `zip(..., strict=True)` |
| Accumulate numeric totals | `sum(...)` |
| Human-readable print | `print(...)` |
| Unambiguous debug representation | `repr(...)` |

## Mini Challenge Set

1. Convert `[("a", "1"), ("b", "2")]` into `{"a": 1, "b": 2}` using built-ins.
2. Given a list of words, print indexed words using `enumerate` starting at 1.
3. Validate that all usernames are non-empty and at least one user is admin.
4. Format a report line with aligned fields using `format`.
5. Use `next(..., default)` to safely consume iterator values.

Extensive use of built-ins is one of the clearest signs of Python fluency.
