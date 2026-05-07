# Python Dictionary Reference

Dictionaries (`dict`) are Python's core key-value data structure. They power configurations, JSON-like payloads, indexing, caching, counting, and object-style records.

## Mental Model

Think of a dictionary as:

- a fast lookup table from **key → value**,
- preserving insertion order,
- optimized for reads/writes by key (average O(1)).

## Dictionary Essentials

```python
person = {
    "name": "Alice",
    "age": 30,
    "skills": ["python", "sql"],
}

print(person["name"])      # Alice
person["city"] = "Berlin"
```

## Method Reference Table

| Method | What it does | Example |
|---|---|---|
| `clear()` | Remove all entries | `person.clear()` |
| `copy()` | Shallow copy | `clone = person.copy()` |
| `fromkeys(iterable, value=None)` | Create dict from keys | `dict.fromkeys(["a", "b"], 0)` |
| `get(key, default=None)` | Read safely with default | `person.get("country", "N/A")` |
| `items()` | View key-value pairs | `for k, v in person.items(): ...` |
| `keys()` | View keys | `list(person.keys())` |
| `pop(key[, default])` | Remove key and return value | `age = person.pop("age")` |
| `popitem()` | Remove and return last inserted pair | `k, v = person.popitem()` |
| `setdefault(key[, default])` | Return existing or set default | `person.setdefault("active", True)` |
| `update([other], **kwargs)` | Merge mappings | `person.update({"age": 31})` |
| `values()` | View values | `list(person.values())` |

## Access Patterns

### Direct indexing vs `get`

| Pattern | Behavior on missing key |
|---|---|
| `d[key]` | Raises `KeyError` |
| `d.get(key)` | Returns `None` |
| `d.get(key, default)` | Returns default value |

```python
settings = {"theme": "dark"}
print(settings.get("font", "system"))  # system
```

Use `d[key]` when missing keys are truly exceptional; use `get` when absence is expected.

## Updating and Merging

```python
base = {"host": "localhost", "port": 5432}
overrides = {"port": 5433, "ssl": True}

merged = base | overrides          # Python 3.9+
print(merged)

base.update(overrides)             # in-place
```

## Iteration Patterns

```python
scores = {"Ava": 91, "Noah": 88, "Liam": 95}

for name in scores:                 # keys by default
    print(name)

for score in scores.values():
    print(score)

for name, score in scores.items():
    print(name, score)
```

## Building Dictionaries

### Dictionary comprehension

```python
squares = {n: n * n for n in range(1, 6)}
```

### From pairs

```python
pairs = [("x", 1), ("y", 2)]
coords = dict(pairs)
```

### Grouping use case

```python
words = ["apple", "apricot", "banana", "blueberry"]
by_initial = {}
for w in words:
    by_initial.setdefault(w[0], []).append(w)
```

## Copying and Nested Data

`copy()` is shallow.

```python
original = {"user": {"name": "Ivy"}}
clone = original.copy()
clone["user"]["name"] = "Mia"
print(original["user"]["name"])  # Mia
```

For deep copies of nested mutable structures, use `copy.deepcopy`.

## Key Requirements

Dictionary keys must be hashable (immutable types like `str`, `int`, tuples of hashables).

```python
valid = {(1, 2): "point"}
# invalid = {[1, 2]: "point"}  # TypeError: unhashable type: 'list'
```

## Time Complexity (Average Case)

| Operation | Complexity |
|---|---|
| Lookup by key | O(1) |
| Insert/update by key | O(1) |
| Delete by key | O(1) |
| Iteration | O(n) |

Worst-case hash collisions can degrade performance, but Python's implementation is robust for normal usage.

## Common Idioms

### Counting

```python
text = "banana"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
```

(Also consider `collections.Counter`.)

### Inverting a mapping (when values are unique)

```python
user_to_id = {"ava": 101, "liam": 102}
id_to_user = {v: k for k, v in user_to_id.items()}
```

### Sorting dictionaries

```python
data = {"b": 2, "a": 1, "c": 3}
by_key = dict(sorted(data.items()))
by_value = dict(sorted(data.items(), key=lambda kv: kv[1]))
```

## Error Handling Patterns

```python
inventory = {"pen": 10}

try:
    inventory["pencil"] -= 1
except KeyError:
    inventory["pencil"] = 0
```

Better:

```python
inventory["pencil"] = inventory.get("pencil", 0) - 1
```

## Comparing Related Types

| Requirement | Recommended type |
|---|---|
| Unique unordered values | `set` |
| Ordered mutable sequence | `list` |
| Keyed record/lookup | `dict` |
| Immutable fixed record | `tuple` |

## Pitfalls and Best Practices

| Pitfall | Example | Recommendation |
|---|---|---|
| Assuming key order in very old Python versions | Legacy assumptions | In modern Python, insertion order is preserved |
| Mutating dict while iterating over it | Runtime error / logic bugs | Iterate over `list(d.items())` if mutating |
| Using mutable keys | `TypeError` or bad semantics | Use immutable hashable keys |
| Deep nested indexing without checks | `KeyError` chains | Use `get`, validation, or helper access functions |

## Mini Real-world Example: Configuration Overlay

```python
def merged_config(defaults, env_overrides, cli_overrides):
    cfg = defaults.copy()
    cfg.update(env_overrides)
    cfg.update(cli_overrides)
    return cfg

base = {"timeout": 30, "retries": 3, "log_level": "INFO"}
env = {"timeout": 45}
cli = {"log_level": "DEBUG"}

print(merged_config(base, env, cli))
```

## Practice Goals

- Use `get`, `setdefault`, and `update` confidently.
- Build dictionaries with comprehensions.
- Explain shallow vs deep copy behavior.
- Choose key types correctly and safely.

Dictionaries are central to Python fluency. Once mastered, they unlock cleaner code for APIs, data processing, and application architecture.
