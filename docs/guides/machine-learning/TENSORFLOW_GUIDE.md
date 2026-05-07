# TensorFlow Guide

TensorFlow is a platform for machine learning workflows from research to production.

## Install

```bash
pip install tensorflow
```

## Core Concepts

- Tensors: multi-dimensional arrays
- Graph execution with eager mode default
- `tf.data` for scalable input pipelines
- `tf.keras` for high-level model APIs

## Minimal Example

```python
import tensorflow as tf

x = tf.constant([[1.0, 2.0], [3.0, 4.0]])
print(tf.reduce_sum(x))
```

## Typical Workflow

1. Prepare input data (`tf.data.Dataset`)
2. Build model (`tf.keras.Sequential` or subclassing)
3. Compile (`optimizer`, `loss`, `metrics`)
4. Train (`model.fit`)
5. Evaluate and export (`model.evaluate`, `model.save`)

## Related Docs

- [TensorFlow Guide](https://www.tensorflow.org/guide)
- [TensorFlow API](https://www.tensorflow.org/api_docs)

