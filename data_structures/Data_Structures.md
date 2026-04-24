# Python Data Structures

## Built-in Data Structures

| Data Structure | Mutable? | Ordered? | Duplicates? | Common Methods |
|---------------|---------|---------|------------|----------------|
| **List (`list`)** | ✅ Yes | ✅ Yes | ✅ Yes | `.append()`, `.extend()`, `.pop()`, `.sort()`, `.reverse()` |
| **Tuple (`tuple`)** | ❌ No | ✅ Yes | ✅ Yes | `.count()`, `.index()` |
| **Set (`set`)** | ✅ Yes | ❌ No | ❌ No | `.add()`, `.remove()`, `.union()`, `.intersection()`, `.difference()` |
| **Dictionary (`dict`)** | ✅ Yes | ✅ Yes (Python 3.7+) | Keys ❌, Values ✅ | `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`, `.pop()` |

## List vs. Tuple vs. Set vs. Dictionary

| Feature        | List | Tuple | Set | Dictionary |
|---------------|------|-------|-----|------------|
| **Indexed?** | ✅ Yes | ✅ Yes | ❌ No | ✅ Keys |
| **Mutable?** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Duplicates Allowed?** | ✅ Yes | ✅ Yes | ❌ No | ✅ Values |
| **Iteration Speed** | Slower | Faster | Fast | Fast (Key Lookup) |
| **Use Case** | General-purpose, dynamic array | Immutable sequence | Unique unordered values | Key-value pairs |

## Stack (LIFO - Last In, First Out)

| Feature  | Description |
|----------|-------------|
| **Implementation** | Can be implemented using a `list` or `collections.deque` |
| **Operations** | `.append()` (push), `.pop()` (pop) |
| **Use Case** | Backtracking (e.g., Browser history, Undo/Redo) |

## Queue (FIFO - First In, First Out)

| Feature  | Description |
|----------|-------------|
| **Implementation** | `collections.deque` (recommended) or `queue.Queue` |
| **Operations** | `.append()` (enqueue), `.popleft()` (dequeue) |
| **Use Case** | Scheduling tasks, print queue |

## Priority Queue (Min/Max Heap)

| Feature  | Description |
|----------|-------------|
| **Implementation** | `heapq` module |
| **Operations** | `heapq.heappush()`, `heapq.heappop()` |
| **Use Case** | Dijkstra’s algorithm, Task scheduling |

## Linked List

| Feature  | Description |
|----------|-------------|
| **Implementation** | Custom class with `Node` objects |
| **Operations** | Insert, Delete, Traverse |
| **Use Case** | Dynamic memory allocation, Efficient insertions/deletions |

## Graphs

| Feature  | Description |
|----------|-------------|
| **Implementation** | Adjacency list (dict of lists) or adjacency matrix |
| **Operations** | Add edge, Remove edge, BFS, DFS |
| **Use Case** | Social networks, Navigation systems |

## Trees

| Feature  | Description |
|----------|-------------|
| **Types** | Binary Tree, Binary Search Tree (BST), AVL Tree, Trie |
| **Operations** | Insert, Delete, Search, Traverse (Inorder, Preorder, Postorder) |
| **Use Case** | Hierarchical data, Searching, Auto-complete |

---

This covers the **core data structures** in Python! 🚀 Let me know if you want more details. 😊
