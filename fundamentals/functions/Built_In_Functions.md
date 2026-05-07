# Python Built-in Functions

Built-in functions are available immediately—no import required. Learning a few of them well saves you from writing a lot of unnecessary code.

## Core Groups to Know Early

| Category | Functions | Why they matter |
|---|---|---|
| Output and debugging | `print()`, `repr()` | See values clearly while learning |
| Measuring and checking | `len()`, `type()`, `isinstance()` | Inspect data before using it |
| Iteration | `range()`, `enumerate()`, `zip()` | Loop over data with less manual bookkeeping |
| Conversion | `int()`, `float()`, `str()`, `list()`, `dict()` | Turn data into the shape you need |
| Aggregation | `sum()`, `min()`, `max()`, `sorted()` | Answer common questions in one call |

## Everyday Examples

### `len()` and `sum()`
```python
scores = [88, 91, 76, 95]
print(len(scores))
print(sum(scores) / len(scores))
```

### `enumerate()`
```python
tasks = ["read", "practice", "review"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
```

### `zip()`
```python
names = ["Ada", "Grace", "Linus"]
roles = ["math", "compiler", "kernel"]
for name, role in zip(names, roles):
    print(f"{name}: {role}")
```

### `sorted()` with a key
```python
students = [
    {"name": "Ava", "score": 91},
    {"name": "Ben", "score": 84},
    {"name": "Cara", "score": 95},
]

ranked = sorted(students, key=lambda student: student["score"], reverse=True)
print(ranked)
```

## A Small Real-World Pattern

```python
raw_prices = ["19.99", "5.50", "12.00"]
prices = [float(value) for value in raw_prices]
print(f"items={len(prices)} total={sum(prices):.2f}")
```

This combines conversion, measuring, and aggregation in a way you will use often in scripts and APIs.

## Common Mistakes to Avoid

- Forgetting that `map()` and `zip()` return iterators in Python 3
- Using `list.sort()` when you actually need a new sorted copy from `sorted()`
- Calling `int()` or `float()` without handling bad input
- Rewriting loops that `sum()`, `any()`, or `all()` already solve cleanly

## Related Reading

- [../README.md](../README.md)
- [../core/BUILT_IN_FUNCTIONS.md](../core/BUILT_IN_FUNCTIONS.md)
- [../../standard_library/Built_In_Functions.md](../../standard_library/Built_In_Functions.md)
