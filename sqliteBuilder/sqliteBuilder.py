#Built-ins
import sqlite3

#External imports
import pandas as pd


class SqliteBuilder():
	"""
	Create, fill, and edit sqlite db with sqlite3 module
	"""
	def __init__(self, filename):
		self.db = filename

	def create(self, tablename, column_setup, primary_key):
		
		#Initial table and columns setup
		formatted_columns = []
		num_columns = len(column_setup)
		for i in range(0, num_columns):
			if (primary_key is True) and (i == 0):
				primary_addition = ' PRIMARY KEY'
			else:
				primary_addition = ''
			column = '{} {}{}'.format(column_setup[i][0], 
				                  column_setup[i][1], 
				                  primary_addition)
			formatted_columns.append(column)

		column_string = ', '.join(formatted_columns)
		create_function = 'CREATE TABLE'
		create_query = '{} {}({})'.format(create_function,
			                       tablename,
			                       column_string)

        #Initialize database
		conn = sqlite3.connect(self.db)
		c = conn.cursor()
		try:
			c.execute(create_query)
		except:
			print("Table already exists.")
		conn.commit()
		conn.close()

	def add_column(self, tablename, column_setup):
		
		#New column setup
		formatted_column = "{} ADD COLUMN {} {}".format(tablename,
			                                        column_setup[0][0],
			                                        column_setup[0][1])
		alter_function = 'ALTER TABLE'
		alter_query = '{} {}'.format(alter_function, formatted_column)
		
		#Add column to database
		conn = sqlite3.connect(self.db)
		c = conn.cursor()
		try:
			c.execute(alter_query)
		except:
			print("Error adding new column.")
		conn.commit()
		conn.close()

	def add_row(self, tablename, row_setup):
		
		#Determine current table row and first column name
		conn = sqlite3.connect(self.db)
		c = conn.cursor()
		c.execute('SELECT COUNT(*) FROM {}'.format(tablename))
		count = c.fetchall()
		c.execute('PRAGMA TABLE_INFO({})'.format(tablename))
		col_names = [i[1] for i in c.fetchall()]
		first_col = col_names[0]
		conn.close()

		#New row setup
		columns = [i[0] for i in row_setup]
		columns.insert(0, str(first_col))
		values = ["'" + str(i[1]) + "'" for i in row_setup]
		values.insert(0, str(count[0][0] + 1))
		formatted_columns = ', '.join(columns)
		formatted_values = ', '.join(values)
		insert_function = 'INSERT INTO'
		insert_query = '{} {} ({}) VALUES ({})'.format(insert_function,
			                                       tablename,
			                                       formatted_columns,
			                                       formatted_values)
		print(insert_query)
	
		#Insert row to database
		conn = sqlite3.connect(self.db)
		c = conn.cursor()
		try:
			c.execute(insert_query)
		except:
			print("Error adding new row.")
		conn.commit()
		conn.close()

	def update(self, tablename, row_setup):
		
		#Updated row setup
		update_vals = []
		columns = [i[0] for i in row_setup]
		values = ["'" + str(i[1]) + "'" for i in row_setup]
		for i in range(1,len(columns)):
			col_vals = '{}={}'.format(columns[i], values[i])
			update_vals.append(col_vals)
		formatted_update_vals = ', '.join(update_vals)
		update_function = 'UPDATE {} SET'.format(tablename)
		update_query = '{} {} WHERE {}={}'.format(update_function,
			                                  formatted_update_vals,
			                                  columns[0],
			                                  values[0])
		
		#Update row information
		conn = sqlite3.connect(self.db)
		c = conn.cursor()
		try:
			c.execute(update_query)
		except:
			print("Error updating row.")
		conn.commit()
		conn.close()

	def query(self, tablename, query, to_print):
		
		#Execute SQL query
		conn = sqlite3.connect(self.db)
		c = conn.cursor()
		c.execute('PRAGMA TABLE_INFO({})'.format(tablename))
		col_names = [i[1] for i in c.fetchall()]
		try:
			c.execute(query)
		except:
			print("Error querying table.")
		results = c.fetchall()
		conn.close()

		#Pretty print database
		if to_print:
		    df = pd.DataFrame(results, columns=col_names)
		    db_title = 'DATABASE: {}'.format(self.db)
		    table_title = 'TABLE: {}'.format(tablename)
		    pretty_db = '{}\n{}\n{}'.format(db_title, table_title, df)
		    print(pretty_db)
		else:
			return results[0][0]
