# Python Fundamentals

This folder introduces the syntax and mental models that every other topic in the repository builds on.

## What You Will Learn

- How variables store values and how Python chooses types dynamically
- How functions package repeated logic into reusable blocks
- How conditionals and loops control the flow of a program
- How core Python references help you look up details without losing the big picture

## Folder Map

- [functions/FUNCTIONS.md](functions/FUNCTIONS.md) — creating and using your own functions
- [functions/functions_playground.py](functions/functions_playground.py) — interactive playground for function concepts
- [control_flow/CONTROL_FLOW.md](control_flow/CONTROL_FLOW.md) — conditionals, loops, and branching
- [control_flow/control_flow_playground.py](control_flow/control_flow_playground.py) — interactive playground for control flow
- [core/README.md](core/README.md) — deeper references for keywords, modules, data types, exceptions, and contexts

## Quick Examples

### Variables and Reassignment
```python
name = "Python learner"
score = 7
score += 1
print(name, score)
```

### Functions and Return Values
```python
def format_price(amount, currency="USD"):
    return f"{currency} {amount:.2f}"

print(format_price(19.5))
print(format_price(19.5, "EUR"))
```

### Control Flow
```python
numbers = [1, 2, 3, 4, 5]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)
```

## Why This Folder Matters

If Python feels magical, fundamentals is where that magic becomes predictable. Once you understand names, values, functions, loops, and exceptions, the rest of the repository feels much less intimidating.

## Good Next Steps

1. Read this folder first.
2. Use [data_structures](../data_structures/README.md) when you want better ways to store information.
3. Jump to [oop](../oop/README.md) once your functions start sharing state and behavior.
