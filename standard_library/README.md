# Python Standard Library

This directory contains documentation and examples from Python's standard library.

## Contents

### 📄 Built_In_Functions.md
Comprehensive reference of Python's built-in functions - functions that are always available without importing.

## Python Built-in Functions Overview

Python provides 69+ built-in functions that are available without any imports. These are the fundamental building blocks of Python programming.

## Common Categories

### Type Conversion
```python
int()      # Convert to integer
float()    # Convert to float
str()      # Convert to string
bool()     # Convert to boolean
list()     # Convert to list
tuple()    # Convert to tuple
dict()     # Convert to dictionary
set()      # Convert to set
```

### Input/Output
```python
print()    # Print to console
input()    # Get user input
open()     # Open a file
```

### Math Functions
```python
abs()      # Absolute value
round()    # Round a number
pow()      # Power (x^y)
sum()      # Sum of iterable
min()      # Minimum value
max()      # Maximum value
divmod()   # Quotient and remainder
```

### Iteration
```python
range()       # Generate sequence of numbers
enumerate()   # Get index and value
zip()         # Combine iterables
map()         # Apply function to iterable
filter()      # Filter iterable
sorted()      # Return sorted list
reversed()    # Reverse iterator
```

### Object Inspection
```python
type()        # Get type of object
isinstance()  # Check if instance of class
issubclass()  # Check if subclass
id()          # Get memory address
dir()         # List attributes/methods
help()        # Get help documentation
vars()        # Get __dict__ attribute
```

### Iterable Functions
```python
len()         # Length of object
all()         # True if all elements true
any()         # True if any element true
iter()        # Get iterator
next()        # Get next item from iterator
```

## Quick Examples

### Working with Numbers
```python
# Absolute value
print(abs(-5))           # 5

# Power
print(pow(2, 3))         # 8

# Round
print(round(3.14159, 2)) # 3.14

# Min/Max
numbers = [1, 5, 3, 9, 2]
print(min(numbers))      # 1
print(max(numbers))      # 9
print(sum(numbers))      # 20
```

### Type Conversion
```python
# String to number
age = int("25")
price = float("19.99")

# Number to string
text = str(42)

# List to set (remove duplicates)
unique = set([1, 2, 2, 3, 3, 3])
print(unique)  # {1, 2, 3}
```

### Iteration
```python
# Range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

### Object Inspection
```python
# Type checking
x = 42
print(type(x))              # <class 'int'>
print(isinstance(x, int))   # True

# List methods
my_list = [1, 2, 3]
print(dir(my_list))         # Lists all methods

# Help
help(len)  # Shows documentation
```

### Boolean Functions
```python
# All
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False

# Any
print(any([False, False, True])) # True
print(any([False, False]))       # False
```

## Commonly Used Built-in Functions

### Essential Functions
1. `print()` - Output to console
2. `len()` - Get length
3. `range()` - Generate sequences
4. `type()` - Check type
5. `input()` - Get user input
6. `int()`, `float()`, `str()` - Type conversion
7. `sum()`, `min()`, `max()` - Math operations
8. `sorted()` - Sort sequences
9. `enumerate()` - Index + value iteration
10. `zip()` - Combine iterables

### Advanced Functions
1. `map()` - Transform iterables
2. `filter()` - Filter iterables
3. `lambda` - Anonymous functions
4. `iter()`, `next()` - Manual iteration
5. `all()`, `any()` - Boolean checks
6. `getattr()`, `setattr()` - Dynamic attributes
7. `isinstance()`, `issubclass()` - Type checking
8. `eval()`, `exec()` - Dynamic code execution (use carefully!)
9. `compile()` - Compile source code
10. `property()` - Create properties

## Standard Library Modules

While built-in functions don't require imports, Python's standard library contains many useful modules:

```python
# Common imports
import os          # Operating system interface
import sys         # System-specific parameters
import math        # Mathematical functions
import random      # Random number generation
import datetime    # Date and time
import json        # JSON encoding/decoding
import re          # Regular expressions
import pathlib     # Object-oriented filesystem paths
import collections # Specialized container datatypes
import itertools   # Iterator functions
```

## Best Practices

1. **Know your built-ins** - They're optimized and always available
2. **Use appropriate functions** - Don't reinvent the wheel
3. **Prefer built-ins over custom code** - They're usually faster
4. **Read the documentation** - Use `help()` function
5. **Use type conversion carefully** - Handle potential errors

```python
# Good - handle conversion errors
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid number")

# Good - use built-in functions
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)          # Better than manual loop
maximum = max(numbers)        # Better than manual comparison
```

## Resources

For detailed information on each built-in function, see:
- **Built_In_Functions.md** - Complete reference in this directory
- [Python Built-in Functions Documentation](https://docs.python.org/3/library/functions.html)
- [Python Standard Library Documentation](https://docs.python.org/3/library/)

## Learning Path

1. **Master the basics**: `print()`, `len()`, `type()`, `range()`
2. **Learn iteration**: `enumerate()`, `zip()`, `map()`, `filter()`
3. **Understand type conversion**: `int()`, `str()`, `list()`, etc.
4. **Explore inspection**: `dir()`, `help()`, `isinstance()`
5. **Study advanced**: `getattr()`, `eval()`, `compile()`

## Quick Reference

```python
# Most used built-in functions
print("Hello")                    # Output
len([1, 2, 3])                   # Length: 3
type(42)                         # Type: int
range(5)                         # Sequence: 0-4
int("42")                        # Convert: 42
sum([1, 2, 3])                   # Sum: 6
max([1, 5, 3])                   # Max: 5
sorted([3, 1, 2])                # Sort: [1, 2, 3]
enumerate(['a', 'b'])            # Index + value
zip([1, 2], ['a', 'b'])         # Combine iterables
```

---

**Remember**: Built-in functions are your friends! They're fast, reliable, and always available.
