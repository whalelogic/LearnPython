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

---

## Deep Reference

### Choosing the Right Structure

Answer these four questions before writing a line of code:

| Question | Points to |
|---|---|
| Do I need to look things up by name? | `dict` |
| Do I need fast membership tests? | `set` |
| Is the order fixed and data immutable? | `tuple` |
| Do I need to append, pop, or sort? | `list` |
| FIFO queue with fast pops from both ends? | `collections.deque` |
| Priority queue (always get smallest first)? | `heapq` / `queue.PriorityQueue` |
| Named fields without a full class? | `collections.namedtuple` or `dataclasses.dataclass` |
| Counting occurrences? | `collections.Counter` |
| Dict with default values? | `collections.defaultdict` |

### Built-in Type Method Reference

#### `list` methods

| Method | Description | Example |
|---|---|---|
| `.append(x)` | Add one element to the end | `lst.append(5)` |
| `.extend(iterable)` | Add all elements from iterable | `lst.extend([6, 7])` |
| `.insert(i, x)` | Insert `x` before position `i` | `lst.insert(0, "first")` |
| `.remove(x)` | Remove first occurrence of `x` | `lst.remove("a")` |
| `.pop(i=-1)` | Remove and return element at index | `lst.pop()` / `lst.pop(0)` |
| `.index(x)` | Position of first `x` | `lst.index("b")` |
| `.count(x)` | How many times `x` appears | `lst.count(3)` |
| `.sort(key=, reverse=)` | Sort in place | `lst.sort(key=str.lower)` |
| `.reverse()` | Reverse in place | `lst.reverse()` |
| `.copy()` | Shallow copy | `copy = lst.copy()` |
| `.clear()` | Remove all elements | `lst.clear()` |

#### `dict` methods

| Method | Description | Example |
|---|---|---|
| `.get(key, default)` | Safe lookup, no `KeyError` | `d.get("x", 0)` |
| `.keys()` / `.values()` / `.items()` | Views for iteration | `for k, v in d.items():` |
| `.update(other)` | Merge another dict in place | `d.update({"c": 3})` |
| `.pop(key, default)` | Remove and return value | `d.pop("x", None)` |
| `.setdefault(key, default)` | Insert default only if key missing | `d.setdefault("count", 0)` |
| `.copy()` | Shallow copy | `d.copy()` |

#### `set` methods

| Method | Description | Example |
|---|---|---|
| `.add(x)` | Add element | `s.add(7)` |
| `.discard(x)` | Remove if present; no error if absent | `s.discard(99)` |
| `.remove(x)` | Remove; raises `KeyError` if absent | `s.remove(3)` |
| `.union(other)` / `\|` | All elements from both | `s \| t` |
| `.intersection(other)` / `&` | Elements in both | `s & t` |
| `.difference(other)` / `-` | Elements in `s` not in `t` | `s - t` |
| `.issubset(other)` | True if all elements of `s` in `t` | `s <= t` |
| `.issuperset(other)` | True if `s` contains all of `t` | `s >= t` |

### Standard Library Extensions

```python
from collections import deque, defaultdict, Counter, namedtuple
import heapq

# deque — O(1) append and pop from both ends
q = deque([1, 2, 3])
q.appendleft(0)    # [0, 1, 2, 3]
q.popleft()        # 0

# defaultdict — no KeyError on missing keys
word_counts = defaultdict(int)
for word in "the cat sat on the mat".split():
    word_counts[word] += 1

# Counter — counting shortcut
c = Counter("mississippi")
print(c.most_common(3))   # [('s', 4), ('i', 4), ('p', 2)]

# namedtuple — lightweight immutable record
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
print(p.x, p.y)

# heapq — min-heap
items = [(3, "normal"), (1, "urgent"), (2, "soon")]
heapq.heapify(items)
print(heapq.heappop(items))   # (1, 'urgent')
```

### Time Complexity Reference

| Operation | `list` | `dict` | `set` | `deque` |
|---|---|---|---|---|
| Access by index | O(1) | N/A | N/A | O(n) |
| Lookup by key/value | O(n) | O(1) avg | O(1) avg | O(n) |
| Append to end | O(1) amortized | — | — | O(1) |
| Insert at front | O(n) | — | — | O(1) |
| Delete by value | O(n) | O(1) avg | O(1) avg | O(n) |
| Membership test | O(n) | O(1) avg | O(1) avg | O(n) |
| Sort | O(n log n) | N/A | N/A | N/A |

**Key insight:** use a `set` or `dict` whenever you find yourself checking membership repeatedly in a `list`. Converting once is O(n); each lookup then becomes O(1).

### Comprehension Patterns

```python
# List comprehension — transform and filter in one line
evens_squared = [x**2 for x in range(20) if x % 2 == 0]

# Dict comprehension — invert a mapping
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

# Set comprehension — unique lowercase words
text = "The Cat sat on the Mat"
unique_words = {w.lower() for w in text.split()}

# Generator expression — lazy; does not build a list
total = sum(x**2 for x in range(1_000_000))
```

### Sorting Patterns

```python
students = [("Ana", 92), ("Sam", 85), ("Lee", 98)]

# Sort by score descending
by_score = sorted(students, key=lambda pair: pair[1], reverse=True)

# Sort by multiple fields
records = [{"name": "Ben", "age": 30}, {"name": "Ava", "age": 25}]
by_age_then_name = sorted(records, key=lambda r: (r["age"], r["name"]))

# Sort in place
students.sort(key=lambda pair: pair[0])   # alphabetical
```

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Create list/dict/set/tuple literals, access elements, use basic methods |
| **Developing** | Choose the right structure for a task, use comprehensions, sort with a key |
| **Proficient** | Use `defaultdict`, `Counter`, `deque`, `heapq`; reason about time complexity |
| **Advanced** | Design structures that match access patterns, benchmark alternatives, use `namedtuple` and `dataclass` appropriately |

### Suggested Practice Projects

1. **Word frequency** — Count word occurrences in a block of text using `Counter`, then display the 5 most common.
2. **Deduplication** — Remove duplicates from a list while preserving order (hint: `dict.fromkeys`).
3. **Inverted index** — Build a `defaultdict(list)` mapping each word to the list of sentence indices it appears in.
4. **Priority task queue** — Use `heapq` to process tasks in priority order from a list of `(priority, task_name)` tuples.
5. **Benchmark** — Measure membership-check time for a `list` vs a `set` at 10k, 100k, and 1M elements.

### Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Mutable default argument | `def fn(lst=[]):` shares one list across all calls | Use `def fn(lst=None): lst = lst or []` |
| Shallow copy of nested structures | `lst.copy()` copies the outer list but shares inner lists | Use `copy.deepcopy(lst)` for nested data |
| `dict` key must be hashable | Lists and dicts cannot be dict keys | Use tuples instead of lists as keys |
| `list.sort` vs `sorted` | `.sort()` returns `None` and modifies in place | Use `sorted()` when you need a new list |
| `set` has no order | You cannot rely on iteration order from a `set` | Use `sorted(s)` when order matters |
| `pop(0)` on a `list` | Removing from the front is O(n) | Use `collections.deque` for FIFO queues |

