# Python Lists

Lists are ordered, mutable sequences. They are usually the first container beginners reach for, and for good reason: they are flexible, readable, and useful everywhere.

## Core Operations

| Method | What it does | Example |
|---|---|---|
| `append(x)` | Add one item to the end | `numbers.append(6)` |
| `extend(values)` | Add many items | `numbers.extend([7, 8])` |
| `insert(i, x)` | Insert at a position | `numbers.insert(1, 99)` |
| `remove(x)` | Remove first matching value | `numbers.remove(3)` |
| `pop()` | Remove and return an item | `last = numbers.pop()` |
| `sort()` | Sort in place | `numbers.sort()` |
| `reverse()` | Reverse in place | `numbers.reverse()` |

## Practical Examples

### Build a To-Do List
```python
tasks = ["read", "practice"]
tasks.append("build mini project")
for task in tasks:
    print(task)
```

### Slice a Window of Data
```python
temperatures = [21, 23, 24, 20, 19, 22, 25]
weekend = temperatures[-2:]
print(weekend)
```

### Transform with a Comprehension
```python
prices = [5, 12, 8]
with_tax = [round(price * 1.2, 2) for price in prices]
print(with_tax)
```

## When Lists Are Not the Best Fit

- Use a `set` when duplicates should disappear.
- Use a `dict` when named lookups matter more than position.
- Use `deque` when you need fast pops from the left.

## Related Reading

- [../Data_Structures.md](../Data_Structures.md)
- [../dictionaries/DICTIONARY.md](../dictionaries/DICTIONARY.md)
