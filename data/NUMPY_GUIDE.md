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


