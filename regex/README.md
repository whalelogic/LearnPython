# Regular Expressions (Regex) in Python

This directory contains resources and examples for working with regular expressions in Python.

## Contents

### 📄 Regex_Reference.md
Comprehensive guide covering:
- Basic regex syntax
- Special characters and metacharacters
- Quantifiers and anchors
- Grouping and capturing
- Lookaheads and lookbehinds
- Common use cases
- Python's `re` module
- Performance tips
- Practical examples

### 📄 find_pattern.py
Python script demonstrating regex pattern matching in practice.

## Quick Start

### Import the re Module

```python
import re
```

### Basic Pattern Matching

```python
text = "My email is user@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print(f"Found: {match.group()}")  # Found: user@example.com
```

## Common re Module Functions

| Function | Description | Example |
|----------|-------------|---------|
| `re.search()` | Find first match | `re.search(r"pattern", text)` |
| `re.match()` | Match at string beginning | `re.match(r"^Hello", text)` |
| `re.findall()` | Find all matches | `re.findall(r"\d+", text)` |
| `re.finditer()` | Iterator of matches | `for m in re.finditer(r"\w+", text)` |
| `re.sub()` | Replace matches | `re.sub(r"old", "new", text)` |
| `re.split()` | Split by pattern | `re.split(r",", text)` |
| `re.compile()` | Compile pattern | `pattern = re.compile(r"\d+")` |

## Essential Regex Patterns

### Character Classes

```python
\d  # Digit [0-9]
\w  # Word character [a-zA-Z0-9_]
\s  # Whitespace [ \t\n\r\f\v]
\D  # Non-digit
\W  # Non-word character
\S  # Non-whitespace
.   # Any character (except newline)
```

### Quantifiers

```python
*   # 0 or more
+   # 1 or more
?   # 0 or 1
{n} # Exactly n times
{n,}  # n or more times
{n,m} # Between n and m times
```

### Anchors

```python
^   # Start of string
$   # End of string
\b  # Word boundary
\B  # Not word boundary
```

## Common Use Cases

### Email Validation

```python
import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "user@example.com"

if re.match(email_pattern, email):
    print("Valid email")
```

### Phone Number Extraction

```python
text = "Call me at 555-1234 or 555-5678"
phones = re.findall(r'\d{3}-\d{4}', text)
print(phones)  # ['555-1234', '555-5678']
```

### URL Matching

```python
text = "Visit https://example.com or http://test.org"
urls = re.findall(r'https?://[^\s]+', text)
print(urls)  # ['https://example.com', 'http://test.org']
```

### Find and Replace

```python
text = "The price is $100"
new_text = re.sub(r'\$(\d+)', r'€\1', text)
print(new_text)  # The price is €100
```

## Grouping and Capturing

```python
# Extract parts of a match
text = "John Doe (johndoe@email.com)"
pattern = r'(\w+)\s+(\w+)\s+\(([^)]+)\)'
match = re.search(pattern, text)

if match:
    first_name = match.group(1)  # John
    last_name = match.group(2)   # Doe
    email = match.group(3)       # johndoe@email.com
```

## Flags

```python
re.IGNORECASE  # Case-insensitive matching
re.MULTILINE   # ^ and $ match line starts/ends
re.DOTALL      # . matches newlines too
re.VERBOSE     # Allow comments in regex

# Using flags
pattern = re.compile(r'hello', re.IGNORECASE)
pattern.search("HELLO")  # Matches
```

## Performance Tips

### Compile Patterns for Reuse

```python
# ❌ Slow - compiles every time
for text in texts:
    match = re.search(r'\d+', text)

# ✅ Fast - compile once
pattern = re.compile(r'\d+')
for text in texts:
    match = pattern.search(text)
```

### Use Non-Greedy Quantifiers

```python
# ❌ Greedy - matches as much as possible
re.search(r'<.*>', '<tag>text</tag>')  # Matches entire string

# ✅ Non-greedy - matches as little as possible
re.search(r'<.*?>', '<tag>text</tag>')  # Matches '<tag>'
```

## Testing Regex

### Use Online Tools
- [Regex101](https://regex101.com/) - Test with explanations
- [Regexr](https://regexr.com/) - Visual testing
- [Pythex](https://pythex.org/) - Python-specific testing

### Test in Python

```python
def test_regex(pattern, test_cases):
    compiled = re.compile(pattern)
    for text, should_match in test_cases:
        match = compiled.search(text)
        result = "✓" if bool(match) == should_match else "✗"
        print(f"{result} '{text}'")

test_regex(
    r'\d{3}-\d{4}',
    [
        ("555-1234", True),
        ("5551234", False),
        ("Call 555-1234", True)
    ]
)
```

## Common Pitfalls

### Escaping Special Characters

```python
# ❌ Wrong - . matches any character
re.search(r'example.com', 'exampleXcom')  # Matches!

# ✅ Correct - escape the dot
re.search(r'example\.com', 'exampleXcom')  # No match
```

### Raw Strings

```python
# ❌ Without raw string
re.search("\\d+", "123")  # Need to escape backslash

# ✅ With raw string
re.search(r"\d+", "123")   # Cleaner
```

## Running Examples

To run the example script:

```bash
python find_pattern.py
```

## Learning Path

1. **Read** `Regex_Reference.md` for comprehensive theory
2. **Experiment** with patterns in Python REPL
3. **Run** `find_pattern.py` to see practical examples
4. **Practice** with online regex testers
5. **Apply** regex to your own text processing tasks

## Quick Reference Card

```python
# Pattern matching
re.search(r'pattern', text)      # First match
re.findall(r'pattern', text)     # All matches
re.sub(r'old', 'new', text)      # Replace

# Common patterns
r'\d+'          # One or more digits
r'\w+'          # One or more word chars
r'[a-zA-Z]+'    # One or more letters
r'^\d{3}$'      # Exactly 3 digits, whole string
r'(pattern)'    # Capture group
r'(?:pattern)'  # Non-capturing group
```

## Additional Resources

- [Python re Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
- [Regex101](https://regex101.com/) - Interactive tester
- Main repository: [LearnPython](../)

---

**Practice makes perfect!** Start with simple patterns and gradually increase complexity.
