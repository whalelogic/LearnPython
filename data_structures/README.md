# Python Data Structures

This folder covers the containers you use to store, search, group, and transform data in Python.

## Folder Map

- [Data_Structures.md](Data_Structures.md) — overview of built-ins and common abstract data structures
- [lists/README.md](lists/README.md) — focused list operations and patterns
- [dictionaries/README.md](dictionaries/README.md) — dictionary-specific context and reference links
- [algorithms/README.md](algorithms/README.md) — data-structure-heavy algorithm notes

## Choose the Right Structure

| Need | Good default |
|---|---|
| Ordered collection you will change often | `list` |
| Fixed record that should not change | `tuple` |
| Fast membership checks and unique items | `set` |
| Named lookups by key | `dict` |

## Quick Example

```python
inventory = {
    "apples": 10,
    "bananas": 4,
    "oranges": 8,
}

low_stock = [name for name, count in inventory.items() if count < 5]
print(low_stock)
```

## Related Context

Most Python programs use more than one data structure at once. A web response may come back as dictionaries inside lists, while a data-cleaning script may use sets to remove duplicates before saving rows to a file.
