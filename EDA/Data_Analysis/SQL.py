import pyodbc , pandas as pd
import os
os.system('cls')

import pyodbc

# Connect to your SQL Server Express
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-O2H5FU1M\\SQLEXPRESS;"
    "DATABASE=master;"  # or any other database name
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Your SQL queries here
cursor.execute("SELECT name FROM sys.databases ORDER BY name")
results = cursor.fetchall()
df = pd.DataFrame(results, columns=['Database Name'])
print(df)

# Don't forget to close
cursor.close()
conn.close()
print("Connection closed")