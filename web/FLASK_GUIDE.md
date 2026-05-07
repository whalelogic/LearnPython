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
