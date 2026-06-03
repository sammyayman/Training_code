import pandas as pd,   numpy as np
from IPython.display import display  

print('\033[1;32m' + "Pandas DataFrame" + '\033[0m')
import polars as pl

# Create a DataFrame
df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
})

# Display the DataFrame
print(df)