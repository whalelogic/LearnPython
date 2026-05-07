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
