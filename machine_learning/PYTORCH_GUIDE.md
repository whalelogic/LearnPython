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

---

## Deep Reference

### Tensors and Autograd

A `torch.Tensor` is PyTorch's core data type — a typed multi-dimensional array that optionally tracks gradients.

```python
import torch

# Create tensors
x = torch.tensor([1.0, 2.0, 3.0])          # from Python list
z = torch.zeros(3, 4)                        # 3×4 zero matrix
r = torch.randn(2, 3)                        # standard normal

# Gradient tracking
w = torch.tensor([[1.0, 2.0]], requires_grad=True)
loss = (w ** 2).sum()
loss.backward()
print(w.grad)    # tensor([[2., 4.]])  — d(loss)/dw

# No gradient needed at inference time
with torch.no_grad():
    out = w * 3
```

### Tensor Operations Quick-Reference

| Operation | Syntax | Notes |
|---|---|---|
| Shape | `t.shape` / `t.size()` | Returns `torch.Size` |
| Dtype | `t.dtype` | e.g. `torch.float32` |
| Device | `t.device` | `cpu` or `cuda:0` |
| Move to GPU | `t.to("cuda")` | Returns new tensor |
| Reshape | `t.reshape(2, -1)` | `-1` infers dimension |
| Flatten | `t.flatten()` | |
| Transpose | `t.T` / `t.transpose(0, 1)` | |
| Matrix multiply | `a @ b` / `torch.matmul(a, b)` | |
| Element-wise multiply | `a * b` | Broadcasts like NumPy |
| Concatenate | `torch.cat([a, b], dim=0)` | Stack along existing dim |
| Stack | `torch.stack([a, b], dim=0)` | New dimension |
| Mean | `t.mean()` / `t.mean(dim=0)` | |
| Convert to NumPy | `t.detach().cpu().numpy()` | Must detach if `requires_grad` |
| Convert from NumPy | `torch.from_numpy(arr)` | Shares memory |

### Building a Model with `nn.Module`

```python
import torch.nn as nn
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(self, in_features, hidden, out_features):
        super().__init__()
        self.fc1 = nn.Linear(in_features, hidden)
        self.dropout = nn.Dropout(0.3)
        self.fc2 = nn.Linear(hidden, out_features)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        return self.fc2(x)

model = MLP(in_features=20, hidden=64, out_features=1)
print(model)
print(sum(p.numel() for p in model.parameters()), "parameters")
```

### Layer Types Quick-Reference

| Layer | Purpose |
|---|---|
| `nn.Linear(in, out)` | Fully connected |
| `nn.Conv2d(in_ch, out_ch, kernel)` | 2-D convolution |
| `nn.MaxPool2d(kernel)` | Spatial downsampling |
| `nn.LSTM(input_size, hidden, layers)` | Long short-term memory |
| `nn.GRU(input_size, hidden)` | Gated recurrent unit |
| `nn.Embedding(vocab, dim)` | Integer tokens → dense vectors |
| `nn.Dropout(p)` | Zero `p` fraction of activations |
| `nn.BatchNorm1d(num_features)` | Batch normalization |
| `nn.LayerNorm(normalized_shape)` | Layer normalization |
| `nn.Sequential(*layers)` | Simple chain |

### Full Training Loop

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

# Fake data
X = torch.randn(1000, 20)
y = (X[:, 0] > 0).float().unsqueeze(1)

dataset = TensorDataset(X, y)
loader  = DataLoader(dataset, batch_size=32, shuffle=True)

model     = MLP(20, 64, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.BCEWithLogitsLoss()

for epoch in range(10):
    model.train()
    total_loss = 0.0
    for X_batch, y_batch in loader:
        optimizer.zero_grad()
        logits = model(X_batch)
        loss   = criterion(logits, y_batch)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1:02d}  loss={total_loss/len(loader):.4f}")

# Evaluation
model.eval()
with torch.no_grad():
    preds = torch.sigmoid(model(X)).squeeze()
    acc   = ((preds > 0.5) == y.squeeze().bool()).float().mean()
    print(f"Accuracy: {acc:.3f}")
```

### Loss Functions Reference

| Task | Loss | Notes |
|---|---|---|
| Binary classification (logits) | `nn.BCEWithLogitsLoss()` | Numerically stable; no sigmoid needed |
| Multi-class (class indices) | `nn.CrossEntropyLoss()` | Combines `LogSoftmax` + `NLLLoss` |
| Regression | `nn.MSELoss()` | |
| Regression (outlier-robust) | `nn.HuberLoss(delta=1.0)` | |
| Multi-label | `nn.BCEWithLogitsLoss()` | Apply sigmoid per label at inference |

### Optimizer Quick-Reference

| Optimizer | Key args | When to use |
|---|---|---|
| `torch.optim.Adam` | `lr=1e-3`, `weight_decay=0` | Good default |
| `torch.optim.AdamW` | `lr=1e-3`, `weight_decay=1e-2` | Adam with proper weight decay (preferred) |
| `torch.optim.SGD` | `lr=0.01`, `momentum=0.9` | Large-batch training, fine-tuning |
| `torch.optim.RMSprop` | `lr=1e-3` | Recurrent networks |

### Saving and Loading

```python
# Save model weights (recommended)
torch.save(model.state_dict(), "model.pt")

# Load
model2 = MLP(20, 64, 1)
model2.load_state_dict(torch.load("model.pt", weights_only=True))
model2.eval()

# Save entire model (fragile across code changes)
torch.save(model, "full_model.pt")
```

### Moving to GPU

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
model  = model.to(device)

for X_batch, y_batch in loader:
    X_batch = X_batch.to(device)
    y_batch = y_batch.to(device)
    ...
```

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Create tensors, run the training loop skeleton, compute a forward pass |
| **Developing** | Write an `nn.Module`, use `DataLoader`, evaluate with `torch.no_grad()` |
| **Proficient** | Track gradients correctly, choose loss/optimizer, save and load checkpoints |
| **Advanced** | Write custom layers and loss functions, use LR schedulers, profile and optimize memory |

### Suggested Practice Projects

1. **Binary classifier** — Train an MLP on synthetic or tabular data; plot training loss.
2. **Image classifier** — Build a CNN for MNIST using `Conv2d` and `MaxPool2d`.
3. **Sequence model** — Use an `LSTM` to predict the next character in a text string.
4. **Regression** — Predict housing prices with `MSELoss`; compare Adam vs SGD convergence speed.
5. **Transfer learning** — Load a pretrained `torchvision.models.resnet18`, freeze all layers except the final `fc`, fine-tune on a small image dataset.

### Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Forgetting `optimizer.zero_grad()` | Gradients accumulate across batches by default | Call `zero_grad()` at the start of each batch |
| `model.train()` / `model.eval()` | Dropout and BatchNorm behave differently in train vs eval mode | Switch modes explicitly |
| In-place operations on leaf tensors | `w += 1` on a `requires_grad` tensor raises an error | Use `w = w + 1` |
| `loss.item()` vs `loss` | Keeping `loss` in a list holds the whole compute graph in memory | Always call `.item()` to extract a plain float |
| Shape mismatch in loss | `BCEWithLogitsLoss` expects `(N, 1)` target to match `(N, 1)` output | Use `.unsqueeze(1)` on 1-D targets |
| CPU/GPU tensor mismatch | Adding a CPU tensor to a GPU tensor raises a RuntimeError | Move all tensors to the same device before operations |

