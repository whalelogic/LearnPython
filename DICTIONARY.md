# Dictionary Methods


| Method                 | Description                                      | Example                     |
|-----------------------|--------------------------------|---------------------------|
| `keys()`              | Returns a view object of keys | `person.keys()` |
| `values()`            | Returns a view object of values | `person.values()` |
| `items()`             | Returns key-value pairs | `person.items()` |
| `get(key, default)`   | Gets a value (returns `default` if key not found) | `person.get("name")` |
| `update(dict2)`       | Merges `dict2` into current dictionary | `person.update({"age": 26})` |
| `pop(key)`            | Removes and returns a key's value | `age = person.pop("age")` |
| `popitem()`           | Removes and returns the last inserted pair | `last = person.popitem()` |
| `setdefault(key, default)` | Gets a value, or sets it if missing | `person.setdefault("gender", "Female")` |
| `copy()`              | Returns a shallow copy of the dictionary | `new_dict = person.copy()` |
| `clear()`             | Removes all key-value pairs | `person.clear()` |
