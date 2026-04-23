# Python Classes & Objects Rules

## Class & Object Basics

| Concept                | Description |
|------------------------|-------------|
| **Class**             | A blueprint for creating objects (defines attributes & methods). |
| **Object**            | An instance of a class with its own unique data. |
| **Instance Variable** | A variable specific to an object (`self.attribute`). |
| **Class Variable**    | A shared variable across all instances (`cls.variable`). |
| **Method**           | A function defined in a class that operates on instances. |
| **Constructor (`__init__`)** | Initializes object attributes when an instance is created. |


## OOP Principles

| Principle       | Explanation |
|----------------|-------------|
| **Encapsulation** | Hiding data inside classes using private variables (`_variable`). |
| **Inheritance**  | A class can inherit attributes/methods from another class (`class Child(Parent)`). |
| **Polymorphism** | Methods can have different implementations in different classes. |
| **Abstraction**  | Hiding implementation details and exposing only necessary parts. |

## On using self or cls (instance vs class)

| Feature            | `self` | `cls` |
|-------------------|--------|--------|
| Refers to        | The specific instance | The class itself |
| Used in         | Instance methods | Class methods |
| Access instance variables? | ✅ Yes | ❌ No |
| Access class variables? | ✅ Yes | ✅ Yes |

## `@classmethod` vs `@staticmethod`

| Feature            | `@classmethod` | `@staticmethod` |
|-------------------|----------------|----------------|
| First parameter  | `cls` (class itself) | No `self` or `cls` |
| Access class variables? | ✅ Yes (can modify `cls.var`) | ❌ No (doesn’t access class state) |
| Modify instance attributes? | ❌ No | ❌ No |
| Use case | Factory methods, tracking instances | Utility functions unrelated to class state |

## Accessing Attributes Inside vs. Outside the Class

| Context            | Syntax |
|-------------------|--------|
| Inside the class  | `self.attribute` |
| Outside the class | `object.attribute` |

## Special Methods (Magic Methods)

| Method | Purpose |
|--------|---------|
| `__init__` | Constructor (initializes instance variables). |
| `__str__` | Returns a user-friendly string representation. |
| `__repr__` | Returns an official string representation. |
| `__len__` | Defines behavior for `len(obj)`. |
| `__call__` | Makes an instance callable like a function. |



