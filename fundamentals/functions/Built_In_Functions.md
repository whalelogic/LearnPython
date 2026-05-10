# Python Built-in Functions

Built-in functions are available immediately—no import required. Learning a few of them well saves you from writing a lot of unnecessary code.

## Core Groups to Know Early

| Category | Functions | Why they matter |
|---|---|---|
| Output and debugging | `print()`, `repr()` | See values clearly while learning |
| Measuring and checking | `len()`, `type()`, `isinstance()` | Inspect data before using it |
| Iteration | `range()`, `enumerate()`, `zip()` | Loop over data with less manual bookkeeping |
| Conversion | `int()`, `float()`, `str()`, `list()`, `dict()` | Turn data into the shape you need |
| Aggregation | `sum()`, `min()`, `max()`, `sorted()` | Answer common questions in one call |

## Everyday Examples

### `len()` and `sum()`
```python
scores = [88, 91, 76, 95]
print(len(scores))
print(sum(scores) / len(scores))
```

### `enumerate()`
```python
tasks = ["read", "practice", "review"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
```

### `zip()`
```python
names = ["Ada", "Grace", "Linus"]
roles = ["math", "compiler", "kernel"]
for name, role in zip(names, roles):
    print(f"{name}: {role}")
```

### `sorted()` with a key
```python
students = [
    {"name": "Ava", "score": 91},
    {"name": "Ben", "score": 84},
    {"name": "Cara", "score": 95},
]

ranked = sorted(students, key=lambda student: student["score"], reverse=True)
print(ranked)
```

## A Small Real-World Pattern

```python
raw_prices = ["19.99", "5.50", "12.00"]
prices = [float(value) for value in raw_prices]
print(f"items={len(prices)} total={sum(prices):.2f}")
```

This combines conversion, measuring, and aggregation in a way you will use often in scripts and APIs.

## Common Mistakes to Avoid

- Forgetting that `map()` and `zip()` return iterators in Python 3
- Using `list.sort()` when you actually need a new sorted copy from `sorted()`
- Calling `int()` or `float()` without handling bad input
- Rewriting loops that `sum()`, `any()`, or `all()` already solve cleanly

## Related Reading

- [../README.md](../README.md)
- [../core/BUILT_IN_FUNCTIONS.md](../core/BUILT_IN_FUNCTIONS.md)
- [../../standard_library/Built_In_Functions.md](../../standard_library/Built_In_Functions.md)

---

## Extended Study Workbook

This extension turns the page into a longer reference you can repeatedly revisit while practicing.

### 1) Learning Goals

By the end of this topic, you should be able to:

- Explain the core vocabulary in plain language.
- Identify when this topic is a good fit for a real task.
- Recognize common beginner mistakes before they happen.
- Debug basic issues without guessing.
- Compose this topic with related Python tools and modules.

### 2) Mental Model

Use this short mental model while reading examples:

1. **Input** — What data or request enters the code?
2. **Transformation** — What operation changes the data?
3. **Output** — What value, file, response, or effect is produced?
4. **Failure modes** — What can go wrong?
5. **Validation** — How do you check correctness quickly?

If you cannot explain all five parts, pause and simplify the example.

### 3) Terminology Drill

Review these terms and define each in your own words:

- value
- expression
- statement
- iterable
- exception
- state
- side effect
- dependency
- serialization
- validation

A useful habit is to write one sentence per term plus one concrete example.

### 4) Practical Checklist

When implementing this topic in a project, verify:

- Inputs are validated early.
- Variable names are explicit.
- Error handling exists for expected failures.
- Edge cases are covered.
- Output format is predictable.
- The code is readable after one week away.
- The solution is tested with both normal and strange input.
- Logging/print statements are meaningful during debugging.
- Temporary experimentation code is removed before sharing.
- You documented assumptions.

### 5) Common Mistakes and Corrections

- **Mistake:** Copying code without understanding data flow.
  - **Fix:** Trace one sample input by hand.
- **Mistake:** Ignoring type/shape/format assumptions.
  - **Fix:** Print and assert assumptions early.
- **Mistake:** Overcomplicating the first version.
  - **Fix:** Build a tiny working baseline first.
- **Mistake:** Mixing setup and business logic.
  - **Fix:** Separate configuration from core operations.
- **Mistake:** Not handling empty input.
  - **Fix:** Add a guard path and test it.

### 6) Debugging Workflow

Follow this process when something breaks:

1. Reproduce the issue with the smallest possible input.
2. Confirm what output you expected.
3. Add narrow debug prints or assertions.
4. Check boundary values and optional fields.
5. Verify external dependencies and environment assumptions.
6. Fix one thing at a time.
7. Re-run the exact failing scenario.
8. Keep a short note about root cause.

### 7) Mini Exercises

Try these short tasks:

1. Rewrite one example using clearer variable names.
2. Add one intentional edge case and handle it gracefully.
3. Add a small validation function for input checks.
4. Convert one example into a reusable function.
5. Produce a tiny test table with three normal cases and three edge cases.
6. Explain one example to a beginner in five sentences.
7. Refactor duplicated lines into a helper.
8. Add a failure path with a clear error message.
9. Measure behavior with larger input and note observations.
10. Compare two approaches and justify your final choice.

### 8) Integration Notes

This topic is strongest when combined with:

- Built-in functions for concise transformations.
- Standard library modules for file handling, paths, parsing, and collections.
- Data structures that match access patterns.
- Clear naming and small functions from core Python fundamentals.
- Lightweight tests to protect behavior while refactoring.

### 9) Review Questions

Use these to self-check understanding:

1. What problem does this topic solve best?
2. Which assumptions does your code make?
3. What happens with empty or missing values?
4. How does your solution fail, and is that failure readable?
5. Can you explain each line to a teammate?
6. Which part should be extracted into a helper?
7. What would you monitor in production?
8. What part of this is easiest to misuse?
9. Where can performance degrade?
10. What would you document for future maintainers?

### 10) Progress Rubric

- **Beginner:** Can run and slightly modify examples.
- **Developing:** Can implement this topic for a small script from scratch.
- **Proficient:** Can handle edge cases and debug confidently.
- **Advanced:** Can design abstractions and teach the topic clearly.

### 11) Suggested Practice Routine

- Day 1: Read and run all examples.
- Day 2: Rebuild key examples from memory.
- Day 3: Add validation and error handling.
- Day 4: Refactor for readability.
- Day 5: Write tiny tests and edge cases.
- Day 6: Integrate with another module in this repository.
- Day 7: Summarize what you learned in your own notes.

### 12) Reference Hygiene

To keep this document useful over time:

- Keep examples short and executable.
- Prefer plain language over jargon.
- Include at least one edge-case example per section.
- Link to neighboring guides when concepts overlap.
- Update examples when APIs or conventions change.

