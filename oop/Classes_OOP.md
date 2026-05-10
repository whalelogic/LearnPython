# Python Classes and Objects

## Core Concepts

| Concept | Meaning |
|---|---|
| Class | A blueprint describing data and behavior |
| Object | A specific instance created from a class |
| Instance attribute | Data stored on one object, like `self.name` |
| Class attribute | Data shared by every instance |
| Method | A function defined inside the class |

## Building a Simple Class

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof"

buddy = Dog("Buddy", 3)
print(buddy.bark())
print(buddy.species)
```

## `self` vs `cls`

- `self` refers to one object.
- `cls` refers to the class itself.
- Use `@classmethod` when you need an alternate constructor or class-wide behavior.
- Use `@staticmethod` for helper logic that belongs near the class but does not need object or class state.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls((fahrenheit - 32) * 5 / 9)

    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0
```

## Inheritance Example

```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    def speak(self):
        return "meow"
```

Inheritance is helpful when subclasses truly share behavior. If two objects only share a few helper functions, composition is often easier to maintain.

## Special Methods You Will See Often

| Method | Why it matters |
|---|---|
| `__init__` | Set up a new object |
| `__str__` | Human-friendly string output |
| `__repr__` | Debug representation |
| `__len__` | Support `len(obj)` |
| `__eq__` | Define equality rules |

## A Real-World Mental Model

Think of a class as a template for related records plus the operations they support. A `Cart` object can track items and total cost; a `Book` object can track title and author while also knowing how to display itself.

## Related Reading

- [README.md](README.md)
- [pets/](pets)

---

## Deep Reference

### Special Methods (Dunder) Reference

Python calls these automatically. Implementing them makes your objects feel like built-in types.

| Method | Triggered by | Use case |
|---|---|---|
| `__init__(self, ...)` | `MyClass(...)` | Initialize instance state |
| `__repr__(self)` | `repr(obj)`, REPL display | Unambiguous developer view |
| `__str__(self)` | `str(obj)`, `print(obj)` | Human-friendly output |
| `__len__(self)` | `len(obj)` | Return logical size |
| `__getitem__(self, key)` | `obj[key]` | Index / slice support |
| `__setitem__(self, key, val)` | `obj[key] = val` | Index assignment |
| `__contains__(self, item)` | `item in obj` | Membership test |
| `__iter__(self)` | `for x in obj:` | Return an iterator |
| `__next__(self)` | `next(obj)` | Advance iterator |
| `__eq__(self, other)` | `obj == other` | Equality check |
| `__lt__(self, other)` | `obj < other` | Less-than (enables sorting) |
| `__hash__(self)` | `hash(obj)`, dict key | Required when `__eq__` defined |
| `__bool__(self)` | `if obj:` | Truthiness |
| `__enter__(self)` | `with obj as x:` | Context manager entry |
| `__exit__(self, exc_type, ...)` | End of `with` block | Context manager cleanup |
| `__call__(self, ...)` | `obj(...)` | Make instances callable |
| `__del__(self)` | Garbage collection | Resource cleanup (use carefully) |

### `property`, `classmethod`, and `staticmethod`

```python
class Circle:
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError(f"Radius must be positive, got {radius}")
        self._radius = radius

    # property — computed attribute with validation on set
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"Radius must be positive, got {value}")
        self._radius = value

    @property
    def area(self) -> float:
        import math
        return math.pi * self._radius ** 2

    # classmethod — alternate constructor
    @classmethod
    def unit(cls) -> "Circle":
        return cls(1.0)

    # staticmethod — utility that belongs near the class but needs no state
    @staticmethod
    def is_valid_radius(value: float) -> bool:
        return value > 0
```

### Inheritance and Composition

**Inheritance** — use when the subclass *is a* specialised version of the parent.

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says woof"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says meow"

animals: list[Animal] = [Dog("Rex"), Cat("Luna")]
for a in animals:
    print(a.speak())   # polymorphism
```

**Composition** — use when the class *has a* relationship, not *is a*.

```python
class Engine:
    def start(self) -> str:
        return "engine started"

class Car:
    def __init__(self) -> None:
        self._engine = Engine()   # composed, not inherited

    def start(self) -> str:
        return self._engine.start()
```

### Abstract Base Classes

Use `abc.ABC` to enforce that subclasses implement required methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"area={self.area():.2f}, perimeter={self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.w, self.h = w, h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return 2 * (self.w + self.h)
```

Trying to instantiate `Shape()` directly raises `TypeError`.

### Dataclasses — Minimal Boilerplate Records

```python
from dataclasses import dataclass, field

@dataclass(order=True, frozen=False)
class Point:
    x: float
    y: float
    label: str = ""
    tags: list[str] = field(default_factory=list)

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3.0, 4.0, label="A")
print(p)                        # Point(x=3.0, y=4.0, label='A', tags=[])
print(p.distance_to_origin())   # 5.0
```

`@dataclass` auto-generates `__init__`, `__repr__`, and `__eq__`. Adding `frozen=True` makes the instance immutable (and hashable).

### `__slots__` — Memory Optimization

```python
class Coordinate:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

# Coordinate instances use ~30% less memory than normal classes
# and attribute access is faster; but __dict__ no longer exists
```

Use `__slots__` when you create millions of small objects.

### Context Managers

```python
class Timer:
    import time

    def __enter__(self):
        self._start = self.time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = self.time.perf_counter() - self._start
        return False   # do not suppress exceptions

with Timer() as t:
    result = sum(range(1_000_000))
print(f"elapsed: {t.elapsed:.4f}s")
```

Or use `contextlib.contextmanager` for a generator-based approach:

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(name: str):
    print(f"opening {name}")
    try:
        yield name
    finally:
        print(f"closing {name}")
```

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Define a class with `__init__`, create instances, add methods |
| **Developing** | Use `@property`, write `__repr__`/`__str__`, understand inheritance and `super()` |
| **Proficient** | Use `ABC`, `dataclass`, `__slots__`, and context managers correctly |
| **Advanced** | Design composable class hierarchies, implement full dunder protocols, reason about MRO |

### Suggested Practice Projects

1. **Stack class** — Implement `push`, `pop`, `peek`, `__len__`, `__bool__`, and `__repr__`.
2. **Money type** — Build a `Money(amount, currency)` class with `__add__`, `__eq__`, and `__str__`; raise `TypeError` on mismatched currencies.
3. **Plugin registry** — Use a class-level `dict` and `__init_subclass__` to auto-register subclasses.
4. **Chainable builder** — Build a query builder where each method returns `self` to allow chaining.
5. **Context manager** — Write a `TempDirectory` context manager that creates a temp dir on enter and deletes it on exit.

### Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Mutable class attribute | `class Foo: items = []` — all instances share one list | Use `self.items = []` in `__init__` |
| `__eq__` without `__hash__` | Defining `__eq__` makes the class unhashable by default | Also define `__hash__` or use `@dataclass(frozen=True)` |
| Forgetting `super().__init__()` | Skipping `super()` leaves the parent uninitialised | Always call `super().__init__(...)` in subclass `__init__` |
| `isinstance` vs type equality | `type(x) == Dog` fails for subclasses | Use `isinstance(x, Dog)` |
| `__del__` timing | Python does not guarantee when `__del__` runs | Use context managers instead of `__del__` for cleanup |
| Deep vs shallow copy | `copy.copy(obj)` only copies one level | Use `copy.deepcopy(obj)` for nested mutable state |

