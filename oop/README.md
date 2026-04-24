# Object-Oriented Programming (OOP) in Python

This directory contains resources and examples for learning Object-Oriented Programming concepts in Python.

## Contents

### 📄 Classes_OOP.md
Comprehensive reference guide for Python classes and OOP principles.

**Topics covered:**
- Class and object basics
- Instance vs. class variables
- Methods (instance, class, static)
- OOP principles (Encapsulation, Inheritance, Polymorphism, Abstraction)
- Special/magic methods
- `@classmethod` vs `@staticmethod`

### 📁 pets/
Practical example demonstrating OOP concepts with a pet management system.

**Files:**
- `main.py` - Main program demonstrating class usage
- `pet.py` - Pet class definition and implementation

## Quick Reference

### Creating a Class

```python
class Dog:
    # Class variable
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # String representation
    def __str__(self):
        return f"{self.name} is {self.age} years old"

# Creating an instance
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Buddy says Woof!
print(my_dog)         # Buddy is 3 years old
```

### Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"
```

## Key OOP Principles

| Principle | Description |
|-----------|-------------|
| **Encapsulation** | Bundle data and methods that work on that data within a class |
| **Inheritance** | Create new classes based on existing classes |
| **Polymorphism** | Different classes can be used through the same interface |
| **Abstraction** | Hide complex implementation details, show only necessary features |

## Method Types

```python
class MyClass:
    # Instance method (uses self)
    def instance_method(self):
        return f"Instance: {self}"
    
    # Class method (uses cls)
    @classmethod
    def class_method(cls):
        return f"Class: {cls}"
    
    # Static method (no self or cls)
    @staticmethod
    def static_method():
        return "Static method"
```

## Special Methods (Magic Methods)

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"Book: {self.title}"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        return self.title == other.title

book = Book("Python Basics", 300)
print(book)        # Book: Python Basics
print(len(book))   # 300
```

## Examples in This Directory

### Pets Example
Navigate to the `pets/` directory to see a complete OOP example:

```bash
cd pets/
python main.py
```

This example demonstrates:
- Class definition and instantiation
- Instance methods and attributes
- Object interaction
- Real-world OOP application

## Learning Path

1. **Start with** `Classes_OOP.md` for theory and concepts
2. **Study** the `pets/` example for practical implementation
3. **Practice** by creating your own classes
4. **Experiment** with inheritance and polymorphism

## Best Practices

- Use clear, descriptive class names (PascalCase)
- Keep classes focused on a single responsibility
- Use `self` for instance variables and methods
- Implement `__str__` and `__repr__` for better debugging
- Prefer composition over deep inheritance hierarchies
- Use properties for controlled attribute access

## Additional Resources

- [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Real Python OOP Guide](https://realpython.com/python3-object-oriented-programming/)
- Main repository: [LearnPython](../)

---

**Practice**: Try modifying the pets example or creating your own class hierarchy!
