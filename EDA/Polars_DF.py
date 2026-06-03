import polars as pl , pandas as pd

# # List of lists or tuples

# data = [
#     ["LED", 5.0, "V"],
#     ["Transistor", 0.7, "V"],
#     ["Diode", 0.3, "V"]
# ]

# df = pl.DataFrame(
#     data,
#     schema=["Component", "Value", "Unit"],
#     orient="row"   # force Polars to treat inner lists as rows
# )




# Create a DataFrame from a dictionary, forcing mixed numeric column to Float64
# df = pl.DataFrame(
#     {
#         "Component": ["Resistor", "Capacitor", "Inductor"],
#         "Value": [100, 0.1, 10],   # mixed int/float
#         "Unit": ["Ohm", "F", "H"]
#     },
#     schema={
#         "Component": pl.Utf8,
#         "Value": pl.Float64,  # force float for mixed numeric column
#         "Unit": pl.Utf8
#     }
# )

 
 


# df = pl.DataFrame()
# df = df.with_columns([
#     pl.Series("Component", ["Motor", "Sensor", "Battery"]),
#     pl.Series("Voltage", [12, 5, 3.7], dtype=pl.Float64)  # specify float
# ])


import numpy as np

# Example data: [Game, Genre, Rating, Players]
# data = np.array([
#     ["The Legend of Zelda", "Adventure", 9.5, 1],
#     ["FIFA 24", "Sports", 8.7, 4],
#     ["Call of Duty", "FPS", 8.9, 12],
#     ["Minecraft", "Sandbox", 9.2, 8],
#     ["Among Us", "Party", 8.0, 10],
#     ["Elden Ring", "RPG", 9.8, 1],
#     ["Fortnite", "Battle Royale", 8.3, 100],
#     ["Cyberpunk 2077", "RPG", 7.5, 1],
#     ["Mario Kart", "Racing", 9.0, 4],
#     ["Overwatch 2", "FPS", 8.6, 12]
# ], dtype=object)  # dtype=object for mixed types

# # Create Polars DataFrame
# df = pl.DataFrame(
#     data,
#     schema=["Game", "Genre", "Rating", "MaxPlayers"],
#     orient="row"
# )

# print(df)


import polars as pl
import pyodbc
import os
import warnings

os.system('cls')
warnings.filterwarnings('ignore')

server = 'LAPTOP-O2H5FU1M\\SQLEXPRESS'
database = 'Testdb'

try:
    # Connect to SQL Server
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    
    print("✅ Connected to SQL Server!")
    cursor = conn.cursor()

    # 2️⃣ Create a table
    cursor.execute("""
    IF OBJECT_ID('VideoGames', 'U') IS NOT NULL
        DROP TABLE VideoGames;

    CREATE TABLE VideoGames (
        GameName NVARCHAR(100),
        Genre NVARCHAR(50),
        Rating FLOAT,
        MaxPlayers INT
    )
    """)
    conn.commit()

    # 3️⃣ Insert data
    games = [
        ("Crash Bandicoot 2", "Adventure", 9.5, 1),
        ("FIFA 24", "Sports", 8.7, 4),
        ("Call of Duty", "FPS", 8.9, 12),
        ("Minecraft", "Sandbox", 9.2, 8),
        ("Among Us", "Party", 8.0, 10)
    ]

    cursor.executemany(
        "INSERT INTO VideoGames (GameName, Genre, Rating, MaxPlayers) VALUES (?, ?, ?, ?)",
        games
    )
    conn.commit()

    # 4️⃣ Query the table
    cursor.execute("SELECT * FROM VideoGames")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    # 5️⃣ Create Polars DataFrame directly from the SQL query
    df_polars = pl.DataFrame(games, schema=["GameName", "Genre", "Rating", "MaxPlayers"])
    print(df_polars)

    # 6️⃣ Close connection
    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")