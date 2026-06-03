import psycopg2
import pandas as pd
import polars as pl
from psycopg2.extras import RealDictCursor

# PostgreSQL connection parameters
# Update these with your actual database credentials
DB_CONFIG = {
    'host': 'localhost',          # or your PostgreSQL server IP
    'port': 5432,                  # default PostgreSQL port
    'database': 'My first db',   # your database name
    'user': 'postgres',       # your PostgreSQL username
    'password': 'root'   # your PostgreSQL password
}

def connect_to_postgres():
    """Establish connection to PostgreSQL database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print('\033[1;32m' + "✓ Successfully connected to PostgreSQL!" + '\033[0m')
        return conn
    except psycopg2.Error as e:
        print(f'\033[1;31m' + f"Error connecting to PostgreSQL: {e}" + '\033[0m')
        return None

def execute_query(conn, query, return_dataframe='pandas'):
    """
    Execute a SQL query and return results as DataFrame
    
    Parameters:
    - conn: PostgreSQL connection object
    - query: SQL query string
    - return_dataframe: 'pandas' or 'polars' (default: 'pandas')
    """
    try:
        if return_dataframe == 'pandas':
            # Using pandas
            df = pd.read_sql_query(query, conn)
            return df
        elif return_dataframe == 'polars':
            # Using polars
            df = pl.read_database(query, conn)
            return df
        else:
            # Return raw results
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query)
                return cur.fetchall()
    except psycopg2.Error as e:
        print(f'\033[1;31m' + f"Error executing query: {e}" + '\033[0m')
        return None

# Example usage
if __name__ == "__main__":
    # Connect to database
    conn = connect_to_postgres()
    
    if conn:
        # Query from your .pgsql file
        query = "SELECT * FROM VideoGames;"
        
        # Get results as pandas DataFrame
        print('\033[1;32m' + "\n--- Using Pandas ---" + '\033[0m')
        df_pandas = execute_query(conn, query, return_dataframe='pandas')
        if df_pandas is not None:
            print(df_pandas)
            print(f"\nShape: {df_pandas.shape}")
        
        # Get results as polars DataFrame
        print('\033[1;32m' + "\n--- Using Polars ---" + '\033[0m')
        df_polars = execute_query(conn, query, return_dataframe='polars')
        if df_polars is not None:
            print(df_polars)
            print(f"\nShape: {df_polars.shape}")
        
        # Close connection
        conn.close()
        print('\033[1;32m' + "\n✓ Connection closed" + '\033[0m')
    else:
        print('\033[1;31m' + "Failed to establish database connection. Please check your DB_CONFIG settings." + '\033[0m')

