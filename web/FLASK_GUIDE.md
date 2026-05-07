# Flask REST API Guide

Flask is a lightweight web framework that helps you turn Python functions into HTTP endpoints quickly.

## Install

```bash
pip install flask flask-restful
```

## Step 1: Create the App

```python
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return {"message": "Welcome to the API"}
```

This creates the application object and a simple health-check style route.

## Step 2: Add a Resource

```python
from flask_restful import Resource, reqparse

books = [
    {"id": 1, "title": "Python Basics", "author": "A. Dev"},
    {"id": 2, "title": "Regex Notes", "author": "B. Learner"},
]

class BookList(Resource):
    def get(self):
        return books

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, required=True)
        parser.add_argument("author", type=str, required=True)
        args = parser.parse_args()

        book = {
            "id": len(books) + 1,
            "title": args["title"],
            "author": args["author"],
        }
        books.append(book)
        return book, 201
```

## Step 3: Register the Routes

```python
class Book(Resource):
    def get(self, book_id):
        return next((book for book in books if book["id"] == book_id), {"error": "not found"})

api.add_resource(BookList, "/books")
api.add_resource(Book, "/books/<int:book_id>")
```

## Run the App

```bash
python app.py
```

## Example Requests

```bash
curl http://127.0.0.1:5000/books
curl -X POST -H "Content-Type: application/json" -d '{"title":"Flask in Action","author":"C. Builder"}' http://127.0.0.1:5000/books
curl http://127.0.0.1:5000/books/1
```

## Why This Example Matters

This guide shows the core web ideas that repeat in bigger frameworks too: routing, request parsing, JSON responses, and separating app setup from endpoint logic.

## Good Next Steps

- Add `PUT` and `DELETE` handlers
- Validate request payloads more carefully
- Replace the in-memory list with a database or file
- Compare this example with [Country_API/README.md](Country_API/README.md)

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

