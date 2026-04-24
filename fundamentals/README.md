# Python Fundamentals

This directory contains fundamental Python concepts and examples.

## Contents

### 📁 Variables
Learn about Python variable declarations, naming conventions, and data types.

- **File**: `variables/variables.py`
- **Topics**: Variable assignment, naming rules, type inference

### 📁 Functions
Explore Python functions, including built-in functions and custom function definitions.

- **File**: `functions/Built_In_Functions.md`
- **Topics**: Built-in functions, function syntax, parameters, return values

### 📁 Control Flow
Understand conditional statements and loops in Python.

- **Topics**: `if`, `elif`, `else`, `for`, `while`, `break`, `continue`

## Getting Started

Each subdirectory contains specific examples and documentation. Navigate to the respective folder to explore:

```bash
cd variables/    # Variable examples
cd functions/    # Function references
cd control_flow/ # Control flow examples
```

## Core Concepts

### Variables
```python
# Variable assignment
name = "Python"
age = 30
is_active = True
```

### Functions
```python
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling a function
message = greet("World")
print(message)
```

### Control Flow
```python
# If statement
if age >= 18:
    print("Adult")
else:
    print("Minor")

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

## Learning Path

1. Start with **Variables** to understand data storage
2. Move to **Functions** to learn code organization
3. Study **Control Flow** to understand program logic

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- Main repository: [LearnPython](../)

---

**Note**: Practice each concept with examples from the respective directories!
