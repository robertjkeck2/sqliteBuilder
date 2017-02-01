# sqliteBuilder
## Helper for building sqlite database

## Quick Start:

Import the builder class:
```python
>>> from sqliteBuilder.sqliteBuilder import SqliteBuilder
```

Initialize a new instance of the builder class by passing the desired db name when initializing:
```python
>>> new_db = SqliteBuilder('new_db_name.sqlite')
```

Create a new table in the db by passing the table name, column setup, and primary key options to the create method:
```python
>>> table_name = 'test_table'
>>> column_setup = [("col1", "TEXT"),("col2", "INTEGER"),("col3", "INTEGER")]
>>> primary_key = True
>>> new_db.create(table_name, column_setup, primary_key
```

Add another column to the table by passing the table name and column setup to the add_column method:
```python
>>> table_name = 'test_table'
>>> column_setup = [("col4", "TEXT")]
>>> new_db.add_column(table_name, column_setup)
```

Insert row data by passing the table name and row setup to the add_row method:
```python
>>> table_name = 'test_table'
>>> row_setup = [("col2", 2),("col3", 3),("col4", 4)]
>>> new_db.add_row(table_name, row_setup)
```

Update a row entry by passing the table name and updated row setup to the update method:
```python
>>> table_name = 'test_table'
>>> row_setup = [("col1", 1),("col2", 7),("col3", 8),("col4", 9)]
>>> new_db.update(table_name, row_setup)
```

Query a table by passing the table name, SQL query, and print options to the query method:
```python 
>>> table_name = 'test_table'
>>> sql_query = 'SELECT * FROM test_table'
>>> print_options = False
>>> new_db.query(table_name, sql_query, print_options)
```
