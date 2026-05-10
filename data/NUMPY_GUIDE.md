# NumPy Guide

NumPy provides fast multidimensional arrays and the vectorized operations that power much of the scientific Python ecosystem.

## Install

```bash
pip install numpy
```

## Quick Start

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * 2)
print(np.mean(a))
```

## Shapes Matter

```python
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix.shape)
print(matrix[:, 0])
```

Understanding shape helps you predict whether operations happen element by element, row by row, or fail with a broadcasting error.

## Real-World Example

```python
sales = np.array([120.0, 99.5, 140.0, 110.0])
centered = sales - sales.mean()
print(centered)
```

This kind of vectorized transformation is what makes NumPy powerful.

## Best Practices

- Prefer array operations over Python loops
- Be explicit about dtype when memory or precision matters
- Use `np.random.default_rng()` for random generation in new code
- Convert to Pandas when labels and table operations matter more than raw arrays

## Related Reading

- [PANDAS_GUIDE.md](PANDAS_GUIDE.md)
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)

---

## Extended Study Workbook

This extension turns the page into a longer reference you can repeatedly revisit while practicing.

### 1) Learning Goals

By the end of this topic, you should be able to:

- Explain the core vocabulary in plain language.
- Identify when this topic is a good fit for a real task.
- Recognize common beginner mistakes before they happen.
- Debug basic issues without guessing.
- Compose this topic with related Python tools and modules.

### 2) Mental Model

Use this short mental model while reading examples:

1. **Input** — What data or request enters the code?
2. **Transformation** — What operation changes the data?
3. **Output** — What value, file, response, or effect is produced?
4. **Failure modes** — What can go wrong?
5. **Validation** — How do you check correctness quickly?

If you cannot explain all five parts, pause and simplify the example.

### 3) Terminology Drill

Review these terms and define each in your own words:

- value
- expression
- statement
- iterable
- exception
- state
- side effect
- dependency
- serialization
- validation

A useful habit is to write one sentence per term plus one concrete example.

### 4) Practical Checklist

When implementing this topic in a project, verify:

- Inputs are validated early.
- Variable names are explicit.
- Error handling exists for expected failures.
- Edge cases are covered.
- Output format is predictable.
- The code is readable after one week away.
- The solution is tested with both normal and strange input.
- Logging/print statements are meaningful during debugging.
- Temporary experimentation code is removed before sharing.
- You documented assumptions.

### 5) Common Mistakes and Corrections

- **Mistake:** Copying code without understanding data flow.
  - **Fix:** Trace one sample input by hand.
- **Mistake:** Ignoring type/shape/format assumptions.
  - **Fix:** Print and assert assumptions early.
- **Mistake:** Overcomplicating the first version.
  - **Fix:** Build a tiny working baseline first.
- **Mistake:** Mixing setup and business logic.
  - **Fix:** Separate configuration from core operations.
- **Mistake:** Not handling empty input.
  - **Fix:** Add a guard path and test it.

### 6) Debugging Workflow

Follow this process when something breaks:

1. Reproduce the issue with the smallest possible input.
2. Confirm what output you expected.
3. Add narrow debug prints or assertions.
4. Check boundary values and optional fields.
5. Verify external dependencies and environment assumptions.
6. Fix one thing at a time.
7. Re-run the exact failing scenario.
8. Keep a short note about root cause.

### 7) Mini Exercises

Try these short tasks:

1. Rewrite one example using clearer variable names.
2. Add one intentional edge case and handle it gracefully.
3. Add a small validation function for input checks.
4. Convert one example into a reusable function.
5. Produce a tiny test table with three normal cases and three edge cases.
6. Explain one example to a beginner in five sentences.
7. Refactor duplicated lines into a helper.
8. Add a failure path with a clear error message.
9. Measure behavior with larger input and note observations.
10. Compare two approaches and justify your final choice.

### 8) Integration Notes

NumPy is the foundation layer for nearly all scientific Python. Understanding how it connects to neighboring tools prevents the most common integration mistakes.

| NumPy pairs with | Why | Bridge example |
|---|---|---|
| `pandas` | DataFrame columns are NumPy arrays under the hood | `df["col"].to_numpy()` |
| `matplotlib` | Plot functions accept NumPy arrays directly | `plt.plot(x, np.sin(x))` |
| `scikit-learn` | Models expect 2-D NumPy input | `X = data.reshape(-1, 1)` |
| `scipy` | Extends NumPy with stats, linalg, and signal processing | `from scipy import stats` |
| `Pillow` | Images become `(H, W, 3)` uint8 arrays | `np.array(Image.open("img.png"))` |
| Python built-ins | `len`, `sum`, `min`, `max` work but are slower | Prefer `arr.sum()`, `arr.min()` |

**Broadcasting rules — when shapes combine automatically:**

Two shapes are compatible when dimensions are equal, or one of them is 1. NumPy stretches the size-1 dimension across the other.

```python
import numpy as np

a = np.array([[1, 2, 3]])   # shape (1, 3)
b = np.array([[10], [20]])  # shape (2, 1)
print(a + b)
# [[11 12 13]
#  [21 22 23]]   — broadcasts to (2, 3)
```

**Loading from common sources:**

```python
# From CSV (no header row)
data = np.loadtxt("scores.csv", delimiter=",")

# From pandas (when labels are not needed)
import pandas as pd
arr = pd.read_csv("scores.csv").to_numpy()

# Save and reload efficiently
np.save("data.npy", arr)
arr2 = np.load("data.npy")
```

### 9) NumPy API Quick-Reference

#### Array creation

| Function | Purpose | Example |
|---|---|---|
| `np.array(data, dtype=)` | Create from list or nested list | `np.array([1, 2, 3], dtype=float)` |
| `np.zeros(shape)` | All-zero array | `np.zeros((3, 4))` |
| `np.ones(shape)` | All-one array | `np.ones((2, 2))` |
| `np.arange(start, stop, step)` | Evenly spaced integers | `np.arange(0, 10, 2)` |
| `np.linspace(start, stop, n)` | `n` evenly spaced floats including endpoints | `np.linspace(0, 1, 5)` |
| `np.eye(n)` | Identity matrix | `np.eye(3)` |
| `np.full(shape, fill_value)` | Array filled with one value | `np.full((2, 3), 7)` |
| `np.random.default_rng(seed).standard_normal(shape)` | Random floats from N(0,1) | `rng.standard_normal((4, 4))` |
| `np.loadtxt(file, delimiter=)` | Load from text file | — |
| `np.load(file)` | Load `.npy` binary file | — |

#### Array inspection

| Attribute / Method | What it tells you |
|---|---|
| `arr.shape` | Tuple of dimension sizes |
| `arr.dtype` | Element data type (`float64`, `int32`, …) |
| `arr.ndim` | Number of axes |
| `arr.size` | Total element count |
| `arr.itemsize` | Bytes per element |
| `arr.nbytes` | Total memory usage in bytes |

#### Reshaping, slicing, and joining

```python
a = np.arange(12)
grid = a.reshape(3, 4)         # view — shares memory with a
col1 = grid[:, 1]              # second column (all rows)
block = grid[0:2, 1:3]        # 2×2 sub-block
flat = grid.ravel()            # 1-D view (no copy if possible)
col_vec = a.reshape(-1, 1)     # shape (12, 1) — column vector

np.concatenate([grid, grid], axis=0)   # stack rows → (6, 4)
np.stack([a, a], axis=0)              # new axis → (2, 12)
np.hstack([grid, grid])               # side by side → (3, 8)
np.vstack([grid, grid])               # top to bottom → (6, 4)
```

#### Math and aggregation

| Function | Description |
|---|---|
| `np.sum(a, axis=0)` | Sum along rows (collapse rows, keep columns) |
| `np.mean(a, axis=1)` | Mean along columns |
| `np.std(a)` / `np.var(a)` | Standard deviation / variance |
| `np.min(a)` / `np.max(a)` | Global min / max |
| `np.argmin(a)` / `np.argmax(a)` | Index of min / max |
| `np.dot(a, b)` or `a @ b` | Dot / matrix product |
| `np.linalg.norm(a)` | Euclidean norm |
| `np.clip(a, lo, hi)` | Clamp values to `[lo, hi]` |
| `np.where(cond, x, y)` | Element-wise conditional select |
| `np.unique(a)` | Sorted unique values |
| `np.cumsum(a)` | Cumulative sum |
| `np.diff(a)` | First-order differences |

#### NaN-safe variants

| Unsafe | NaN-safe |
|---|---|
| `np.mean(a)` | `np.nanmean(a)` |
| `np.sum(a)` | `np.nansum(a)` |
| `np.min(a)` | `np.nanmin(a)` |
| `np.std(a)` | `np.nanstd(a)` |

### 10) Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Create arrays from lists, index rows/columns, call `np.mean` and `np.sum` |
| **Developing** | Reshape arrays, understand broadcasting rules, use boolean masking, use `np.where` |
| **Proficient** | Handle dtype and shape mismatches, chain transforms without loops, use NaN-safe aggregation |
| **Advanced** | Write fully vectorized pipelines, use `np.linalg`, integrate with pandas/scikit-learn, reason about memory layout and views vs copies |

### 11) Suggested Practice Projects

1. **Normalize a dataset** — Given a 2-D score matrix, subtract the column mean and divide by the column standard deviation. Verify the result has zero mean and unit std per column.
2. **Image manipulation** — Load a grayscale image with `matplotlib.image.imread`, crop it by slicing, flip it horizontally with `[:, ::-1]`, and compute the mean pixel value.
3. **Moving average** — Compute a 3-period moving average over a 1-D price array without any Python loops (hint: use slicing and addition).
4. **Boolean masking pipeline** — Filter rows where a column value is above a threshold and compute the mean of another column — entirely without a loop.
5. **Matrix operations** — Create two random matrices, multiply them with `@`, compute the transpose, and verify that `(A @ B).T == B.T @ A.T`.

### 12) Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| View vs copy | Slices return views; modifying a slice modifies the original | Use `.copy()` when you need an independent array |
| Integer dtype truncation | `np.array([1, 2]) / 3` returns `[0, 0]` in older NumPy | Use float literals or `dtype=float` |
| `np.sum` vs `sum` | Python `sum` is 10–100× slower on large arrays | Always use `np.sum` on NumPy arrays |
| Shape `(n,)` vs `(n,1)` | Broadcasting treats 1-D and 2-D very differently | Use `.reshape(-1, 1)` when you need a column vector |
| NaN silently corrupts | `np.mean` returns `NaN` if any element is `NaN` | Use `np.nanmean`, `np.nansum`, and friends |
| In-place ops on views | `a[:] *= 2` modifies the source array | Be deliberate about in-place vs new-array operations |

