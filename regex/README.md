# Regular Expressions (Regex) in Python

Regex helps you search, validate, split, and rewrite text using patterns.

## In This Folder

- [Regex_Reference.md](Regex_Reference.md) — practical introduction and common patterns
- [reference/README.md](reference/README.md) — deeper regex syntax notes
- `find_pattern.py` — a script for experimenting with matches

## A Beginner-Friendly Mental Model

A regex describes **what text should look like**, not how to manually scan one character at a time. You describe pieces such as digits, spaces, optional parts, and repetition, then let Python's `re` engine do the matching.

## Quick Example

```python
import re

text = "Order #1042 will ship on 2026-05-09"
match = re.search(r"\d{4}-\d{2}-\d{2}", text)
if match:
    print(match.group())
```

## Good Uses for Regex

- Extract email addresses, dates, IDs, and tags
- Validate a constrained input format
- Replace repeated text patterns
- Split strings on flexible separators

## When Not to Use Regex

If plain string methods solve the problem clearly, use them. Regex is powerful, but it becomes hard to maintain when a simple `split()`, `replace()`, or `startswith()` would do.
