# Python Data Structures and Algorithms Reference

This reference covers essential data structures and algorithms with Python-oriented mental models, complexity guidance, and implementation patterns.

## Mental Models First

1. **Data structure choice dominates performance** for most real programs.
2. **Big-O describes growth**, not exact runtime.
3. **Trade-offs are contextual**: readability, memory, mutation frequency, and access patterns all matter.

## Big-O Cheat Sheet

| Complexity | Informal meaning |
|---|---|
| `O(1)` | Constant time |
| `O(log n)` | Grows slowly (divide-and-conquer) |
| `O(n)` | Linear scan |
| `O(n log n)` | Efficient comparison sorts |
| `O(n^2)` | Nested loops over same data |
| `O(2^n)` | Exponential branching |

## Core Python Structures

| Structure | Lookup | Insert | Delete | Ordered? | Key use |
|---|---|---|---|---|---|
| `list` | O(1) index | O(1) append / O(n) middle | O(1) pop end / O(n) middle | Yes | Dynamic arrays |
| `tuple` | O(1) index | N/A (immutable) | N/A | Yes | Fixed records |
| `dict` | O(1) avg key | O(1) avg | O(1) avg | Insertion-ordered | Fast mapping |
| `set` | O(1) avg membership | O(1) avg | O(1) avg | Unordered | Dedup + membership |
| `deque` | O(1) ends | O(1) ends | O(1) ends | Yes | Queues/stacks |

## Lists and Dynamic Arrays

```python
arr = [10, 20, 30]
arr.append(40)      # amortized O(1)
arr.insert(1, 15)   # O(n)
arr.pop()           # O(1)
```

### When lists are ideal
- random index access
- append-heavy workloads
- small to medium collections where simplicity matters

## Stack (LIFO)

Use list or deque.

```python
stack = []
stack.append("A")
stack.append("B")
print(stack.pop())  # B
```

Typical use cases: undo systems, DFS, expression parsing.

## Queue (FIFO)

Prefer `collections.deque`.

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)         # enqueue
print(q.popleft())  # dequeue -> 1
```

Use cases: BFS, task scheduling, buffering.

## Priority Queue (Heap)

Python provides min-heap via `heapq`.

```python
import heapq

heap = []
heapq.heappush(heap, (2, "medium"))
heapq.heappush(heap, (1, "high"))
print(heapq.heappop(heap))  # (1, 'high')
```

Use cases: shortest-path algorithms, event scheduling, top-k queries.

## Hash-based Structures: `dict` and `set`

- Great for membership tests and indexing.
- Avoid mutable keys.
- Average O(1), but conceptually still dependent on hash quality.

```python
seen = set()
for n in [1, 2, 2, 3]:
    if n in seen:
        print("duplicate", n)
    seen.add(n)
```

## Linked Lists (Conceptual)

Python does not include a built-in linked list class for general use; `deque` is often better.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```

Linked lists are mainly educational in Python unless specific pointer semantics are needed.

## Trees

## Binary Tree Node

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

## Traversals

```python
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)
```

### Tree traversal summary

| Traversal | Visit order |
|---|---|
| Preorder | Root, Left, Right |
| Inorder | Left, Root, Right |
| Postorder | Left, Right, Root |
| Level-order | Breadth-first by level |

## Graph Representations

### Adjacency list (most common)

```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": [],
}
```

### Adjacency matrix
- Better for dense graphs.
- Simpler edge existence check by index, higher memory usage.

## BFS and DFS

### Breadth-First Search (BFS)

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)
    return order
```

### Depth-First Search (DFS)

```python
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []
    visited.add(start)
    order.append(start)
    for nbr in graph[start]:
        if nbr not in visited:
            dfs(graph, nbr, visited, order)
    return order
```

## Sorting Algorithms

## Python-native sorting

Use `sorted()` and `.sort()` first (Timsort, stable, highly optimized).

```python
items = [("A", 3), ("B", 1), ("C", 2)]
print(sorted(items, key=lambda x: x[1]))
```

## Canonical educational sorts

### Merge sort (O(n log n), stable)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
```

### Quick sort (average O(n log n), worst O(n^2))

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    low = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]
    return quick_sort(low) + mid + quick_sort(high)
```

## Searching Algorithms

### Linear search

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

### Binary search (requires sorted input)

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

## Two-pointer and Sliding Window Patterns

These are high-value interview and production techniques for array/string tasks.

### Two pointers example

```python
def has_pair_with_sum(nums, target):
    nums = sorted(nums)
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return True
        if s < target:
            i += 1
        else:
            j -= 1
    return False
```

### Sliding window example

```python
def max_sum_k(nums, k):
    if k > len(nums):
        return None
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        best = max(best, window)
    return best
```

## Dynamic Programming (DP) Mental Model

DP solves overlapping subproblems by storing intermediate results.

### Fibonacci with memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

### Bottom-up variant

```python
def fib_tab(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

## Recursion vs Iteration

| Approach | Pros | Cons |
|---|---|---|
| Recursion | Elegant for trees/divide-conquer | Stack depth limits |
| Iteration | Often faster and memory safer | Sometimes less expressive |

## Complexity-aware Design Decisions

| Requirement | Best default |
|---|---|
| Frequent membership checks | `set` |
| Keyed lookup by id/name | `dict` |
| FIFO processing | `deque` |
| Sorted retrieval repeatedly | maintain heap / sorted structure |
| One-time sort then many searches | sort once + binary search |

## Practical Checklist

- Choose data structure before coding algorithm details.
- Track both time and memory complexity.
- Validate edge cases (empty input, single item, duplicates).
- Prefer Python built-ins (`sorted`, `heapq`, `deque`, `dict`, `set`) over reinventing low-level structures.

## Common Pitfalls

| Pitfall | Example | Fix |
|---|---|---|
| Using list as queue with `pop(0)` | O(n) dequeue | Use `deque.popleft()` |
| Sorting repeatedly in loops | O(n log n) each iteration | Sort once if possible |
| Ignoring input constraints | TLE/memory issues | Match algorithm to data size |
| Premature micro-optimization | Complex unreadable code | Start with clear correct solution |

## Learning Progression

1. Master list/dict/set/deque and complexity.
2. Implement BFS, DFS, binary search, merge sort.
3. Practice two pointers and sliding window.
4. Learn heaps, recursion patterns, and DP memoization.
5. Apply these patterns to real project code, not only exercises.

Data structures and algorithms are not separate from Python—they are the reason Python code can be both expressive and performant when used thoughtfully.

## Extended Complexity Table by Pattern

| Pattern | Typical complexity | Notes |
|---|---|---|
| One pass scan | O(n) | Counting, filtering |
| Nested full scan | O(n^2) | Pair comparisons |
| Sort then linear pass | O(n log n) | Common optimization |
| Heap top-k | O(n log k) | Efficient when `k << n` |
| Hash lookup per item | O(n) avg | Great for duplicate detection |

## Top-K Example with Heap

```python
import heapq

def top_k(nums, k):
    return heapq.nlargest(k, nums)
```

## Prefix Sum Pattern

```python
def prefix_sums(nums):
    out = [0]
    for n in nums:
        out.append(out[-1] + n)
    return out

# Sum in range [l, r] => pref[r+1] - pref[l]
```

## Monotonic Stack Idea

Useful for next greater/smaller element problems.

```python
def next_greater(nums):
    res = [-1] * len(nums)
    stack = []
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            idx = stack.pop()
            res[idx] = n
        stack.append(i)
    return res
```

## Algorithm Selection Heuristics

- Need unique detection quickly → `set`.
- Need frequency counts → `dict` / `Counter`.
- Need shortest path with non-negative weights → Dijkstra + heap.
- Need hierarchical traversal → recursion or explicit stack/queue.
- Need repeated median/top values → heaps.

## Edge-case Checklist for Implementations

- Empty input
- One element
- Duplicate values
- Negative numbers / zero
- Already sorted / reverse sorted data
- Very large input (memory pressure)

Good algorithm practice is mostly good trade-off reasoning backed by clear complexity awareness.

## Graph Algorithm Mental Models

## Dijkstra (non-negative edge weights)

```python
import heapq

def dijkstra(graph, start):
    # graph: {node: [(neighbor, weight), ...]}
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cur_dist, node = heapq.heappop(heap)
        if cur_dist != dist[node]:
            continue
        for nbr, w in graph[node]:
            cand = cur_dist + w
            if cand < dist[nbr]:
                dist[nbr] = cand
                heapq.heappush(heap, (cand, nbr))
    return dist
```

## Topological sort (DAG)

```python
from collections import deque

def topo_sort(graph):
    indeg = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indeg[v] += 1

    q = deque([u for u, d in indeg.items() if d == 0])
    out = []

    while q:
        u = q.popleft()
        out.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(out) != len(graph):
        raise ValueError("Cycle detected")
    return out
```

## Union-Find (Disjoint Set)

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
```

## Data Structure Selection by Operation Mix

| Workload | Best fit |
|---|---|
| Frequent append + random reads | `list` |
| Frequent push/pop both ends | `deque` |
| Repeated key lookups | `dict` |
| Frequent uniqueness checks | `set` |
| Keep smallest/largest efficiently | `heapq` |

## Testing Algorithms Correctly

- test normal case,
- edge case (empty/single),
- duplicate-heavy case,
- randomized input,
- adversarial case for worst complexity.

## Practical Performance Advice

- Prefer built-ins and stdlib algorithms first.
- Measure with representative data before optimizing.
- Reduce algorithmic complexity before micro-optimizing loops.
- Keep correctness and readability unless performance constraints require trade-offs.

Algorithms become practical when paired with clear constraints, measured behavior, and thoughtful data-structure choices.
