import pandas as pd 
from IPython.display import display
df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Red', 'Green', 'Blue', 'Red', 'Yellow', 'Green', 'Blue', 'Red']
})

duplicates = df['Color'].duplicated()

print(f"df['Color'].duplicated():\n{duplicates}" , \
    '==================> Sum of Duplicates or True = duplicates.sum() :', \
        duplicates.sum())

df_with_duplicates = pd.concat([df, duplicates], axis=1)
print("df_with_duplicates = pd.concat([df, duplicates], axis=1):\n",\
    df_with_duplicates)
print('--'*20 , '\n')
df_with_duplicates.columns = ['Color', 'IsDuplicate']
print(f" df_with_duplicates.columns = ['Color', 'IsDuplicate'] : \n  {df_with_duplicates}")



print('==='*20 , '\n'*2)

unique_count = df['Color'].nunique()
print(f"df['Color'].nunique() = {unique_count}")



print('==='*20 , '\n'*2)

counts = df['Color'].value_counts()
display("df['Color'].value_counts(): \n",counts)

print('==='*20 , '\n'*2)


counts_df = counts.reset_index()
print(f"counts.reset_index(): \n{counts_df}")



print('--'*20 , '\n')

counts_df.columns = ['Color_Value', 'Count']
display(f"counts_df.columns = ['Color_Value', 'Count']: \n  {counts_df}") 
print('==='*20 , '\n'*2)

results = {}
results['Color'] = {
    'duplicates': duplicates.sum(),
    'unique_values': unique_count,
    'value_counts_df': counts_df
}

print(results)                     