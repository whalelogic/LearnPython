# Python Data Types Reference

Data types are the foundation of Python programs. They determine what values mean, what operations are valid, and how data is stored and passed around.

## Mental Model: Value Semantics in Python

Keep these ideas in mind:

1. **Everything is an object** with a type.
2. **Names bind to objects** (variables are references, not boxes).
3. **Mutability matters** more than type names for debugging behavior.
4. **Operations are type-driven** (`+` behaves differently for numbers, strings, and lists).

## Type Families at a Glance

| Family | Types | Mutable? | Ordered? | Typical use |
|---|---|---|---|---|
| Numeric | `int`, `float`, `complex` | No | N/A | Arithmetic, counters, scientific values |
| Boolean | `bool` | No | N/A | Conditions, flags |
| Sequence | `str`, `list`, `tuple`, `range` | `str`/`tuple`/`range`: No, `list`: Yes | Yes | Text, collections, iteration |
| Binary | `bytes`, `bytearray`, `memoryview` | `bytes`: No, `bytearray`: Yes | Yes | Network/file binary data |
| Mapping | `dict` | Yes | Insertion ordered | Key-value records |
| Set | `set`, `frozenset` | `set`: Yes, `frozenset`: No | Unordered | Membership, deduplication, set algebra |
| Null | `NoneType` (`None`) | No | N/A | Missing/sentinel value |

## Numeric Types

### `int`

```python
a = 42
b = -7
c = 1_000_000  # underscores improve readability
print(type(a))
```

### `float`

```python
price = 19.99
ratio = 1e-3
print(price * ratio)
```

### `complex`

```python
z = 2 + 3j
print(z.real, z.imag)
```

### Numeric comparison table

| Operation | Example | Notes |
|---|---|---|
| Addition | `2 + 3` | Numeric types combine by coercion rules |
| Division | `5 / 2` | Always returns `float` |
| Floor division | `5 // 2` | Drops remainder |
| Modulo | `5 % 2` | Remainder |
| Exponentiation | `2 ** 8` | Power |

## Boolean Type (`bool`)

`True` and `False` are instances of `bool` (a subclass of `int`).

```python
print(True + True)   # 2
print(bool([]))      # False
print(bool([1]))     # True
```

### Truthiness rules

Falsy values include:
- `None`
- `False`
- `0`, `0.0`, `0j`
- Empty collections (`""`, `[]`, `{}`, `set()`, `tuple()`)

Everything else is truthy.

## String Type (`str`)

Strings are immutable sequences of Unicode characters.

```python
text = "Learn Python"
print(text[0])        # 'L'
print(text[-1])       # 'n'
print(text[6:])       # 'Python'
print(text.upper())   # 'LEARN PYTHON'
```

### Common string operations

| Operation | Example | Result |
|---|---|---|
| Concatenation | `"a" + "b"` | `"ab"` |
| Repetition | `"ha" * 3` | `"hahaha"` |
| Membership | `"Py" in text` | `True` |
| Formatting | `f"Hi {name}"` | Interpolated string |

## List Type (`list`)

Lists are mutable, ordered collections.

```python
nums = [1, 2, 3]
nums.append(4)
nums[0] = 10
print(nums)  # [10, 2, 3, 4]
```

### List method quick reference

| Method | Purpose |
|---|---|
| `append(x)` | Add one item to end |
| `extend(iterable)` | Add many items |
| `insert(i, x)` | Insert at position |
| `pop([i])` | Remove and return item |
| `remove(x)` | Remove first matching value |
| `sort(...)` | In-place sort |
| `reverse()` | In-place reverse |

## Tuple Type (`tuple`)

Tuples are immutable ordered collections.

```python
point = (10, 20)
x, y = point
print(x, y)
```

Use tuples when data should not change and when fixed structure helps readability.

## Range Type (`range`)

Efficient arithmetic sequence object.

```python
for i in range(2, 10, 2):
    print(i)
```

`range` is lazy and memory-efficient compared with creating full lists.

## Dictionary Type (`dict`)

Dictionaries map keys to values.

```python
user = {"name": "Ava", "age": 30}
user["city"] = "Paris"
print(user["name"])
```

### Dictionary characteristics

| Feature | Detail |
|---|---|
| Key uniqueness | Keys must be unique |
| Key constraints | Keys must be hashable |
| Order | Preserves insertion order |
| Lookup complexity | Average O(1) |

## Set Types (`set`, `frozenset`)

Set values are unique and unordered.

```python
tags = {"python", "api", "python"}
print(tags)  # {'python', 'api'}
```

```python
a = {1, 2, 3}
b = {3, 4}
print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
```

## Binary Types (`bytes`, `bytearray`, `memoryview`)

```python
raw = b"ABC"
mutable_raw = bytearray(raw)
mutable_raw[0] = 90  # 'Z'
print(bytes(mutable_raw))
```

`memoryview` allows zero-copy access to bytes-like objects:

```python
data = bytearray(b"hello")
view = memoryview(data)
view[0] = ord("H")
print(data)  # bytearray(b'Hello')
```

## `None` and Optional Data

`None` indicates "no value" or "not yet assigned".

```python
def find_user(user_id):
    return None

user = find_user(10)
if user is None:
    print("User not found")
```

## Conversion Between Types

| From | To | Example |
|---|---|---|
| String digits | `int` | `int("42")` |
| Integer | `str` | `str(42)` |
| Iterable | `list` | `list(range(3))` |
| Iterable | `set` | `set([1, 1, 2])` |
| Key-value pairs | `dict` | `dict([("a", 1), ("b", 2)])` |

## Mutability and Side Effects

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]
```

Because `a` and `b` reference the same list, mutation through one name affects the other.

### Defensive copying patterns

```python
original = [1, 2, 3]
copy1 = original[:]        # shallow copy
copy2 = list(original)     # shallow copy
```

## Identity vs Equality

```python
x = [1, 2]
y = [1, 2]
z = x

print(x == y)  # True (same value)
print(x is y)  # False (different objects)
print(x is z)  # True (same object)
```

## Choosing the Right Type

| Requirement | Preferred type |
|---|---|
| Ordered mutable collection | `list` |
| Immutable fixed record | `tuple` |
| Key-value record | `dict` |
| Fast membership + uniqueness | `set` |
| Text processing | `str` |
| Exact binary payload | `bytes` |

## Common Pitfalls

| Pitfall | Example | Fix |
|---|---|---|
| Mutable default argument | `def f(items=[]): ...` | Use `None` then create list inside |
| Float precision surprise | `0.1 + 0.2 != 0.3` | Use `decimal.Decimal` for money |
| Confusing empty with missing | `if not value:` | Distinguish `None` vs empty collection |
| Assuming set order | Iterating set for deterministic output | Sort before display (`sorted(my_set)`) |

## Practice Goals

- Build nested structures combining list/dict/set.
- Explain mutability effects without running code.
- Convert between common types safely.
- Choose data structures based on complexity and semantics.

Strong data type fluency makes every other Python topic easier: functions, OOP, exceptions, files, and APIs all depend on these fundamentals.

## Type Selection Decision Table

| Situation | Recommended type | Why |
|---|---|---|
| Need ordered mutable sequence of events | `list` | Efficient append and indexing |
| Need immutable coordinate/record | `tuple` | Prevent accidental mutation |
| Need fast lookup by identifier | `dict` | Average O(1) access |
| Need membership checks and uniqueness | `set` | Fast membership + deduplication |
| Need binary network payload | `bytes` | Immutable byte content |

## Type-hint Awareness (Conceptual)

Even though runtime types are dynamic, type hints clarify intent:

```python
def normalize_tags(tags: list[str]) -> list[str]:
    return [t.strip().lower() for t in tags if t.strip()]
```

This improves readability, IDE support, and maintainability without changing runtime behavior.

## Data Type Mastery Recap

A strong Python developer can:
- predict mutability side effects,
- choose structures by access pattern,
- convert data safely at boundaries,
- and explain identity vs equality clearly.

That foundation makes advanced topics (concurrency, APIs, data science, web backends) much easier to learn and apply.
