# Pandas Guide

Pandas is the go-to library for tabular data in Python. It helps you clean messy files, reshape tables, group records, and prepare data for reports or machine learning.

## Install

```bash
pip install pandas
```

## Core Objects

- `Series` — one labeled column of data
- `DataFrame` — a full table with rows and columns

## Quick Start

```python
import pandas as pd

df = pd.DataFrame(
    [
        {"region": "North", "revenue": 1200, "orders": 14},
        {"region": "South", "revenue": 900, "orders": 11},
        {"region": "North", "revenue": 700, "orders": 9},
    ]
)

print(df.head())
print(df["revenue"].mean())
```

## Common Tasks

### Filter Rows
```python
high_revenue = df[df["revenue"] >= 1000]
print(high_revenue)
```

### Create a New Column
```python
df["average_order_value"] = df["revenue"] / df["orders"]
print(df[["region", "average_order_value"]])
```

### Group and Summarize
```python
summary = df.groupby("region", as_index=False)["revenue"].sum()
print(summary)
```

## Why Pandas Is Useful

Pandas shines when your data has column names and mixed types. CSV exports, spreadsheets, log summaries, and API response tables are all great fits.

## Common Mistakes

- Forgetting to inspect dtypes before doing math or date operations
- Chaining many operations without checking intermediate results
- Looping row by row when vectorized operations are clearer and faster

## Related Reading

- [NUMPY_GUIDE.md](NUMPY_GUIDE.md)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
