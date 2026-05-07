# Markdown Syntax Guide

A comprehensive guide to Markdown formatting for creating well-structured documentation.

## Headers

Use `#` symbols for headers. More `#` symbols = smaller header.

```markdown
# H1 - Main Title
## H2 - Section
### H3 - Subsection
#### H4 - Minor Heading
##### H5 - Even Smaller
###### H6 - Smallest
```

## Emphasis

```markdown
*italic* or _italic_
**bold** or __bold__
***bold and italic***
~~strikethrough~~
```

Result: *italic*, **bold**, ***bold and italic***, ~~strikethrough~~

## Lists

### Unordered Lists

```markdown
- Item 1
- Item 2
  - Nested item 2.1
  - Nested item 2.2
- Item 3

* Also works with asterisks
+ Or plus signs
```

### Ordered Lists

```markdown
1. First item
2. Second item
3. Third item
   1. Nested item
   2. Another nested item
```

## Links

```markdown
[Link text](https://example.com)
[Link with title](https://example.com "Hover title")
[Reference-style link][reference]

[reference]: https://example.com
```

## Images

```markdown
![Alt text](image-url.jpg)
![Alt text](image-url.jpg "Image title")
```

## Code

### Inline Code

Use single backticks for inline code: `` `code here` ``

```markdown
Use the `print()` function to display output.
```

### Code Blocks

Use triple backticks with optional language specification:

````markdown
```python
def hello_world():
    print("Hello, World!")
```

```javascript
function helloWorld() {
    console.log("Hello, World!");
}
```

```bash
echo "Hello, World!"
```
````

### Code Block with No Language

````markdown
```
Plain code block without syntax highlighting
```
````

## Blockquotes

```markdown
> This is a blockquote
> It can span multiple lines
>
> And have multiple paragraphs
```

Result:
> This is a blockquote
> It can span multiple lines

## Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data     | Data     |
| Row 2    | Data     | Data     |

# Alignment
| Left | Center | Right |
|:-----|:------:|------:|
| L    | C      | R     |
```

## Horizontal Rules

```markdown
---
***
___
```

## Task Lists

```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task
```

## Escaping Characters

Use backslash `\` to escape special characters:

```markdown
\* Not italic \*
\# Not a header
\[Not a link\]
```

## HTML in Markdown

You can use HTML tags when needed:

```markdown
<details>
<summary>Click to expand</summary>

Hidden content here

</details>

<kbd>Ctrl</kbd> + <kbd>C</kbd>
```

## Footnotes

```markdown
Here's a sentence with a footnote.[^1]

[^1]: This is the footnote content.
```

## Definition Lists

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

## Common Mistakes to Avoid

### ❌ Wrong: Missing blank lines around code blocks

```markdown
Some text
```python
code here
```
More text
```

### ✅ Correct: Blank lines around code blocks

```markdown
Some text

```python
code here
```

More text
```

### ❌ Wrong: Indented code without language specification

```markdown
Some text:
    def hello():
        print("Hi")
```

### ✅ Correct: Use proper code blocks

```markdown
Some text:

```python
def hello():
    print("Hi")
```
```

### ❌ Wrong: Broken table formatting

```markdown
| Header 1 | Header 2
|----------|----------
| Data | More data
```

### ✅ Correct: Complete table formatting

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Data     | More data|
```

## Best Practices

1. **Always use blank lines** between different elements (paragraphs, code blocks, lists, etc.)
2. **Use language identifiers** for code blocks (python, javascript, bash, etc.)
3. **Keep tables properly aligned** for readability in source
4. **Use consistent list markers** (either `-`, `*`, or `+`, but be consistent)
5. **Test your markdown** in a previewer before committing
6. **Escape special characters** when you want them literal
7. **Use descriptive alt text** for images
8. **Keep lines reasonably short** (80-120 characters) for better diffs

## Markdown Flavors

Different platforms may support different Markdown features:

- **GitHub Flavored Markdown (GFM)**: Supports task lists, tables, strikethrough
- **CommonMark**: Standard specification, widely supported
- **Python-Markdown**: Common for documentation
- **Pandoc**: Extended features for document conversion

## Tools for Markdown

- **VS Code**: Built-in preview (Ctrl+Shift+V)
- **Typora**: WYSIWYG Markdown editor
- **MarkdownLint**: Linting tool for consistent style
- **Pandoc**: Convert between formats
- **grip**: Preview GitHub-flavored markdown locally

## Quick Reference

```markdown
# Headers: # ## ### #### ##### ######
**Bold** *Italic* ***Both***
[Link](url) ![Image](url)
`inline code`

```code block```

- List item
1. Numbered item

| Table | Header |
|-------|--------|
| Data  | Data   |

> Blockquote

---

- [ ] Task
```

---

**Remember**: When in doubt, add blank lines between elements and use proper code block syntax with language identifiers!
