"""
Functions Playground
-------------------
This file demonstrates various ways to define and use functions in Python.
"""

def basic_function(name: str) -> str:
    """A simple function with a type hint."""
    return f"Hello, {name}!"

def function_with_defaults(name: str, greeting: str = "Hi") -> str:
    """A function with a default parameter."""
    return f"{greeting}, {name}!"

def variadic_function(*args, **kwargs):
    """
    Demonstrates *args (tuple of positional args)
    and **kwargs (dictionary of keyword args).
    """
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

def mutable_default_gotcha(item, collection=[]):
    """
    DANGER: The list is created once at definition time,
    not each time the function is called!
    """
    collection.append(item)
    return collection

def safe_default(item, collection=None):
    """The safe way to handle mutable defaults."""
    if collection is None:
        collection = []
    collection.append(item)
    return collection

def outer_function(text):
    """Demonstrates a closure."""
    def inner_function():
        print(f"Closure remembered: {text}")
    return inner_function

def simple_decorator(func):
    """A basic decorator that adds logging."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper

@simple_decorator
def decorated_greet(name):
    print(f"Greetings, {name}!")

if __name__ == "__main__":
    print("--- Basic Functions ---")
    print(basic_function("Pythonista"))
    print(function_with_defaults("Friend"))
    print(function_with_defaults("Developer", greeting="Welcome"))

    print("\n--- Variadic Arguments ---")
    variadic_function(1, 2, 3, mode="debug", verbose=True)

    print("\n--- Mutable Default Gotcha ---")
    print(f"Call 1: {mutable_default_gotcha(1)}")
    print(f"Call 2: {mutable_default_gotcha(2)}")  # Surprise! [1, 2]

    print("\n--- Safe Default ---")
    print(f"Call 1: {safe_default(1)}")
    print(f"Call 2: {safe_default(2)}")  # Correct: [2]

    print("\n--- Lambda Functions ---")
    square = lambda x: x * x
    print(f"Square of 5: {square(5)}")

    print("\n--- Closures ---")
    my_closure = outer_function("Secret Message")
    my_closure()

    print("\n--- Decorators ---")
    decorated_greet("World")
