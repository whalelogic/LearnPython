# Pandas Guide

Pandas is the core Python library for tabular data analysis.

## Install

```bash
pip install pandas
```

## Core Structures

- `Series`: 1D labeled array.
- `DataFrame`: 2D labeled table.

## Quick Start

```python
import pandas as pd

# Load CSV
df = pd.read_csv("sales.csv")

# Inspect
print(df.head())
print(df.info())
print(df.describe())

# Select
revenue = df["revenue"]
subset = df[["date", "revenue"]]

# Filter
high = df[df["revenue"] > 1000]

# Group and aggregate
summary = df.groupby("region", as_index=False)["revenue"].sum()
```

## Common Tasks

1. Missing data handling: `dropna()`, `fillna()`
2. Type conversion: `astype()`, `to_datetime()`
3. Merge/join: `merge()`, `join()`
4. Pivoting: `pivot_table()`
5. Export: `to_csv()`, `to_parquet()`

## Best Practices

- Keep columns typed correctly early.
- Use vectorized operations over loops.
- Use `loc`/`iloc` for explicit indexing.
- Check memory usage on large datasets.

## Related Docs

- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

