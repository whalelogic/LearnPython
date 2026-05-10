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

---

## Deep Reference

### DataFrame and Series Mental Model

A `DataFrame` is a dictionary of equal-length `Series`. Each `Series` is a labeled 1-D array backed by NumPy. Operations on columns are vectorized; row-wise `apply` is a last resort.

```python
import pandas as pd

df = pd.DataFrame({
    "name":    ["Ava", "Ben", "Cara"],
    "score":   [91, 78, 88],
    "passed":  [True, False, True],
})

# Series — one column
print(df["score"])          # 0    91 / 1    78 / 2    88
print(type(df["score"]))    # <class 'pandas.core.series.Series'>

# Scalar access — fastest for single cells
print(df.at[0, "name"])     # Ava
print(df.iat[0, 1])         # 91
```

### Loading and Saving

| Format | Read | Write |
|---|---|---|
| CSV | `pd.read_csv("f.csv")` | `df.to_csv("f.csv", index=False)` |
| JSON | `pd.read_json("f.json")` | `df.to_json("f.json", orient="records")` |
| Excel | `pd.read_excel("f.xlsx", sheet_name=0)` | `df.to_excel("f.xlsx", index=False)` |
| Parquet | `pd.read_parquet("f.parquet")` | `df.to_parquet("f.parquet")` |
| SQL | `pd.read_sql(query, engine)` | `df.to_sql("table", engine, if_exists="replace")` |
| Clipboard | `pd.read_clipboard()` | `df.to_clipboard()` |

```python
# Read with type hints and date parsing
df = pd.read_csv(
    "orders.csv",
    dtype={"order_id": int, "amount": float},
    parse_dates=["created_at"],
)
```

### Selection Patterns

```python
# Column selection
df["revenue"]                        # Series
df[["region", "revenue"]]            # DataFrame

# Row filtering — boolean mask
df[df["revenue"] > 1000]
df[(df["revenue"] > 500) & (df["region"] == "North")]

# Label-based — loc
df.loc[0:4, "revenue":"orders"]      # rows 0–4, columns revenue through orders
df.loc[df["revenue"] > 500, "region"]

# Integer-position — iloc
df.iloc[0:3, 1:3]                    # first 3 rows, columns 1 and 2
df.iloc[-1, :]                       # last row

# Query string (readable for complex filters)
df.query("revenue > 1000 and region == 'North'")
```

### Inspection Quick-Reference

| Method / Attribute | Purpose |
|---|---|
| `df.head(n)` / `df.tail(n)` | First / last `n` rows |
| `df.info()` | Column names, dtypes, null counts |
| `df.describe()` | Count, mean, std, quartiles for numeric columns |
| `df.shape` | `(rows, columns)` tuple |
| `df.dtypes` | Per-column dtype |
| `df.isnull().sum()` | Null count per column |
| `df["col"].value_counts()` | Frequency table |
| `df["col"].nunique()` | Count of distinct values |
| `df.sample(n)` | Random sample of `n` rows |
| `df.memory_usage(deep=True)` | Memory per column in bytes |

### Transformation Quick-Reference

| Operation | Method / pattern |
|---|---|
| Add a column | `df["new"] = df["a"] + df["b"]` or `df.assign(new=...)` |
| Rename columns | `df.rename(columns={"old": "new"})` |
| Drop columns | `df.drop(columns=["col"])` |
| Cast type | `df.astype({"col": int})` |
| Fill nulls | `df["col"].fillna(0)` / `df.fillna(df.mean(numeric_only=True))` |
| Drop null rows | `df.dropna(subset=["col"])` |
| Parse dates | `pd.to_datetime(df["date"])` |
| String ops | `df["name"].str.lower()` / `.str.contains("pat")` |
| Apply function | `df["col"].apply(fn)` (element-wise) |
| Map values | `df["status"].map({"Y": True, "N": False})` |
| Replace values | `df.replace({"old": "new"})` |
| Reset index | `df.reset_index(drop=True)` |

### Aggregation and GroupBy

```python
# Simple aggregation
df.groupby("region")["revenue"].sum()
df.groupby("region")["revenue"].agg(["sum", "mean", "count"])

# Multiple aggregations with named outputs
summary = df.groupby("region").agg(
    total_revenue=("revenue", "sum"),
    avg_orders=("orders", "mean"),
    num_rows=("revenue", "count"),
)

# Pivot table
df.pivot_table(
    values="revenue",
    index="region",
    columns="quarter",
    aggfunc="sum",
    fill_value=0,
)
```

### Merging and Combining

| Function | Use case |
|---|---|
| `pd.merge(df1, df2, on="id")` | Inner join on common column |
| `pd.merge(..., how="left")` | Left join — keep all rows from left |
| `pd.merge(..., how="outer")` | Outer join — keep all rows from both |
| `pd.concat([df1, df2])` | Stack rows (append) |
| `pd.concat([df1, df2], axis=1)` | Stack columns side by side |

```python
customers = pd.DataFrame({"id": [1, 2], "name": ["Ava", "Ben"]})
orders    = pd.DataFrame({"id": [1, 1, 2], "amount": [100, 200, 50]})

merged = pd.merge(customers, orders, on="id", how="left")
print(merged.groupby("name")["amount"].sum())
```

### Data Cleaning Patterns

```python
# Audit nulls
print(df.isnull().sum())
print(df.isnull().mean() * 100)   # percentage per column

# Fill numeric columns with median
num_cols = df.select_dtypes("number").columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Remove duplicate rows
df = df.drop_duplicates(subset=["order_id"])

# Strip whitespace from all string columns
str_cols = df.select_dtypes("object").columns
df[str_cols] = df[str_cols].apply(lambda s: s.str.strip())
```

### Progress Rubric

| Level | Demonstrated ability |
|---|---|
| **Beginner** | Load a CSV, inspect with `head()` / `info()`, select and filter columns |
| **Developing** | Add computed columns, use `groupby`, handle nulls |
| **Proficient** | Merge tables, parse dates, use `loc`/`iloc` correctly, avoid chained assignment |
| **Advanced** | Optimize dtypes for memory, build reusable cleaning pipelines, use vectorized string ops |

### Suggested Practice Projects

1. **Sales summary** — Load a CSV with region/product/revenue, group by region, compute totals, export to a new CSV.
2. **Missing-value audit** — Find columns with nulls, fill numeric ones with median, drop rows where key columns are null.
3. **Date analysis** — Parse a datetime column, extract year and month, group by month to find a revenue trend.
4. **Join exercise** — Merge an orders table and a customers table on ID, then compute per-customer totals.
5. **Full pipeline** — Read raw data → clean nulls and types → filter → aggregate → export.

### Common Gotchas

| Gotcha | Explanation | Fix |
|---|---|---|
| Chained assignment | `df[mask]["col"] = x` silently fails (SettingWithCopyWarning) | Use `df.loc[mask, "col"] = x` |
| Default `object` dtype | Mixed types or strings default to `object` — slow and large | Cast explicitly with `astype` |
| `apply` on rows is slow | Row-wise `apply(fn, axis=1)` is a Python loop in disguise | Use vectorized column math instead |
| Index misalignment | After filtering, the index retains original row numbers | Call `.reset_index(drop=True)` when positional access is needed |
| `inplace=True` | Returns `None`; easy to accidentally discard the result | Prefer `df = df.rename(...)` reassignment |
| Date comparison | Comparing strings to `datetime` silently returns `False` | Convert with `pd.to_datetime` before filtering |

