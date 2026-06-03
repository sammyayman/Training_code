# psycopg2 Connection and Cursor Methods Reference

## Connection Object (`conn`) Methods

### Essential Methods:

- **`conn.cursor()`** - Creates a new cursor object

  ```python
  cur = conn.cursor()
  ```

- **`conn.commit()`** - Commits the current transaction (saves changes)

  ```python
  conn.commit()  # Required after INSERT, UPDATE, DELETE
  ```

- **`conn.rollback()`** - Rolls back the current transaction (undoes changes)

  ```python
  conn.rollback()  # Undoes uncommitted changes
  ```

- **`conn.close()`** - Closes the database connection
  ```python
  conn.close()
  ```

### Configuration Methods:

- **`conn.set_session()`** - Configures session parameters

  ```python
  conn.set_session(autocommit=True)  # Auto-commit mode
  conn.set_session(isolation_level=1)  # Read uncommitted
  ```

- **`conn.set_isolation_level()`** - Sets transaction isolation level

  ```python
  conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
  ```

- **`conn.set_client_encoding()`** - Sets client encoding
  ```python
  conn.set_client_encoding('UTF8')
  ```

### Information Methods:

- **`conn.get_dsn_parameters()`** - Returns connection parameters as dict

  ```python
  params = conn.get_dsn_parameters()
  ```

- **`conn.status`** - Connection status (1 = open, 0 = closed)

  ```python
  if conn.status == 1:
      print("Connection is open")
  ```

- **`conn.closed`** - Returns 0 if open, non-zero if closed
  ```python
  if conn.closed == 0:
      print("Connection is active")
  ```

---

## Cursor Object (`cur`) Methods

### Execution Methods:

- **`cur.execute(query, params=None)`** - Executes a single SQL command

  ```python
  cur.execute("SELECT * FROM table WHERE id = %s", (123,))
  ```

- **`cur.executemany(query, param_list)`** - Executes query multiple times with different parameters

  ```python
  data = [('John', 25), ('Jane', 30)]
  cur.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", data)
  ```

- **`cur.callproc(procname, params=None)`** - Calls a stored procedure
  ```python
  cur.callproc('my_procedure', (param1, param2))
  ```

### Fetch Methods:

- **`cur.fetchone()`** - Fetches the next row (returns tuple or None)

  ```python
  row = cur.fetchone()  # Returns one row or None
  ```

- **`cur.fetchmany(size=cursor.arraysize)`** - Fetches multiple rows

  ```python
  rows = cur.fetchmany(5)  # Returns list of up to 5 rows
  ```

- **`cur.fetchall()`** - Fetches all remaining rows

  ```python
  all_rows = cur.fetchall()  # Returns list of all rows
  ```

- **`cur.scroll(value, mode='relative')`** - Moves cursor position
  ```python
  cur.scroll(2, mode='relative')  # Move forward 2 rows
  cur.scroll(0, mode='absolute')  # Move to beginning
  ```

### Information Methods:

- **`cur.description`** - Returns column information (read-only)

  ```python
  columns = cur.description  # List of column info tuples
  ```

- **`cur.rowcount`** - Number of rows affected by last query (read-only)

  ```python
  print(f"Rows affected: {cur.rowcount}")
  ```

- **`cur.statusmessage`** - Status message from last command (read-only)

  ```python
  print(cur.statusmessage)  # e.g., "SELECT 10"
  ```

- **`cur.query`** - The last executed query string (read-only)
  ```python
  print(cur.query)
  ```

### Configuration:

- **`cur.arraysize`** - Default number of rows for fetchmany()

  ```python
  cur.arraysize = 100  # Default fetchmany size
  ```

- **`cur.close()`** - Closes the cursor
  ```python
  cur.close()
  ```

### Advanced Methods:

- **`cur.copy_from(file, table, columns=None, sep='\t')`** - Copy data from file to table

  ```python
  cur.copy_from(open('data.csv'), 'mytable', columns=('col1', 'col2'))
  ```

- **`cur.copy_to(file, table, columns=None, sep='\t')`** - Copy data from table to file

  ```python
  cur.copy_to(open('output.csv', 'w'), 'mytable')
  ```

- **`cur.copy_expert(sql, file)`** - Advanced copy using SQL COPY command
  ```python
  cur.copy_expert("COPY table TO STDOUT WITH CSV", file)
  ```

---

## Common Usage Patterns

### Pattern 1: Read Operations (SELECT)

```python
cur.execute("SELECT * FROM table")
rows = cur.fetchall()  # or fetchone(), fetchmany()
# No commit needed for SELECT
```

### Pattern 2: Write Operations (INSERT/UPDATE/DELETE)

```python
cur.execute("INSERT INTO table VALUES (%s, %s)", (val1, val2))
conn.commit()  # MUST commit to save changes
```

### Pattern 3: Multiple Inserts

```python
data = [(1, 'a'), (2, 'b'), (3, 'c')]
cur.executemany("INSERT INTO table (col1, col2) VALUES (%s, %s)", data)
conn.commit()
```

### Pattern 4: Transaction with Rollback

```python
try:
    cur.execute("INSERT INTO table VALUES (%s)", (val,))
    conn.commit()
except:
    conn.rollback()  # Undo on error
```

### Pattern 5: Get Column Names

```python
cur.execute("SELECT * FROM table")
column_names = [desc[0] for desc in cur.description]
```
