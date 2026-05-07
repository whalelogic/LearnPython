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

## Flask Request and Response Deep Dive

### Request lifecycle (high level)

1. A client sends an HTTP request.
2. Flask matches the URL to a route.
3. Route code reads request data.
4. Business logic runs.
5. A response object is returned.
6. Flask sends status, headers, and body.

### Read request data safely

```python
from flask import request

@app.post("/echo")
def echo():
    payload = request.get_json(silent=True) or {}
    message = payload.get("message")
    if not message:
        return {"error": "message is required"}, 400
    return {"message": message}, 200
```

### Return explicit status codes

- `200` for successful reads/updates.
- `201` for successful resource creation.
- `400` for invalid input.
- `404` when resource is missing.
- `500` only for unexpected server errors.

## Validation Strategy

Use two levels of validation:

- **Transport validation**: is JSON well-formed and required fields present?
- **Domain validation**: does the data make sense in business terms?

Example checks:

- title length > 0
- author length > 0
- IDs are positive integers
- no duplicate title/author pair in simple demo datasets

## Error Handling Pattern

```python
@app.errorhandler(404)
def not_found(_error):
    return {"error": "route not found"}, 404

@app.errorhandler(500)
def internal_error(_error):
    return {"error": "internal server error"}, 500
```

Keep internal details out of user-facing responses.

## Project Structure for Growth

As endpoints increase, split files:

- `app.py` for app factory/startup
- `resources/books.py` for book resources
- `services/books.py` for business rules
- `schemas/books.py` for validation schemas

This avoids one giant route file.

## Testing Checklist for Flask APIs

- Unit test service logic without HTTP first.
- Use Flask test client for endpoint tests.
- Check status code and response body.
- Test happy path and invalid input path.
- Verify not-found behavior.

## Flask Security Basics

- Never trust client input.
- Limit payload size where possible.
- Avoid returning stack traces.
- Use environment variables for secrets.
- Add authentication before exposing write endpoints.

## Performance Notes

- Minimize expensive work inside routes.
- Cache repeated lookups where sensible.
- Paginate list endpoints for large datasets.
- Add timing logs for slow routes.

## Production Readiness Reminders

- Run behind a production WSGI/ASGI server.
- Add structured logs.
- Add health and readiness endpoints.
- Add request IDs for tracing.
- Document each endpoint contract.

## Practice Tasks

1. Add `PUT /books/<id>` with validation.
2. Add `DELETE /books/<id>`.
3. Add pagination to `GET /books`.
4. Add query filter `?author=`.
5. Add simple token auth middleware.
6. Add tests for all status code paths.

## Related Reading

- [Country_API/README.md](Country_API/README.md)
- [../system/FILE_IO_GUIDE.md](../system/FILE_IO_GUIDE.md)
- [../data/PANDAS_GUIDE.md](../data/PANDAS_GUIDE.md)
