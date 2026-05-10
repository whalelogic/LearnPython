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

## Deep Reference

### Array Memory Model

A NumPy array is a contiguous block of typed memory plus metadata (shape, dtype, strides). Understanding this explains why slices are views (no copy) and why dtype matters for performance.

```python
import numpy as np

a = np.arange(6, dtype=np.float32)
print(a.nbytes)     # 24  (6 elements × 4 bytes each)
print(a.strides)    # (4,) — step 4 bytes to reach the next element

b = a.reshape(2, 3)
print(b.strides)    # (12, 4) — 12 bytes to next row, 4 bytes to next column

# Slices share memory
b[0, 0] = 99
print(a[0])         # 99.0 — a was changed too

# Force a copy when independence is required
c = b.copy()
```

### Vectorization: Replacing Loops

Loops in Python are slow because each iteration has interpreter overhead. NumPy operations run in compiled C and operate on entire arrays at once.

```python
import numpy as np
import time

data = np.random.default_rng(0).standard_normal(1_000_000)

# Slow — Python loop
t0 = time.perf_counter()
result = [x**2 for x in data]
print(f"loop:   {time.perf_counter() - t0:.3f}s")

# Fast — vectorized
t0 = time.perf_counter()
result = data ** 2
print(f"numpy:  {time.perf_counter() - t0:.3f}s")
# NumPy is typically 20–100× faster here
```

**Rule of thumb:** if you are writing a `for` loop over array elements, there is almost always a NumPy operation that replaces it.

### Broadcasting Rules

Two shapes broadcast when, reading dimensions from the right, each pair of values is either equal or one of them is 1.

| Shape A | Shape B | Result | Notes |
|---|---|---|---|
| `(3,)` | `(3,)` | `(3,)` | Same shape — no broadcast |
| `(1, 3)` | `(2, 1)` | `(2, 3)` | Both dimensions broadcast |
| `(4, 3)` | `(3,)` | `(4, 3)` | B treated as `(1, 3)` |
| `(4, 3)` | `(4, 1)` | `(4, 3)` | B column repeated 3 times |
| `(4, 3)` | `(4,)` | Error | Trailing dims `3 ≠ 4` |

```python
prices  = np.array([10, 20, 30])          # shape (3,)
weights = np.array([[0.5], [0.25]])       # shape (2, 1)
print(prices * weights)
# [[  5.  10.  15.]
#  [  2.5  5.   7.5]]    — result shape (2, 3)
```

### Indexing Patterns

```python
a = np.arange(20).reshape(4, 5)

# Basic slicing (returns a view)
a[1, :]          # entire row 1
a[:, 2]          # entire column 2
a[1:3, 0:2]      # sub-matrix

# Boolean masking (returns a copy)
a[a > 10]        # flat array of values > 10
a[(a % 2) == 0]  # even values

# Fancy indexing (returns a copy)
a[[0, 3], :]     # rows 0 and 3
a[:, [1, 4]]     # columns 1 and 4

# np.where — conditional replacement
np.where(a > 10, a, 0)   # keep value if > 10, else 0
```

### Array Creation Quick-Reference

| Function | Purpose | Example |
|---|---|---|
| `np.array(data, dtype=)` | From Python list or nested list | `np.array([[1, 2], [3, 4]], dtype=float)` |
| `np.zeros(shape)` | All-zero array | `np.zeros((3, 4))` |
| `np.ones(shape)` | All-one array | `np.ones((2, 2))` |
| `np.full(shape, val)` | All same value | `np.full((3,), 7)` |
| `np.eye(n)` | Identity matrix | `np.eye(4)` |
| `np.arange(start, stop, step)` | Evenly spaced integers | `np.arange(0, 10, 2)` |
| `np.linspace(start, stop, n)` | `n` evenly spaced floats (inclusive) | `np.linspace(0.0, 1.0, 5)` |
| `np.random.default_rng(seed).standard_normal(shape)` | N(0,1) random floats | `rng.standard_normal((100, 4))` |
| `np.loadtxt(file, delimiter=)` | Load plain-text numeric file | `np.loadtxt("data.csv", delimiter=",")` |
| `np.load(file)` | Load `.npy` binary | `np.load("array.npy")` |
| `np.concatenate([a, b], axis=)` | Join existing arrays | `np.concatenate([a, b], axis=0)` |

### Aggregation and Math Quick-Reference

| Function | Description | Axis note |
|---|---|---|
| `np.sum(a, axis=)` | Sum | `axis=0` collapses rows; `axis=1` collapses columns |
| `np.mean(a, axis=)` | Arithmetic mean | Same axis convention |
| `np.std(a, axis=)` | Standard deviation | `ddof=1` for sample std |
| `np.min(a)` / `np.max(a)` | Global min/max | |
| `np.argmin(a)` / `np.argmax(a)` | Index of min/max | |
| `np.cumsum(a)` | Cumulative sum | |
| `np.diff(a)` | First differences | |
| `np.clip(a, lo, hi)` | Clamp values | |
| `np.where(cond, x, y)` | Element-wise conditional | |
| `np.unique(a)` | Sorted unique values | |
| `np.dot(a, b)` / `a @ b` | Dot / matrix product | |
| `np.linalg.norm(a)` | Euclidean norm | |
| `np.linalg.inv(a)` | Matrix inverse | |
| `np.linalg.eig(a)` | Eigenvalues and eigenvectors | |

### NaN-Safe Variants

Always prefer the `nan*` family when data may contain missing values:

| Unsafe | NaN-safe |
|---|---|
| `np.mean(a)` | `np.nanmean(a)` |
| `np.sum(a)` | `np.nansum(a)` |
| `np.min(a)` | `np.nanmin(a)` |
| `np.max(a)` | `np.nanmax(a)` |
| `np.std(a)` | `np.nanstd(a)` |

### Integration with the Python Ecosystem

| NumPy pairs with | Bridge |
|---|---|
| `pandas` | `df["col"].to_numpy()` / `pd.DataFrame(arr, columns=[...])` |
| `matplotlib` | `plt.plot(x, np.sin(x))` — arrays plug in directly |
| `scikit-learn` | Models expect 2-D float arrays: `X.reshape(-1, 1)` |
| `scipy` | `from scipy import stats; stats.ttest_ind(a, b)` |
| `Pillow` | `np.array(Image.open("img.png"))` → `(H, W, 3)` uint8 |
| Python built-ins | `len(arr)` returns first dim; prefer `arr.shape[0]` for clarity |

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Create arrays from lists, index rows/columns, call `np.mean` and `np.sum` |
| **Developing** | Reshape arrays, apply broadcasting, use boolean masking and `np.where` |
| **Proficient** | Handle dtype/shape mismatches, chain transforms without loops, use NaN-safe aggregation |
| **Advanced** | Write fully vectorized pipelines, use `np.linalg`, reason about views vs copies and memory layout |

### Suggested Practice Projects

1. **Normalize a matrix** — Given a 2-D score matrix, subtract the column mean and divide by the column std. Verify result has zero mean and unit std per column.
2. **Moving average** — Compute a 3-period moving average over a 1-D price array without any Python loops.
3. **Boolean masking pipeline** — Filter rows where column A exceeds a threshold, then compute the mean of column B — no loop.
4. **Image as array** — Load a grayscale PNG, flip it horizontally with `[:, ::-1]`, compute the mean pixel value, and save back.
5. **Matrix operations** — Build two random matrices, multiply with `@`, compute the transpose, and verify `(A @ B).T == B.T @ A.T`.

### Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| View vs copy | Slices share memory; modifying a slice modifies the original | Use `.copy()` when independence is required |
| Integer dtype truncation | `np.array([1, 2]) / 3` gives `[0, 0]` in some contexts | Use float literals or `dtype=float` |
| `np.sum` vs `sum` | Python `sum` is 10–100× slower on large arrays | Always use `np.sum` on NumPy arrays |
| Shape `(n,)` vs `(n,1)` | Broadcasting treats 1-D and 2-D column vectors differently | Use `.reshape(-1, 1)` for a column vector |
| NaN propagation | `np.mean` returns `NaN` if any element is `NaN` | Use `np.nanmean`, `np.nansum`, etc. |
| In-place ops on views | `a[:] *= 2` modifies the source | Be deliberate about in-place vs new-array operations |

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

