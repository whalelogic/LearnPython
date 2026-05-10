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

### Pattern Syntax Quick-Reference

| Pattern | Meaning | Matches | Does not match |
|---|---|---|---|
| `\d` | Digit `[0-9]` | `7`, `0` | `a`, ` ` |
| `\D` | Non-digit | `a`, `!` | `5` |
| `\w` | Word char `[a-zA-Z0-9_]` | `name_1` | `-`, ` ` |
| `\W` | Non-word char | ` `, `-` | `a` |
| `\s` | Whitespace | space, tab, `\n` | `a` |
| `\S` | Non-whitespace | `a`, `!` | ` ` |
| `.` | Any char except `\n` | `a`, `9`, `!` | `\n` |
| `^` | Start of string (or line with `re.M`) | — | — |
| `$` | End of string (or line with `re.M`) | — | — |
| `\b` | Word boundary | Between `\w` and `\W` | — |
| `[abc]` | Character class | `a`, `b`, `c` | `d` |
| `[^abc]` | Negated class | anything except `a`, `b`, `c` | — |
| `[a-z]` | Character range | `a` through `z` | `A`, `1` |
| `a\|b` | Alternation | `a` or `b` | `c` |
| `(abc)` | Capturing group | captures `abc` | — |
| `(?:abc)` | Non-capturing group | groups without capturing | — |
| `(?P<name>...)` | Named group | captures with name | — |
| `(?=...)` | Lookahead (positive) | position before match | — |
| `(?!...)` | Lookahead (negative) | position where not followed by | — |
| `(?<=...)` | Lookbehind (positive) | position after match | — |

#### Quantifiers

| Quantifier | Meaning | Greedy? |
|---|---|---|
| `*` | Zero or more | Yes |
| `+` | One or more | Yes |
| `?` | Zero or one (optional) | Yes |
| `{n}` | Exactly `n` | — |
| `{n,}` | At least `n` | Yes |
| `{n,m}` | Between `n` and `m` | Yes |
| `*?` / `+?` / `??` | Lazy (minimal) versions | No |

### `re` Module Function Reference

| Function | Description | Returns |
|---|---|---|
| `re.search(pat, s, flags=0)` | Find first match anywhere in string | `Match` or `None` |
| `re.match(pat, s, flags=0)` | Match only at the start of string | `Match` or `None` |
| `re.fullmatch(pat, s, flags=0)` | Entire string must match | `Match` or `None` |
| `re.findall(pat, s, flags=0)` | All non-overlapping matches | `list[str]` or `list[tuple]` |
| `re.finditer(pat, s, flags=0)` | Iterator of `Match` objects | iterator |
| `re.sub(pat, repl, s, count=0)` | Replace matches with `repl` | `str` |
| `re.subn(pat, repl, s)` | Replace and return count | `(str, int)` |
| `re.split(pat, s, maxsplit=0)` | Split on pattern | `list[str]` |
| `re.compile(pat, flags=0)` | Compile for reuse | `re.Pattern` |
| `re.escape(s)` | Escape all special chars in `s` | `str` |

### `Match` Object Methods

| Method / Attribute | Returns |
|---|---|
| `.group(0)` or `.group()` | Entire matched string |
| `.group(n)` | Content of capturing group `n` |
| `.group("name")` | Content of named group |
| `.groups()` | Tuple of all capturing groups |
| `.groupdict()` | Dict of all named groups |
| `.start()` / `.end()` | Start / end index in original string |
| `.span()` | `(start, end)` tuple |

### Flags Reference

| Flag | Shorthand | Effect |
|---|---|---|
| `re.IGNORECASE` | `re.I` | Case-insensitive matching |
| `re.MULTILINE` | `re.M` | `^` and `$` match at each line boundary |
| `re.DOTALL` | `re.S` | `.` matches `\n` too |
| `re.VERBOSE` | `re.X` | Allow whitespace and `#` comments in pattern |
| `re.ASCII` | `re.A` | `\w`, `\d`, etc. match ASCII only |

```python
# re.VERBOSE — break a complex pattern across lines
import re

date_pat = re.compile(r"""
    (?P<year>  \d{4})   # four-digit year
    [-/]
    (?P<month> \d{1,2}) # one or two digit month
    [-/]
    (?P<day>   \d{1,2}) # one or two digit day
""", re.VERBOSE)

m = date_pat.fullmatch("2024-07-04")
print(m.groupdict())  # {'year': '2024', 'month': '07', 'day': '04'}
```

### Common Real-World Patterns

```python
import re

# Email (simplified)
EMAIL = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

# URL
URL = re.compile(r"https?://[^\s/$.?#].[^\s]*")

# US phone number
PHONE = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")

# IPv4 address
IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

# Username: 3–20 alphanumeric + underscore
USERNAME = re.compile(r"^[a-z0-9_]{3,20}$", re.I)

# Hashtags
HASHTAG = re.compile(r"#\w+")

# Strip HTML tags
HTML_TAG = re.compile(r"<[^>]+>")

# Extract all numbers (int or float)
NUMBER = re.compile(r"-?\d+(?:\.\d+)?")
```

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

## Extended Pattern Library

## Contact and Identifier Patterns

| Use case | Pattern | Notes |
|---|---|---|
| Username (3-20 chars) | `^[a-zA-Z][a-zA-Z0-9_]{2,19}$` | Must start with letter |
| UUID v4 (simple) | `^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$` | Case-insensitive recommended |
| IPv4 | `^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$` | Strict numeric ranges |
| Hex color | `^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$` | CSS color formats |

## Log Parsing Recipes

### Apache-like logs

```python
apache_re = re.compile(
    r'(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<time>[^\]]+)\]\s+"(?P<method>\S+)\s+(?P<path>\S+)\s+(?P<proto>[^"]+)"\s+(?P<status>\d{3})\s+(?P<size>\S+)'
)
```

### Key-value logs (`k=v`)

```python
line = "level=INFO user=alice op=login duration_ms=18"
pairs = re.findall(r"([a-z_]+)=([^\s]+)", line)
record = dict(pairs)
```

### Timestamp extraction

```python
ts = re.search(r"\b\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}\b", "at 2026-05-07 12:31:15 done")
```

## Text Normalization Patterns

```python
def normalize_spaces(s):
    return re.sub(r"\s+", " ", s).strip()


def normalize_quotes(s):
    return re.sub(r"[“”]", '"', s)


def remove_non_alnum_keep_space(s):
    return re.sub(r"[^\w\s]", "", s)
```

## Advanced Grouping Notes

| Syntax | Use when |
|---|---|
| `(?:...)` | Grouping without capture overhead |
| `(?P<name>...)` | Need semantic extraction by field name |
| `(?P=name)` | Enforce repeated structure with clarity |
| `(?>...)` | Atomic groups are not available in Python `re` |

Python's `re` favors readability and portability over every advanced engine feature.

## Lookaround Use Cases

### 1) Extract value before `%`

```python
print(re.findall(r"\d+(?=%)", "cpu=87% mem=42%"))
```

### 2) Ensure word not followed by suffix

```python
print(re.findall(r"cat(?!s)", "cat cats catlike"))
```

### 3) Match currency amounts after `$`

```python
print(re.findall(r"(?<=\$)\d+(?:\.\d{2})?", "Total $12.50 and fee $3"))
```

## Multi-line and Dotall Behavior

```python
text = "line1\nline2\nline3"
print(bool(re.search(r"^line2$", text, re.M)))    # True
print(bool(re.search(r"line1.*line3", text, re.S)))  # True
```

## Named Capture for Structured Parsing

```python
event_re = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<level>INFO|WARN|ERROR)\s+"
    r"(?P<message>.+)$"
)

line = "2026-05-07 ERROR payment failed"
m = event_re.fullmatch(line)
if m:
    event = m.groupdict()
```

## Defensive Validation with `fullmatch`

`search` may accept unwanted strings.

```python
print(bool(re.search(r"\d+", "abc123xyz")))      # True
print(bool(re.fullmatch(r"\d+", "abc123xyz")))   # False
```

Use `fullmatch` for strict validation fields.

## Pattern Composition Tips

### Build from fragments

```python
YEAR = r"\d{4}"
MONTH = r"0[1-9]|1[0-2]"
DAY = r"0[1-9]|[12]\d|3[01]"
DATE = rf"(?:{YEAR})-(?:{MONTH})-(?:{DAY})"

date_re = re.compile(rf"^{DATE}$")
```

### Compile once, reuse often

```python
WORD_RE = re.compile(r"\b[a-zA-Z]{3,}\b")
for text in ["one two", "many words here"]:
    print(WORD_RE.findall(text))
```

## Parsing Semi-structured Config

```python
cfg = """
host = localhost
port = 5432
ssl = true
"""

entry_re = re.compile(r"^\s*([a-z_]+)\s*=\s*(.+?)\s*$", re.M)
parsed = {k: v for k, v in entry_re.findall(cfg)}
```

## Common Extraction Patterns

| Goal | Pattern |
|---|---|
| Hashtags | `#\w+` |
| Mentions | `@\w+` |
| Quoted text | `"([^"]*)"` |
| Integers incl. sign | `[+-]?\d+` |
| Decimal number | `[+-]?\d+(?:\.\d+)?` |
| Repeated words | `\b(\w+)\s+\1\b` |

## Data Cleaning Pipeline Example

```python
def clean_text(s):
    s = s.lower()
    s = re.sub(r"https?://[^\s]+", "", s)   # remove URLs
    s = re.sub(r"[^a-z0-9\s]", " ", s)      # keep letters/numbers/spaces
    s = re.sub(r"\s+", " ", s).strip()      # collapse spaces
    return s
```

## Testing Regex with Cases

```python
def assert_matches(pattern, valid, invalid, flags=0):
    r = re.compile(pattern, flags)
    for s in valid:
        assert r.fullmatch(s), f"Expected valid: {s}"
    for s in invalid:
        assert not r.fullmatch(s), f"Expected invalid: {s}"

assert_matches(
    r"^[a-z]{3,8}$",
    valid=["alpha", "python"],
    invalid=["A", "ab", "toolongword", "abc123"],
)
```

## Readability Strategies for Large Patterns

- Use `re.X` and named groups.
- Keep one semantic component per line.
- Add comments for edge constraints.
- Maintain test vectors next to pattern definitions.

## Practical Anti-patterns

| Anti-pattern | Why it hurts |
|---|---|
| Mega-regex replacing parser when grammar is complex | Hard to maintain and debug |
| Relying only on regex for semantic validation | Regex checks shape, not full meaning |
| Ignoring Unicode/locale requirements | Unexpected misses or false matches |
| Copy-pasting internet patterns without tests | Hidden vulnerabilities and false assumptions |

## When Not to Use Regex

Prefer other tools when:
- format is structured (use JSON/YAML/XML parsers),
- delimiters are simple (`split`, `partition`),
- logic requires nested grammar parsing (use tokenizer/parser).

## Extended Practice Set

1. Validate usernames with start/end rules.
2. Extract all signed decimal numbers from reports.
3. Parse timestamped logs into dictionaries.
4. Remove HTML tags conservatively from simple snippets.
5. Build a pattern that matches Python identifiers but excludes keywords.

Regex is most powerful when paired with disciplined testing, clear naming, and incremental pattern construction.

## Domain-specific Mini References

## Financial Amount Parsing

```python
amount_re = re.compile(r"^(?P<currency>[A-Z]{3})\s+(?P<amount>[+-]?\d+(?:\.\d{2})?)$")
for s in ["USD 12.50", "EUR -9.00"]:
    m = amount_re.fullmatch(s)
    if m:
        print(m.groupdict())
```

## Semantic Version Extraction

```python
semver_re = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?(?:\+([0-9A-Za-z.-]+))?$")
print(bool(semver_re.fullmatch("1.2.3-alpha+build.9")))
```

## HTML-like tag pair matching (simple)

```python
tag_re = re.compile(r"<(?P<tag>[a-z][a-z0-9]*)>(?P<body>.*?)</(?P=tag)>", re.I | re.S)
```

This is useful for simple snippets, but full HTML parsing should use an HTML parser.

## CSV-like quoted field extraction (lightweight)

```python
line = 'a,"b,c",d'
fields = re.findall(r'"(?:[^"]|"")*"|[^,]+', line)
```

## Regex for Data Quality Audits

```python
def find_suspicious_ids(ids):
    bad = []
    pattern = re.compile(r"^[A-Z]{2}-\d{6}$")
    for value in ids:
        if not pattern.fullmatch(value):
            bad.append(value)
    return bad
```

## Benchmarking Pattern Choices

```python
import time

texts = ["user123@example.com"] * 10000
p1 = re.compile(r".+@.+\..+")
p2 = re.compile(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$", re.I)

start = time.perf_counter()
_ = [bool(p1.fullmatch(t)) for t in texts]
print("p1", time.perf_counter() - start)

start = time.perf_counter()
_ = [bool(p2.fullmatch(t)) for t in texts]
print("p2", time.perf_counter() - start)
```

More precise patterns are often both safer and faster.

## Regex Design Checklist

- Define whether you need extraction, validation, or replacement.
- Anchor full validations with `^...$` or `fullmatch`.
- Prefer named groups for fields with semantic meaning.
- Keep patterns tested with valid/invalid examples.
- Avoid catastrophic patterns in user-facing services.

## Pattern Documentation Template

For each production regex, document:

1. Purpose
2. Allowed input examples
3. Rejected input examples
4. Captured groups and semantics
5. Performance notes

## Comprehensive Practice Grid

| Level | Exercise |
|---|---|
| Beginner | Match phone numbers and postal codes |
| Intermediate | Parse log entries into structured dicts |
| Intermediate | Normalize free text with chained substitutions |
| Advanced | Build verbose pattern with lookarounds and named groups |
| Advanced | Optimize a slow regex and write benchmark tests |

Regex becomes maintainable when patterns are treated like code: named, tested, reviewed, and documented.

## Extended End-to-End Examples

## Example: Parsing application metrics lines

```python
line = "service=api latency_ms=123 status=200 route=/users"
metric_re = re.compile(r"([a-z_]+)=([^\s]+)")
metrics = {k: v for k, v in metric_re.findall(line)}
print(metrics)
```

## Example: Extract and validate markdown headings

```python
doc = """
# Title
## Section A
text
### Subsection
"""

heading_re = re.compile(r"^(?P<level>#{1,6})\s+(?P<title>.+)$", re.M)
for m in heading_re.finditer(doc):
    print(len(m.group("level")), m.group("title"))
```

## Example: Redacting PII-like patterns

```python
def redact(text):
    text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[SSN]", text)
    text = re.sub(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", "[EMAIL]", text, flags=re.I)
    return text
```

## Example: Parsing command-like input

```python
command = "deploy --env=prod --replicas=3 --dry-run"
flag_re = re.compile(r"--(?P<name>[a-z-]+)(?:=(?P<value>[^\s]+))?")
flags = {}
for m in flag_re.finditer(command):
    flags[m.group("name")] = m.group("value") if m.group("value") is not None else True
print(flags)
```

## Example: Duplicate word detector with normalization

```python
def duplicate_words(sentence):
    return re.findall(r"\b(\w+)\b(?=\s+\1\b)", sentence.lower())

print(duplicate_words("This is is a test Test"))
```

## Example: Identifier validation excluding Python keywords

```python
import keyword

identifier_re = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

def is_valid_identifier(name):
    return bool(identifier_re.fullmatch(name)) and not keyword.iskeyword(name)
```

## Capturing Strategy Guide

| Goal | Strategy |
|---|---|
| Keep only full match | Use no explicit groups or non-capturing groups |
| Extract several fields | Use named groups with `groupdict()` |
| Reuse matched fragment later | Backreference (`\1` / `(?P=name)`) |
| Repetition only for grouping | Non-capturing group `(?:...)` |

## Replacement Strategy Guide

| Task | Replacement approach |
|---|---|
| Static replacement | String replacement text |
| Rearranging captured parts | Backreference replacement (`r"\2 \1"`) |
| Conditional/computed replacement | Function callback replacement |

## Unicode and Locale Notes

By default, Python `re` in Python 3 works with Unicode strings.

- `\w` includes many word characters depending on mode.
- Use `re.A` for ASCII-only behavior.
- For strict multilingual processing, test language-specific examples explicitly.

## Safe Regex Deployment Checklist

- Benchmark against representative large inputs.
- Keep patterns version-controlled and documented.
- Add unit tests with expected match groups.
- Include negative tests for common malformed input.
- Avoid exposing catastrophic patterns to untrusted text in hot paths.

## Regex Maintenance Workflow

1. Document intent in comments or nearby docs.
2. Add examples of accepted and rejected inputs.
3. Encapsulate pattern in named constant.
4. Add tests before editing pattern.
5. Review changes with a peer before production rollout.

## Production-ready Pattern Constant Example

```python
EMAIL_PATTERN = re.compile(
    r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$",
    re.I,
)

DATE_PATTERN = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
```

## Regex Learning Milestones

| Milestone | Skills |
|---|---|
| 1 | Literals, classes, quantifiers |
| 2 | Anchors, groups, replacement |
| 3 | Named groups, lookarounds, flags |
| 4 | Performance tuning and maintainability |
| 5 | Production-grade test-driven regex development |

If you can design, explain, and test patterns using these milestones, you're operating at an advanced practical regex level in Python.


## Related Context in This Repository

- Start with the practical overview in [../Regex_Reference.md](../Regex_Reference.md) and use this file when you need deeper syntax details or trickier matching patterns.
- The example script in [../find_pattern.py](../find_pattern.py) is a good place to test one expression at a time before applying it to a bigger text-cleaning task.
- Regex gets easier when you treat each pattern as a series of decisions: what counts as a token, where the match can start, how much text to consume, and what should be captured.
