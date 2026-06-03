# import polars as pl , pandas as pd

# # df_pl = pl.DataFrame({
# #     "name": ["Sam", "Lina", "Omar"],
# #     "age": [21, 30, 25],
# #     "score": [88, 92, 79]
# # })

# # print(df_pl)

# df_pd = pd.DataFrame({
#     "name": ["Sam", "Lina", "Omar"],
#     "age": [21, 30, 25],
#     "score": [88, 92, 79]
# })
# print(df_pd)

# # Convert Polars DataFrame to Pandas DataFrame
# # pl_df = pl.from_arrow(df_pd)
# pl_df = pl.from_pandas(df_pd)

# print(pl_df)



import pandas as pd
import polars as pl

# Pandas DataFrame: large resistor table
df = pd.DataFrame({
    "resistor_id": [f"R{i}" for i in range(1, 21)],
    "resistance_ohms": [
        10, 22, 33, 47, 68, 82, 100, 150, 220, 330,
        470, 680, 820, 1000, 1500, 2200, 3300, 4700, 6800, 10000
    ],
    "tolerance_pct": [
        1, 1, 5, 5, 5, 10, 1, 5, 1, 1,
        5, 10, 10, 1, 5, 10, 5, 1, 1, 5
    ],
    "power_watt": [
        0.25, 0.25, 0.25, 0.5, 0.5, 1, 0.25, 0.5, 1, 2,
        2, 1, 0.25, 0.25, 0.5, 1, 1, 2, 2, 2
    ]
})

# Convert pandas → Polars
pl_df = pl.from_pandas(df)
print(df)
print(pl_df)




# Pandas DataFrame: capacitor specs
df = pd.DataFrame({
    "capacitor_id": ["C1", "C2", "C3"],
    "capacitance_uF": [10, 47, 100],
    "voltage_rating_v": [16, 25, 50]
})

# Convert to Polars
pl_df = pl.from_pandas(df)

print(pl_df)
print(df)

 