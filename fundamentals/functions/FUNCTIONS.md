# Functions in Python

Functions are the primary building blocks of Python programs. They allow you to bundle code into reusable, modular units that perform specific tasks.

## Function Core Concepts

| Concept | Keyword / Syntax | Description |
|---|---|---|
| Definition | `def name():` | Starts a function definition |
| Return Value | `return value` | Exits the function and passes a value back to the caller |
| Documentation | `"""Docstring"""` | Triple-quoted string explaining the function's purpose |
| Type Hints | `(arg: type) -> type` | Optional annotations for argument and return types |
| Positional Args | `fn(a, b)` | Arguments mapped to parameters by position |
| Keyword Args | `fn(a=1, b=2)` | Arguments mapped to parameters by name |
| Default Params | `def fn(a=0):` | Parameters that use a default value if not provided |
| Variadic Args | `*args` | Captures extra positional arguments into a tuple |
| Variadic Kwargs | `**kwargs` | Captures extra keyword arguments into a dictionary |
| Lambda | `lambda x: x * 2` | Small, anonymous, one-line functions |

### Function Scope and Behavior

| Behavior | Description |
|---|---|
| First-Class | Functions are objects; they can be passed as arguments or returned |
| Local Scope | Variables defined inside a function are not visible outside |
| Global Access | Functions can read global variables, but need `global` to modify them |
| Closure | Inner functions can "remember" variables from their outer scope |
| Decorators | Functions that wrap other functions to modify their behavior |

---

## Defining and Calling Functions

```python
def greet(name: str, greeting: str = "Hello") -> str:
    """Returns a personalized greeting."""
    return f"{greeting}, {name}!"

# Call with positional arguments
print(greet("Alice"))  # Output: Hello, Alice!

# Call with keyword arguments
print(greet(name="Bob", greeting="Hi"))  # Output: Hi, Bob!
```

## Working with `*args` and `**kwargs`

Use `*args` for an unknown number of positional arguments and `**kwargs` for named ones.

```python
def make_sandwich(bread, *fillings, **toppings):
    print(f"Making a sandwich on {bread} bread.")
    print(f"Fillings: {', '.join(fillings)}")
    for key, value in toppings.items():
        print(f"Extra {key}: {value}")

make_sandwich("Sourdough", "Turkey", "Swiss", mayo=True, lettuce="shredded")
```

## Anonymous (Lambda) Functions

Lambdas are useful for quick, throwaway logic, often used with functions like `map`, `filter`, or `sorted`.

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# Sort by the second element (the word)
pairs.sort(key=lambda pair: pair[1])
print(pairs)
```

## Best Practices

- **Keep it Focused:** A function should do exactly one thing.
- **Naming:** Use `snake_case` for function names.
- **Avoid Side Effects:** Prefer returning values over modifying global state or mutable input arguments.
- **Document:** Use docstrings for all non-trivial functions.
- **Type Hints:** Use them to improve readability and catch bugs early.

---

## Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Define simple functions, use parameters, and `return` values. |
| **Developing** | Use default parameters, type hints, and understand local vs global scope. |
| **Proficient** | Effectively use `*args`, `**kwargs`, and write meaningful docstrings. |
| **Advanced** | Use closures, decorators, and write high-order functions. |

## Suggested Practice Projects

1. **Calculator:** Create a set of functions for basic math operations and a main function to orchestrate them.
2. **Data Formatter:** Write a function that takes a list of dictionaries and prints them as a formatted table.
3. **Password Validator:** A function that checks if a string meets various complexity criteria (length, digits, etc.).
4. **Decorator Logger:** Create a decorator that prints "Calling function X with args Y" every time the wrapped function is executed.

## Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Mutable Defaults | `def fn(a=[])` shares the same list across all calls | Use `a=None` and `if a is None: a = []` |
| Shadowing | Naming a local variable the same as a built-in (e.g., `list = []`) | Use descriptive names like `item_list` |
| Missing `return` | Functions return `None` by default if no `return` is reached | Ensure all logical paths return the expected type |
| Unpacking Errors | Passing the wrong number of arguments to a function | Use `*args` or keyword arguments for flexibility |
