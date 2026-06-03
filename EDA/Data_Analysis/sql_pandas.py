import pyodbc
import pandas as pd

# Simple SQL Server connection with pandas
server = 'LAPTOP-O2H5FU1M\\SQLEXPRESS'
database = 'master'

try:
    # Connect to SQL Server
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    
    print("✅ Connected to SQL Server!")
    
    # Example 1: Simple query to pandas DataFrame
    query1 = "SELECT name, database_id, create_date FROM sys.databases"
    df1 = pd.read_sql(query1, conn)
    print("\n📊 Databases:")
    print(df1)
    
    # Example 2: Query with pandas formatting
    query2 = """
    SELECT 
        @@SERVERNAME as ServerName,
        @@VERSION as Version,
        GETDATE() as CurrentTime
    """
    df2 = pd.read_sql(query2, conn)
    print("\n📊 Server Info:")
    print(df2)
    
    # Example 3: Save DataFrame to CSV
    df1.to_csv('databases.csv', index=False)
    print("\n💾 Saved databases list to 'databases.csv'")
    
    # Close connection
    conn.close()
    print("\n✅ Connection closed")
    
except Exception as e:
    print(f"❌ Error: {e}")
