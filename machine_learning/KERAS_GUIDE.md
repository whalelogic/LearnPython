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

---

## Deep Reference

### Keras Workflow at a Glance

Every Keras model follows the same four-step pattern. Understand each step before customizing any of them.

```
Define layers → compile → fit → evaluate / predict
```

```python
import keras
from keras import layers
import numpy as np

# 1. Define layers
model = keras.Sequential([
    layers.Input(shape=(20,)),
    layers.Dense(64, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(32, activation="relu"),
    layers.Dense(1, activation="sigmoid"),  # binary output
])

# 2. Compile — pick optimizer, loss, and metrics
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

# 3. Train
X_train = np.random.rand(1000, 20).astype("float32")
y_train = np.random.randint(0, 2, size=(1000,)).astype("float32")

history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    verbose=1,
)

# 4. Evaluate and predict
X_test = np.random.rand(200, 20).astype("float32")
y_test = np.random.randint(0, 2, size=(200,)).astype("float32")
loss, acc = model.evaluate(X_test, y_test)
preds = model.predict(X_test)   # probabilities
```

### Layer Types Quick-Reference

| Layer | Purpose | Key arguments |
|---|---|---|
| `Dense(units, activation=)` | Fully connected layer | `units`, `activation`, `kernel_regularizer` |
| `Conv2D(filters, kernel_size, activation=)` | 2-D convolution for images | `filters`, `kernel_size`, `strides`, `padding` |
| `MaxPooling2D(pool_size=)` | Spatial downsampling | `pool_size`, `strides` |
| `LSTM(units, return_sequences=)` | Long short-term memory for sequences | `units`, `return_sequences`, `dropout` |
| `GRU(units)` | Gated recurrent unit (lighter than LSTM) | `units`, `return_sequences` |
| `Embedding(vocab_size, embed_dim)` | Integer tokens → dense vectors | `input_dim`, `output_dim`, `mask_zero` |
| `Flatten()` | Collapse spatial dims to 1-D | — |
| `Dropout(rate)` | Zero random fraction of activations during training | `rate` (0–1) |
| `BatchNormalization()` | Normalize activations per batch | `momentum`, `epsilon` |
| `GlobalAveragePooling2D()` | Average each feature map to one value | — |

### Loss Functions Reference

| Task | Loss function | Output activation |
|---|---|---|
| Binary classification | `binary_crossentropy` | `sigmoid` |
| Multi-class (one label) | `sparse_categorical_crossentropy` | `softmax` |
| Multi-class (one-hot labels) | `categorical_crossentropy` | `softmax` |
| Multi-label classification | `binary_crossentropy` | `sigmoid` |
| Regression | `mean_squared_error` | None (linear) |
| Regression (outlier-robust) | `huber` | None (linear) |

### Optimizer Quick-Reference

| Optimizer | When to use |
|---|---|
| `Adam(lr=1e-3)` | Good default for most tasks |
| `SGD(lr=0.01, momentum=0.9)` | Better generalization with tuned schedule |
| `RMSprop(lr=1e-3)` | Recurrent networks |
| `AdamW(lr=1e-3, weight_decay=1e-4)` | Adam with L2 regularization built in |

### Callbacks

Callbacks hook into the training loop to add behavior without changing `fit()`.

```python
callbacks = [
    # Stop early when val_loss stops improving
    keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=3, restore_best_weights=True
    ),
    # Save the best checkpoint
    keras.callbacks.ModelCheckpoint(
        "best_model.keras", monitor="val_loss", save_best_only=True
    ),
    # Reduce LR when plateau
    keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss", factor=0.5, patience=2
    ),
]

history = model.fit(X_train, y_train, epochs=50, callbacks=callbacks)
```

### Functional API — Multi-Input / Multi-Output Models

Use the functional API when you need shared layers, skip connections, or multiple inputs.

```python
# Shared embedding for two text inputs
input_a = keras.Input(shape=(100,), name="text_a")
input_b = keras.Input(shape=(100,), name="text_b")

shared = layers.Embedding(10000, 64)
a = shared(input_a)
b = shared(input_b)

merged = layers.Concatenate()([a, b])
flat = layers.Flatten()(merged)
out = layers.Dense(1, activation="sigmoid")(flat)

model = keras.Model(inputs=[input_a, input_b], outputs=out)
```

### Saving and Loading

```python
# Recommended: native Keras format
model.save("my_model.keras")
loaded = keras.models.load_model("my_model.keras")

# Weights only (architecture defined separately)
model.save_weights("weights.h5")
model.load_weights("weights.h5")

# Export for TensorFlow Serving or TFLite
model.export("saved_model_dir")
```

### Inspecting Training History

```python
import matplotlib.pyplot as plt

plt.plot(history.history["loss"],     label="train loss")
plt.plot(history.history["val_loss"], label="val loss")
plt.legend()
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()
```

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Build a `Sequential` model, compile, call `fit` and `evaluate` |
| **Developing** | Choose correct loss/activation pair, add `Dropout`/`BatchNorm`, read training history |
| **Proficient** | Use callbacks for early stopping, use the functional API, save and reload models |
| **Advanced** | Write custom layers and losses, design multi-input architectures, tune hyperparameters systematically |

### Suggested Practice Projects

1. **Binary classifier** — Classify tabular data (e.g., UCI Heart Disease) with a `Sequential` model; tune depth and dropout.
2. **Image classifier** — Build a CNN for MNIST or CIFAR-10 using `Conv2D`, `MaxPooling2D`, and `Flatten`.
3. **Sentiment analysis** — Use `Embedding` + `LSTM` on the IMDB dataset bundled in `keras.datasets`.
4. **Regression** — Predict a continuous target (e.g., Boston housing) and compare MSE vs Huber loss.
5. **Transfer learning** — Load `keras.applications.MobileNetV2`, freeze base layers, attach a new head, fine-tune.

### Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Wrong activation for loss | Using `relu` output with `binary_crossentropy` gives garbage | Match activation to loss as shown in the table above |
| Forgetting `validation_split` | Training loss looks great but you have no signal on generalization | Always pass `validation_split` or a validation set |
| Input shape mismatch | First `Dense` infers shape from data; adding `Input(shape=)` makes errors earlier | Declare an explicit `Input` layer |
| `predict` returns probabilities | For classification, `predict` gives probabilities, not class labels | Apply `(preds > 0.5).astype(int)` or `np.argmax(preds, axis=1)` |
| Training on GPU but saving floats | Mixed-precision training can cause weight dtype issues | Set policy explicitly with `keras.mixed_precision.set_global_policy` |

