

# A variable is a container for storing data values. In Python, you can create
# a variable by simply assigning a value to it like so:

# An integer variable
x = 5
print(x)
print(type(x))


# A string variable
y = "Hello, World!"
print(y)
print(type(y))


# A float variable
z = 3.14
print(z)
print(type(z))


# You can also reassign a variable to a different value or even a different type:
x = "Now I'm a string!"
print(x)
print(type(x))

# Variables can also be used in expressions and can hold the result of calculations:
a = 10
b = 20
c = a + b
print(c)  # Output: 30

# In Python, variable names must start with a letter or an underscore and can contain letters, numbers, and underscores. They are case-sensitive, meaning that 'myVariable' and 'myvariable' are considered different variables.

# It's important to choose meaningful variable names that describe the data they hold, as this makes your code easier to read and understand.

# Example of meaningful variable names

age = 25
name = "Alice"

# Printing and `f-strings` are a convenient way to include variable values in strings. The `f` before the string allows you to embed expressions inside curly braces `{}` which will be evaluated at runtime and included in the string output.

print(f"{name} is {age} years old.")
print(f"The value of x is: {x}")
