# Keras Guide

Keras is a high-level API for building neural networks with readable, composable code.

## Install

```bash
pip install keras tensorflow
```

## Quick Start

```python
import keras
from keras import layers

model = keras.Sequential([
    layers.Dense(64, activation="relu"),
    layers.Dense(1),
])

model.compile(optimizer="adam", loss="mse")
```

## Why Learners Like Keras

Keras keeps the training workflow compact:

1. Define layers
2. Compile with optimizer and loss
3. Train with `fit()`
4. Evaluate and save

## Common Layer Types

- Dense layers for tabular or flattened input
- Convolution layers for images
- Recurrent layers for sequences
- Dropout and normalization layers for regularization and stability

## Related Reading

- [TENSORFLOW_GUIDE.md](TENSORFLOW_GUIDE.md)
- [Keras Documentation](https://keras.io/)
