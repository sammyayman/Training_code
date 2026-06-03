import pyodbc

# Simple SQL Server connection
server = 'LAPTOP-O2H5FU1M\\SQLEXPRESS'
database = 'master'

try:
    # Connect using Windows Authentication
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    
    cursor = conn.cursor()
    print("✅ Connected successfully!")
    
    # Test query
    cursor.execute("SELECT @@VERSION")
    version = cursor.fetchone()[0]
    print(f"SQL Server version: {version[:60]}...")
    
    # Show databases
    cursor.execute("SELECT name FROM sys.databases ORDER BY name")
    print("\nAvailable databases:")
    for row in cursor.fetchall():
        print(f"  - {row[0]}")
    
    # Example query
    cursor.execute("SELECT GETDATE() as CurrentTime, @@SERVERNAME as ServerName")
    row = cursor.fetchone()
    print(f"\nCurrent time: {row[0]}")
    print(f"Server name: {row[1]}")
    
    # Close connection
    cursor.close()
    conn.close()
    print("\n✅ Connection closed")
    
except pyodbc.Error as e:
    print(f"❌ Connection failed: {e}")
    print("\nMake sure SQL Server Express is running!")
