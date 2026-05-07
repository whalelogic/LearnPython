# NumPy Guide

NumPy provides fast n-dimensional arrays and vectorized numeric computation.

## Install

```bash
pip install numpy
```

## Quick Start

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)        # [5 7 9]
print(a * 2)        # [2 4 6]
print(np.mean(a))   # 2.0
```

## Matrix Operations

```python
m = np.array([[1, 2], [3, 4]])
print(m.shape)              # (2, 2)
print(m.T)                  # transpose
print(np.linalg.inv(m))     # inverse
```

## Best Practices

1. Prefer vectorized ops over Python loops.
2. Understand array shape and broadcasting rules.
3. Use appropriate dtype for speed/memory.
4. Use `np.random.default_rng()` for modern random generation.

## Related Docs

- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)

