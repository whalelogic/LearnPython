# Control Flow in Python

Control flow determines the order in which code is executed. In Python, this is managed through conditional statements, loops, and branching logic.

## Control Flow Keywords and Functions

| Keyword / Function | Category | Description |
|---|---|---|
| `if` | Conditional | Executes a block if the condition is `True` |
| `elif` | Conditional | "Else if" - checks another condition if previous ones were `False` |
| `else` | Branching | Executes if no preceding conditional was `True` |
| `for` | Loop | Iterates over a sequence (list, range, string, etc.) |
| `while` | Loop | Repeats a block as long as a condition remains `True` |
| `break` | Loop Control | Exits the innermost loop immediately |
| `continue` | Loop Control | Skips the rest of the current loop iteration |
| `pass` | Placeholder | A "do nothing" statement used as a syntactical placeholder |
| `match` | Pattern Matching | Structural pattern matching (Python 3.10+) |
| `case` | Pattern Matching | Specific pattern to match against in a `match` block |
| `range(stop)` | Iteration | Generates a sequence of numbers |
| `enumerate(iter)` | Iteration | Returns index and value pairs from an iterable |
| `zip(*iters)` | Iteration | Aggregates elements from multiple iterables |

---

## Conditionals

Python uses `if`, `elif`, and `else` for decision making. Indentation is mandatory to define the scope of each block.

```python
age = 20

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

### Truthiness
In Python, the following values are considered `False`:
- `None`, `False`
- Zero of any numeric type: `0`, `0.0`, `0j`
- Empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`

## Loops

### For Loops
`for` loops are used for iterating over a sequence.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Using range
for i in range(5):
    print(f"Iteration {i}")
```

### While Loops
`while` loops execute as long as the condition is `True`.

```python
count = 5
while count > 0:
    print(count)
    count -= 1
```

## Loop Control Statements

- **`break`**: Stop the loop entirely.
- **`continue`**: Skip to the next iteration.
- **`else`**: Executes after the loop finishes normally (i.e., NOT via `break`).

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        # Loop fell through without finding a factor
        print(f"{n} is a prime number")
```

## Structural Pattern Matching (Python 3.10+)

The `match` statement compares an expression against multiple patterns.

```python
status = 404

match status:
    case 200:
        print("OK")
    case 400 | 404:
        print("Not Found / Bad Request")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")
```

---

## Best Practices

- **Avoid Deep Nesting:** Use "guard clauses" and `return` or `continue` to keep code flat.
- **Prefer `for` over `while`:** Use `for` loops when iterating over known sequences; they are generally safer and more readable.
- **Use `enumerate`:** Instead of `range(len(list))`, use `enumerate(list)` to get both index and value.
- **Conditional Expressions:** For simple assignments, use ternary syntax: `value = "High" if x > 10 else "Low"`.

---

## Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Use `if/else` and basic `for` and `while` loops. |
| **Developing** | Use `elif`, `range()`, and basic `break`/`continue` logic. |
| **Proficient** | Use `enumerate`, `zip`, and understand `for-else` behavior. |
| **Advanced** | Use complex `match-case` patterns and the Walrus operator in conditionals. |

## Suggested Practice Projects

1. **FizzBuzz:** Print numbers 1-100, replacing multiples of 3 with "Fizz", 5 with "Buzz", and both with "FizzBuzz".
2. **Guess the Number:** A `while` loop game where the user tries to guess a random number with "higher/lower" hints.
3. **Menu System:** Use a `match-case` block to handle user input for a simple CLI tool.
4. **Prime Finder:** Use nested loops and `break/else` to find all prime numbers up to a limit.

## Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Infinite `while` | Forgetting to update the loop variable | Ensure the condition eventually becomes `False` |
| Off-by-one Error | `range(5)` goes from 0 to 4, not 5 | Remember `range` is stop-exclusive |
| `if x = 5` | Using assignment `=` instead of comparison `==` | Use `==` for checks (though Python usually catches this as a SyntaxError) |
| `for-else` confusion | Thinking `else` runs only if the loop *never* runs | `else` runs if the loop *finishes* (no `break`) |
