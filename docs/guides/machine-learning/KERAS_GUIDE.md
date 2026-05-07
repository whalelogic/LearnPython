# Keras Guide

Keras is a high-level deep learning API (commonly used via TensorFlow).

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
    layers.Dense(1)
])

model.compile(optimizer="adam", loss="mse")
```

## Common Layers

- Dense (`layers.Dense`)
- Convolution (`layers.Conv2D`)
- Recurrent (`layers.LSTM`, `layers.GRU`)
- Dropout (`layers.Dropout`)
- BatchNorm (`layers.BatchNormalization`)

## Training Workflow

1. Prepare tensors/datasets
2. Define architecture
3. Compile model
4. Fit and validate
5. Save/load model

## Related Docs

- [Keras Documentation](https://keras.io/)
- [Keras Examples](https://keras.io/examples/)

