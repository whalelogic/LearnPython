"""
Control Flow Playground
----------------------
Explore how Python handles conditionals, loops, and branching logic.
"""

def demonstrate_conditionals(value):
    print(f"\n--- Conditionals (Checking {value}) ---")
    if value > 100:
        print("Large number")
    elif value > 0:
        print("Positive number")
    elif value == 0:
        print("Exactly zero")
    else:
        print("Negative number")

    # Ternary operator
    status = "Even" if value % 2 == 0 else "Odd"
    print(f"The number is {status}")

def demonstrate_loops():
    print("\n--- Loops ---")
    
    # For loop with range
    print("Range loop (0-2):", end=" ")
    for i in range(3):
        print(i, end=" ")
    print()

    # Enumerate
    items = ["a", "b", "c"]
    print("Enumerate:")
    for index, value in enumerate(items):
        print(f"  [{index}]: {value}")

def demonstrate_loop_control():
    print("\n--- Loop Control (break, continue, else) ---")
    
    print("Finding the first number divisible by 7 in 1-20:")
    for i in range(1, 21):
        if i % 7 == 0:
            print(f"  Found it: {i}")
            break
    
    print("Printing odds, skipping evens (1-5):", end=" ")
    for i in range(1, 6):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()

    print("For-Else (Searching for 100 in range 1-10):")
    for i in range(1, 11):
        if i == 100:
            print("Found 100!")
            break
    else:
        print("  100 was not found. The 'else' block executed.")

def demonstrate_match_case(command):
    print(f"\n--- Match-Case (Handling '{command}') ---")
    # Note: Requires Python 3.10+
    match command.split():
        case ["quit"]:
            print("Exiting...")
        case ["load", filename]:
            print(f"Loading file: {filename}")
        case ["save", filename, "--force"]:
            print(f"Force saving: {filename}")
        case ["save", filename]:
            print(f"Saving: {filename}")
        case _:
            print("Unknown command")

def demonstrate_walrus():
    print("\n--- Walrus Operator (:=) ---")
    # Allows assignment within an expression
    if (n := len("Python")) > 5:
        print(f"The string is long enough ({n} characters)")

if __name__ == "__main__":
    demonstrate_conditionals(10)
    demonstrate_conditionals(-5)
    
    demonstrate_loops()
    demonstrate_loop_control()
    
    demonstrate_match_case("load data.csv")
    demonstrate_match_case("save backup.db --force")
    demonstrate_match_case("unknown")
    
    demonstrate_walrus()
