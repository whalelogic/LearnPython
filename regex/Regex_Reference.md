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
