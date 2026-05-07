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
