# Practical Regex Reference

## Core Building Blocks

| Pattern | Meaning | Example match |
|---|---|---|
| `\d` | digit | `7` |
| `\w` | word character | `name_1` |
| `\s` | whitespace | space, tab, newline |
| `.` | any character except newline | `a`, `!`, `9` |
| `+` | one or more | `aaa` |
| `*` | zero or more | `` or `aaaa` |
| `?` | optional | `color` and `colour` |

## Search, Find All, Replace

```python
import re

text = "IDs: A-10, B-20, C-30"
print(re.search(r"[A-Z]-\d+", text).group())
print(re.findall(r"[A-Z]-\d+", text))
print(re.sub(r"\d+", "XX", text))
```

## Useful Real-World Examples

### Extract Hashtags
```python
post = "Learning #python and #regex today"
print(re.findall(r"#\w+", post))
```

### Validate a Simple Username
```python
username = "learner_24"
is_valid = bool(re.fullmatch(r"[a-z0-9_]{3,20}", username))
print(is_valid)
```

### Split on Multiple Separators
```python
line = "apples,bananas;oranges|grapes"
print(re.split(r"[,;|]", line))
```

## Tips

- Prefer raw strings like `r"\d+"`.
- Test one small pattern at a time.
- Use `re.fullmatch()` when the whole string must fit the rule.
- Add groups only when you need to capture part of the match.

## Related Reading

- [README.md](README.md)
- [reference/REGEX_REFERENCE.md](reference/REGEX_REFERENCE.md)

---

## Deep Reference

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

### Substitution with a Function

`re.sub` accepts a callable as the replacement:

```python
import re

def redact_digits(m: re.Match) -> str:
    return "X" * len(m.group())

print(re.sub(r"\d+", redact_digits, "Order 12345, SKU 99"))
# Order XXXXX, SKU XX
```

### Named Groups and Back-References

```python
import re

# Named groups make patterns self-documenting
log_line = "2024-03-15 ERROR Connection refused"
pat = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>\w+) (?P<message>.+)"
)
m = pat.match(log_line)
if m:
    print(m.group("level"),   # ERROR
          m.group("message"))  # Connection refused

# Back-reference to find repeated words
doubled = re.search(r"\b(\w+)\s+\1\b", "the the mistake")
print(doubled.group())   # 'the the'
```

### Compiling for Reuse

Always compile patterns used inside loops or called frequently:

```python
import re

# Compile once at module level
_EMAIL = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

def extract_emails(text: str) -> list[str]:
    return _EMAIL.findall(text)
```

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Write simple character class and quantifier patterns; use `re.search` and `re.findall` |
| **Developing** | Use capturing groups, anchors, and `re.sub`; choose `search` vs `match` vs `fullmatch` correctly |
| **Proficient** | Use named groups, flags, and lookaheads; compile patterns for reuse; avoid catastrophic backtracking |
| **Advanced** | Write and explain complex multi-group patterns, use `re.VERBOSE`, replace with a callable, parse structured formats |

### Suggested Practice Projects

1. **Log parser** — Extract date, log level, and message from Apache or Python log lines.
2. **Email extractor** — Find all valid email addresses in a multi-line text file.
3. **Markdown link finder** — Extract all `[text](url)` pairs from a markdown document.
4. **Phone normalizer** — Match various phone formats and reformat them all to `+1-XXX-XXX-XXXX`.
5. **Password validator** — Use `re.fullmatch` with lookaheads to require at least one digit, one uppercase, and minimum 8 characters.

### Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Forgetting raw strings | `"\d"` is the same as `"d"` because `\d` is not a recognized escape | Always use `r"\d+"` |
| `re.match` vs `re.search` | `match` only checks the start of the string | Use `search` to find anywhere; `fullmatch` for entire string |
| Greedy vs lazy | `.*` grabs as much as possible and can over-match | Use `.*?` (lazy) inside larger patterns |
| Catastrophic backtracking | Nested quantifiers like `(a+)+` on long strings cause exponential time | Simplify or use possessive quantifiers / atomic groups |
| Compiling inside a loop | `re.compile` has overhead; repeated calls in a tight loop are slow | Compile once at module level |
| `findall` with groups | When the pattern has a capturing group, `findall` returns the group contents, not full matches | Use `(?:...)` for non-capturing groups if you want full matches |

