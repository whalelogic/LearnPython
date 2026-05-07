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
