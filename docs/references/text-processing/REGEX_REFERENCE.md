# Regular Expressions in Python: Comprehensive Reference

Regular expressions (regex) describe text patterns. In Python, the `re` module lets you validate formats, extract structured parts from strings, transform text, and build robust parsers for semi-structured data.

## Mental Model

Think of regex as a tiny pattern language with three layers:

1. **Atoms**: literal chars, classes (`a`, `\d`, `[A-Z]`)
2. **Quantifiers**: how many (`*`, `+`, `{m,n}`)
3. **Control**: anchors, groups, assertions (`^`, `$`, `()`, `(?=...)`, `\b`)

Regex answers: **"Where does this pattern occur?"** and **"What subparts can I capture?"**

## Python `re` Module Essentials

| Function | Purpose |
|---|---|
| `re.search(pattern, text)` | First match anywhere |
| `re.match(pattern, text)` | Match only at start |
| `re.fullmatch(pattern, text)` | Entire string must match |
| `re.findall(pattern, text)` | Return all matches as list |
| `re.finditer(pattern, text)` | Iterator of match objects |
| `re.sub(pattern, repl, text)` | Replace matching text |
| `re.split(pattern, text)` | Split text by pattern |
| `re.compile(pattern, flags=0)` | Precompile pattern object |

## Raw Strings Matter

Always prefer raw strings (`r"..."`) for regex patterns:

```python
pattern = r"\d+"   # correct
# pattern = "\d+"  # works but harder to read
```

## Syntax Reference

## 1) Literal Characters

| Pattern | Meaning |
|---|---|
| `cat` | Match exact text `cat` |
| `\.` | Literal dot |
| `\*` | Literal asterisk |

## 2) Character Classes

| Pattern | Meaning | Example matches |
|---|---|---|
| `[abc]` | One char: a or b or c | `a`, `b` |
| `[a-z]` | Lowercase letter | `m` |
| `[A-Za-z0-9_]` | Word-like class | `K`, `7`, `_` |
| `[^0-9]` | Any non-digit | `A`, `#` |

## 3) Predefined Classes

| Pattern | Meaning |
|---|---|
| `\d` | Digit (`[0-9]`) |
| `\D` | Non-digit |
| `\w` | Word char (`[A-Za-z0-9_]` in ASCII mode) |
| `\W` | Non-word char |
| `\s` | Whitespace |
| `\S` | Non-whitespace |

## 4) Quantifiers

| Pattern | Meaning |
|---|---|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 |
| `{n}` | Exactly n |
| `{n,}` | n or more |
| `{n,m}` | Between n and m |

### Greedy vs non-greedy

- Greedy: `.*` takes as much as possible.
- Non-greedy: `.*?` takes as little as possible.

```python
import re
text = "<b>one</b><b>two</b>"
print(re.findall(r"<b>.*</b>", text))    # ['<b>one</b><b>two</b>']
print(re.findall(r"<b>.*?</b>", text))   # ['<b>one</b>', '<b>two</b>']
```

## 5) Anchors and Boundaries

| Pattern | Meaning |
|---|---|
| `^` | Start of string (or line with `re.M`) |
| `$` | End of string (or line with `re.M`) |
| `\A` | Absolute start of string |
| `\Z` | Absolute end of string |
| `\b` | Word boundary |
| `\B` | Not a word boundary |

## 6) Groups and Backreferences

| Pattern | Meaning |
|---|---|
| `(abc)` | Capturing group |
| `(?:abc)` | Non-capturing group |
| `(?P<name>...)` | Named group |
| `\1`, `\2` | Backreference by index |
| `(?P=name)` | Backreference by name |

```python
m = re.search(r"(?P<area>\d{3})-(?P<number>\d{4})", "555-1234")
print(m.group("area"), m.group("number"))
```

## 7) Lookarounds (Assertions)

| Pattern | Meaning |
|---|---|
| `(?=...)` | Positive lookahead |
| `(?!...)` | Negative lookahead |
| `(?<=...)` | Positive lookbehind |
| `(?<!...)` | Negative lookbehind |

```python
text = "ID:1234, ref:ABCD"
print(re.findall(r"\d+(?=,)", text))  # ['1234']
```

## Flags Reference

| Flag | Name | Effect |
|---|---|---|
| `re.I` | Ignore case | Case-insensitive matching |
| `re.M` | Multiline | `^` and `$` work per line |
| `re.S` | Dotall | `.` matches newline too |
| `re.X` | Verbose | Allows spacing/comments in patterns |
| `re.A` | ASCII | ASCII-only behavior for `\w`, `\b`, etc. |

Example with verbose mode:

```python
pattern = re.compile(r"""
    ^
    (?P<user>[a-z0-9._%+-]+)
    @
    (?P<host>[a-z0-9.-]+)
    \.
    (?P<tld>[a-z]{2,})
    $
""", re.I | re.X)
```

## Match Object Reference

| Method | Meaning |
|---|---|
| `group()` | Full match |
| `group(n)` | Capture group by index |
| `group("name")` | Capture by name |
| `groups()` | Tuple of all captured groups |
| `groupdict()` | Dict of named groups |
| `span()` | Start/end index tuple |
| `start()`, `end()` | Match boundaries |

## Search Function Comparison

| API | Checks from beginning only? | Requires whole string? | Returns |
|---|---|---|---|
| `search` | No | No | First match anywhere |
| `match` | Yes | No | Match at position 0 |
| `fullmatch` | Yes | Yes | Full-string match |

## Real-world Patterns

## 1) Email validation (basic practical form)

```python
email_re = re.compile(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$", re.I)
print(bool(email_re.fullmatch("user@example.com")))  # True
```

## 2) URL extraction

```python
text = "Visit https://example.com and http://test.org/docs"
urls = re.findall(r"https?://[^\s]+", text)
```

## 3) Date parsing (`YYYY-MM-DD`)

```python
date_re = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
m = date_re.fullmatch("2026-05-07")
if m:
    year, month, day = map(int, m.groups())
```

## 4) Log line parsing

```python
log = '127.0.0.1 - - [07/May/2026:10:22:11 +0000] "GET /index.html HTTP/1.1" 200 1234'
pattern = re.compile(
    r'(?P<ip>\S+)\s+-\s+-\s+\[(?P<time>[^\]]+)\]\s+"(?P<method>\S+)\s+(?P<path>\S+)\s+(?P<proto>[^"]+)"\s+(?P<status>\d{3})\s+(?P<size>\d+)'
)
m = pattern.search(log)
if m:
    print(m.groupdict())
```

## 5) Tokenizing words and numbers

```python
text = "Order 12 apples, 3 bananas."
tokens = re.findall(r"\d+|[A-Za-z]+", text)
```

## Replacement Patterns (`re.sub`)

```python
text = "Call me at 555-1234"
masked = re.sub(r"\d", "*", text)
print(masked)
```

Using captured groups in replacement:

```python
name = "Doe, Jane"
fixed = re.sub(r"^(\w+),\s*(\w+)$", r"\2 \1", name)
print(fixed)  # Jane Doe
```

Using function replacement:

```python
def repl(m):
    return str(int(m.group()) * 2)

print(re.sub(r"\d+", repl, "x=5 y=10"))  # x=10 y=20
```

## Splitting with Regex

```python
line = "apple, banana;pear | grape"
parts = re.split(r"\s*[,;|]\s*", line)
print(parts)
```

## Performance Guidance

| Practice | Benefit |
|---|---|
| Compile repeated patterns | Avoid re-parsing pattern each call |
| Use specific classes instead of `.*` | Reduce backtracking |
| Prefer anchors when validating full strings | Faster reject and clearer intent |
| Break giant patterns into verbose mode with comments | Easier maintenance |

## Catastrophic Backtracking (Concept)

Certain nested quantifier patterns can blow up runtime on near-miss inputs.

Risky style example:

```regex
^(a+)+$
```

Safer strategy:
- avoid ambiguous nested repeats,
- use specific boundaries,
- test against adversarial inputs.

## Debugging Workflow

1. Start with a tiny target string.
2. Build pattern in increments.
3. Test each group before adding quantifiers.
4. Print `match.span()` and `groups()`.
5. Add anchors and boundaries for precision.

## Regex vs Plain String Methods

| Task | Prefer |
|---|---|
| Exact prefix/suffix checks | `str.startswith`, `str.endswith` |
| Simple replacement | `str.replace` |
| Structured extraction by pattern | `re` |
| Complex validation with multiple conditions | `re.fullmatch` |

Use regex when pattern logic is genuinely pattern-based; don't overuse it for simple string operations.

## Practical Recipe: Parsing Key-Value Pairs

```python
text = "name=alice;role=admin;active=true"
pairs = re.findall(r"([a-z_]+)=([^;]+)", text)
result = {k: v for k, v in pairs}
print(result)
```

## Practical Recipe: Strong Password Check

```python
password_re = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,64}$"
)

print(bool(password_re.fullmatch("SafePass1!")))
```

## Practical Recipe: Cleaning Whitespace

```python
def normalize_whitespace(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()
```

## Common Mistakes

| Mistake | Example | Fix |
|---|---|---|
| Forgetting raw string prefix | `"\bword\b"` confusion | Use `r"\bword\b"` |
| Using `match` when full validation needed | Partial acceptance | Use `fullmatch` |
| Overusing greedy `.*` | Over-captures text | Use precise classes or `.*?` |
| Assuming `\w` is all Unicode letters | Locale/flag differences | Use explicit classes as needed |
| Building unreadable mega-patterns | Hard maintenance | Use `re.X` verbose mode |

## Practice Goals

- Write patterns for extraction, validation, and replacement.
- Use named groups and lookarounds intentionally.
- Explain `search` vs `match` vs `fullmatch`.
- Optimize a slow regex by reducing ambiguity.

Regex mastery dramatically improves text-processing productivity for logs, APIs, ETL pipelines, and data cleaning tasks.
