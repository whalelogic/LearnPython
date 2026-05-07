# PyTorch Guide

PyTorch is a deep learning framework focused on flexibility and Python-first development.

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

## Typical Workflow

1. Build datasets and dataloaders
2. Define model class inheriting from `torch.nn.Module`
3. Define optimizer and loss
4. Training loop with forward/backward pass
5. Evaluate and save checkpoint

## Minimal Training Skeleton

```python
import torch
import torch.nn as nn

model = nn.Linear(10, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()
```

## Related Docs

- [PyTorch Docs](https://pytorch.org/docs/stable/index.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

