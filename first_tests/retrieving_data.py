import polars as pl


# Eager approach
df = pl.read_csv("input/teste.csv")
# print(df)
# print(df.head(5))
# print(df.schema)
shape = df.shape
rows = f"Rows: {shape[0]}"
columns = f"Columns: {shape[1]}"
# print(shape)
# print(rows)
# print(columns)
column_names = df.columns
print(column_names)
