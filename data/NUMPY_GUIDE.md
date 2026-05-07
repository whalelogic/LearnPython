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
