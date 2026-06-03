import pandas as pd
from IPython.display import display
df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Red', 'Green', 'Blue', 'Red', 'Yellow', 'Green', 'Blue', 'Red']
})

duplicates = df['Color'].duplicated().sum()
print(duplicates)
df['Color'].duplicated()
print
print('==='*20 , '\n'*2)

unique_count = df['Color'].nunique()
print(unique_count)
print('==='*20 , '\n'*2)

counts = df['Color'].value_counts()
display(counts)
print('==='*20 , '\n'*2)

counts_df = counts.reset_index()
counts_df.columns = ['Color_Value', 'Count']
display(counts_df)
print(counts_df)