# Python Data Structures

This directory contains information and examples about Python's built-in data structures.

## Contents

### 📄 Data_Structures.md
Comprehensive reference covering:
- Built-in data structures (Lists, Tuples, Sets, Dictionaries)
- Comparison tables
- Stack (LIFO) and Queue (FIFO)
- Priority Queue (Heap)
- Linked Lists
- Graphs and Trees

### 📁 lists/
Detailed examples and documentation for Python lists.

## Built-in Data Structures Overview

### Lists
Ordered, mutable sequences that allow duplicates.

```python
my_list = [1, 2, 3, "apple", True]
my_list.append(4)
my_list[0] = 10
print(my_list)  # [10, 2, 3, 'apple', True, 4]
```

### Tuples
Ordered, immutable sequences that allow duplicates.

```python
my_tuple = (1, 2, 3, "apple")
# my_tuple[0] = 10  # Error: tuples are immutable
print(my_tuple[1])  # 2
```

### Sets
Unordered collections of unique elements.

```python
my_set = {1, 2, 3, 3, 4}
print(my_set)  # {1, 2, 3, 4}
my_set.add(5)
my_set.remove(1)
```

### Dictionaries
Key-value pairs, ordered (Python 3.7+).

```python
my_dict = {"name": "Alice", "age": 30}
my_dict["city"] = "New York"
print(my_dict["name"])  # Alice
```

## Quick Comparison

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| Ordered | ✅ | ✅ | ❌ | ✅ (3.7+) |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ | Keys: ❌, Values: ✅ |
| Indexed | ✅ | ✅ | ❌ | By key |
| Syntax | `[]` | `()` | `{}` | `{k: v}` |

## Common Operations

### List Operations

```python
# Creating
fruits = ["apple", "banana", "cherry"]

# Adding
fruits.append("orange")        # Add to end
fruits.insert(1, "blueberry")  # Insert at index
fruits.extend(["grape", "kiwi"]) # Add multiple

# Removing
fruits.remove("banana")        # Remove by value
popped = fruits.pop()          # Remove and return last
del fruits[0]                  # Delete by index

# Accessing
first = fruits[0]
last = fruits[-1]
subset = fruits[1:3]           # Slicing

# Other operations
fruits.sort()                  # Sort in place
fruits.reverse()               # Reverse in place
length = len(fruits)           # Get length
```

### Dictionary Operations

```python
# Creating
person = {"name": "John", "age": 30}

# Accessing
name = person["name"]
age = person.get("age", 0)     # With default

# Modifying
person["city"] = "NYC"         # Add/update
person.update({"age": 31, "country": "USA"})

# Removing
del person["city"]
age = person.pop("age")        # Remove and return

# Iteration
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Useful methods
keys = person.keys()
values = person.values()
items = person.items()
```

### Set Operations

```python
# Creating
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Adding
set1.add(5)

# Removing
set1.remove(1)        # Raises error if not found
set1.discard(10)      # No error if not found

# Set operations
union = set1 | set2              # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2        # {3, 4}
difference = set1 - set2          # {1, 2}
symmetric_diff = set1 ^ set2      # {1, 2, 5, 6}

# Testing
is_subset = {1, 2}.issubset(set1)
is_superset = set1.issuperset({1, 2})
```

## Advanced Data Structures

### Stack (LIFO - Last In, First Out)

```python
# Using a list
stack = []
stack.append(1)    # Push
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop (returns 3)

# Using deque (more efficient)
from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
top = stack.pop()
```

### Queue (FIFO - First In, First Out)

```python
from collections import deque

queue = deque()
queue.append(1)      # Enqueue
queue.append(2)
queue.append(3)
first = queue.popleft()  # Dequeue (returns 1)
```

### Priority Queue (Heap)

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

smallest = heapq.heappop(heap)  # Returns 1
```

### Counter

```python
from collections import Counter

# Count elements
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(counter)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common
print(counter.most_common(2))  # [('apple', 3), ('banana', 2)]
```

### DefaultDict

```python
from collections import defaultdict

# Dictionary with default values
dd = defaultdict(int)  # Default value is 0
dd["count"] += 1       # No KeyError

dd_list = defaultdict(list)
dd_list["items"].append(1)  # Creates list automatically
```

## Time Complexity

### List

| Operation | Time Complexity |
|-----------|-----------------|
| Access by index | O(1) |
| Search | O(n) |
| Insert at end | O(1) |
| Insert at position | O(n) |
| Delete | O(n) |

### Dictionary

| Operation | Time Complexity |
|-----------|-----------------|
| Access | O(1) average |
| Insert | O(1) average |
| Delete | O(1) average |
| Search | O(1) average |

### Set

| Operation | Time Complexity |
|-----------|-----------------|
| Add | O(1) average |
| Remove | O(1) average |
| Contains | O(1) average |
| Union/Intersection | O(len(s1) + len(s2)) |

## Best Practices

1. **Choose the right data structure**
   - Need order and mutability? → List
   - Need uniqueness? → Set
   - Need key-value pairs? → Dictionary
   - Need immutability? → Tuple

2. **Use comprehensions** for concise code
   ```python
   squares = [x**2 for x in range(10)]
   even_squares = {x**2 for x in range(10) if x % 2 == 0}
   word_lengths = {word: len(word) for word in ["hi", "hello"]}
   ```

3. **Use appropriate methods**
   - `get()` for dictionaries with defaults
   - `in` operator for membership testing
   - `enumerate()` for index and value

4. **Consider memory and performance**
   - Tuples use less memory than lists
   - Sets are faster for membership tests
   - Deque is faster for queue operations

## Subdirectories

### lists/
Contains detailed information about list operations, methods, and best practices. See [lists/README.md](lists/README.md) for more details.

## Additional Resources

- [Python Data Structures Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [collections Module](https://docs.python.org/3/library/collections.html)
- [heapq Module](https://docs.python.org/3/library/heapq.html)
- Main repository: [LearnPython](../)

---

**Master these data structures** - they're fundamental to efficient Python programming!
