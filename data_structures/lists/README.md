Summary 
Lists

    Ordered, mutable, allows duplicates.
    Use .append(), .remove(), .sort(), .pop(), etc.
    Iterate with for loops.


| Method            | Description                                    | Example                   |
|------------------|--------------------------------|---------------------------|
| `append(x)`      | Adds an element to the end of the list | `numbers.append(6)` |
| `extend(iterable)` | Extends list by adding multiple elements | `numbers.extend([7, 8, 9])` |
| `insert(index, x)` | Inserts an element at a specific index | `numbers.insert(2, 99)` |
| `remove(x)`      | Removes the first occurrence of `x` | `numbers.remove(3)` |
| `pop(index)`      | Removes and returns an item at `index` | `last = numbers.pop()` |
| `index(x)`       | Returns the index of `x` | `idx = numbers.index(4)` |
| `count(x)`       | Counts occurrences of `x` | `cnt = numbers.count(2)` |
| `sort()`         | Sorts the list (in-place) | `numbers.sort()` |
| `reverse()`      | Reverses the list (in-place) | `numbers.reverse()` |
| `copy()`         | Returns a shallow copy of the list | `new_list = numbers.copy()` |
| `clear()`        | Removes all elements from the list | `numbers.clear()` |










