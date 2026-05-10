# TensorFlow Guide

TensorFlow is a machine learning platform that works from experimentation through production deployment.

## Install

```bash
pip install tensorflow
```

## Core Ideas

- Tensors are multi-dimensional arrays
- `tf.data` builds input pipelines
- `tf.keras` provides high-level model building
- Eager execution makes code feel more Pythonic while still supporting optimized execution

## Minimal Example

```python
import tensorflow as tf

x = tf.constant([[1.0, 2.0], [3.0, 4.0]])
print(tf.reduce_sum(x))
```

## Small Training Workflow

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(1),
])

model.compile(optimizer="adam", loss="mse")
```

## When TensorFlow Fits Well

TensorFlow is a good choice when you want a mature ecosystem, deployment tooling, and strong support for production workflows.

## Related Reading

- [KERAS_GUIDE.md](KERAS_GUIDE.md)
- [TensorFlow Guide](https://www.tensorflow.org/guide)

---

## TensorFlow Deep-Dive Reference

### Tensor shapes and dtypes

Always check both shape and dtype before debugging math issues.

```python
import tensorflow as tf

x = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
print(x.shape)   # (2, 2)
print(x.dtype)   # float32
```

Common pitfalls:

- mixing `float32` and `float64`
- forgetting batch dimension
- incorrect rank after reshape/squeeze

### Eager mode vs graph execution

- Eager mode: immediate execution, easier debugging.
- `@tf.function`: traces Python into optimized graph functions.

Use eager for development clarity; add graph tracing when performance matters.

```python
@tf.function
def step(x):
    return x * 2
```

### `tf.data` pipeline basics

```python
import tensorflow as tf

features = tf.constant([[1.0], [2.0], [3.0], [4.0]])
labels = tf.constant([[2.0], [4.0], [6.0], [8.0]])

dataset = tf.data.Dataset.from_tensor_slices((features, labels))
dataset = dataset.shuffle(4).batch(2).prefetch(tf.data.AUTOTUNE)
```

Pipeline checklist:

- shuffle training data
- batch consistently
- prefetch for throughput
- cache if dataset fits memory

### Compile / fit / evaluate flow

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(1),
])

model.compile(optimizer="adam", loss="mse", metrics=["mae"])
history = model.fit(dataset, epochs=5, verbose=0)
metrics = model.evaluate(dataset, verbose=0)
print(metrics)
```

### Overfitting controls

Use these tools early:

- validation split/dataset
- dropout layers
- L2 regularization
- early stopping callback

```python
callbacks = [
    tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=3, restore_best_weights=True)
]
```

### Saving and loading models

```python
model.save("model.keras")
loaded = tf.keras.models.load_model("model.keras")
```

Save format guidance:

- use `.keras` for native Keras model format
- version model artifacts with metadata
- keep preprocessing steps documented

### Inference checklist

Before deploying inference code, verify:

- input schema matches training schema
- normalization is identical to training
- output decoding is documented
- latency is measured on realistic input sizes

### Debugging workflow for TensorFlow

1. Print sample batch shapes.
2. Confirm loss decreases across epochs.
3. Check for NaNs in inputs/gradients.
4. Reduce model size to isolate instability.
5. Compare against a tiny synthetic dataset.

### TensorFlow + ecosystem notes

- Keras gives concise model APIs.
- NumPy interop is straightforward.
- TensorBoard helps track training metrics.
- SavedModel / `.keras` formats support serving workflows.

### Practice tasks

1. Train a tiny regression model on synthetic data.
2. Add validation metrics and early stopping.
3. Add model save/load round trip test.
4. Replace in-memory arrays with `tf.data` pipeline.
5. Compare two optimizers and record results.

### Self-check questions

- Can you explain each tensor shape in your pipeline?
- Do you know why chosen loss/metric fits the task?
- Is preprocessing consistent between train and inference?
- Can you recover cleanly from training instability?
- Is your model artifact reproducible?

### Related Reading

- [KERAS_GUIDE.md](KERAS_GUIDE.md)
- [PYTORCH_GUIDE.md](PYTORCH_GUIDE.md)
- [../data/NUMPY_GUIDE.md](../data/NUMPY_GUIDE.md)
