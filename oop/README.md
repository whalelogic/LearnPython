# Object-Oriented Programming (OOP) in Python

This folder explains how Python groups data and behavior into classes.

## In This Folder

- [Classes_OOP.md](Classes_OOP.md) — core class syntax, method types, and inheritance examples
- `pets/` — a small project that shows objects interacting in a realistic way

## Why OOP Helps

OOP becomes useful when several functions need to work on the same state. Instead of passing the same values through every function call, you create objects that keep related data and behavior together.

## Quick Example

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount("Riley", 100)
print(account.deposit(25))
```

## What to Practice

1. Create a class with attributes and instance methods.
2. Add `__str__` so objects print clearly.
3. Refactor repeated dictionary-based code into a class.
4. Try inheritance only after the basic object model feels natural.
