# PyTorch Guide

PyTorch is a deep learning framework known for its Python-first style and flexible training loops.

## Install

```bash
pip install torch torchvision torchaudio
```

## Quick Start

```python
import torch

x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(torch.sum(x))
```

## Minimal Training Skeleton

```python
import torch
import torch.nn as nn

model = nn.Linear(10, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()
```

## Why People Choose PyTorch

PyTorch makes it easy to inspect tensors, write custom training loops, and debug model code using familiar Python flow.

## Related Reading

- [TENSORFLOW_GUIDE.md](TENSORFLOW_GUIDE.md)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
