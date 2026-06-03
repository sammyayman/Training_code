import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="Ayman_DB",
        user="postgres",
        password="root"
    )

    cur = conn.cursor()  
    
    cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public';
""")

    tables = cur.fetchall()
    print("Tables in the database:", tables)
    
    # cur.execute("""ALTER TABLE videogames RENAME TO Games;
    #             SELECT table_name
    #             FROM information_schema.tables
    #             WHERE table_schema = 'public';
    #             """)
    # conn.commit() 
    cur.execute("SELECT game, price, sales, price*sales AS revenue FROM Games")
    print(cur.fetchall())

    cur.execute("SELECT current_database(), current_user, inet_server_addr(), inet_server_port();")
    print(cur.fetchall())

    cur.execute("SELECT COUNT(*), MAX(id) FROM Games;")
    print(cur.fetchall())

    result = cur.fetchall()

    print("✅ Connection successful, result:", result)

except Exception as e:
    print("❌ Connection failed")
    print(e)

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()

