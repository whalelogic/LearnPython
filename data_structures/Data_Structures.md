# Python Data Structures

## Built-in Structures at a Glance

| Data Structure | Mutable? | Ordered? | Duplicates? | Best for |
|---|---|---|---|---|
| `list` | Yes | Yes | Yes | Sequences you append to and iterate over |
| `tuple` | No | Yes | Yes | Fixed records and function return groups |
| `set` | Yes | No | No | Membership tests and uniqueness |
| `dict` | Yes | Yes | Keys: No | Named fields and fast lookups |

## Concrete Examples

### List
```python
queue = ["first", "second"]
queue.append("third")
print(queue.pop(0))
```

### Tuple
```python
point = (3, 7)
x, y = point
print(x, y)
```

### Set
```python
tags = {"python", "api", "python", "docs"}
print(tags)
print("api" in tags)
```

### Dictionary
```python
user = {"name": "Ari", "role": "student"}
user["active"] = True
print(user["name"])
```

## When to Reach for Other Structures

### Stack (LIFO)
Use a `list` or `deque` when the newest item should be removed first.

```python
stack = []
stack.append("open menu")
stack.append("edit item")
print(stack.pop())
```

### Queue (FIFO)
Use `collections.deque` when the oldest item should leave first.

```python
from collections import deque

jobs = deque(["email", "report", "backup"])
print(jobs.popleft())
```

### Heap / Priority Queue
Use `heapq` when the smallest or highest-priority item should come out first.

```python
import heapq

items = []
heapq.heappush(items, (2, "normal"))
heapq.heappush(items, (1, "urgent"))
print(heapq.heappop(items))
```

## A Useful Comparison Question

Before choosing a structure, ask yourself:

1. Do I need order?
2. Do I need uniqueness?
3. Will I look things up by name?
4. Will I add and remove items frequently?

Those four questions usually point you to the right default.

## Related Reading

- [README.md](README.md)
- [lists/README.md](lists/README.md)
- [dictionaries/README.md](dictionaries/README.md)
- [algorithms/README.md](algorithms/README.md)
