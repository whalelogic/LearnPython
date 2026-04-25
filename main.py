# Welcome!

# Using Python 3.14.4



# Define a function.
def say_hi(name: str) -> str:
    """ A function that takes a string (name), and return a greeting. """
    return f"Hi, {name}!"


# The 'main' function (the program) run below
def main():
    print("Welcome to LearnPython!")
    print("This is a new line.")
    print(say_hi("Thucydides")) # This is a comment
    print(say_hi("Plato"))
    print(say_hi("Aristotle"))
    print(say_hi("Socrates"))


# This runs the 'main' function above.
if __name__ == "__main__":
    main()
