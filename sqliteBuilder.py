#Built-ins
import sqlite3


class SqliteBuilder():
	"""
	Create, fill, and edit sqlite db with sqlite3 module
	"""
	def __init__(self):
		pass

	def create(self, filename, tablename, column_setup, primary_key):
		
		#Determine table setup
		num_columns = len(column_setup)
		formatted_columns = []
		for i in range(0, num_columns):
			if (primary_key is True) and (i == 0):
				primary_addition = ' PRIMARY KEY'
			else:
				primary_addition = ''
			column = '{cn} {ft}{pk}'.format(cn = column_setup[i][0], 
											  ft = column_setup[i][1], 
											  pk = primary_addition)
			formatted_columns.append(column)

		column_string = ', '.join(formatted_columns)

		#Initialize database
		conn = sqlite3.connect(filename)
		c = conn.cursor()
		sql_function = 'CREATE TABLE'
		sql_query = '{sf} {tn}({cs})'.format(sf = sql_function,
										     tn = tablename,
				  						     cs = column_string)
		try:
			c.execute(sql_query)
		except:
			print("Table already exists.")
		
		conn.commit()
		conn.close()

	def add_column(self):
		pass
	def insert_row(self):
		pass
	def update(self):
		pass

a = SqliteBuilder()
b = 'test_db.sqlite'
d = 'test'
e = True
c = [("a", "TEXT"),("b", "INTEGER"),("c", "INTEGER")]
a.create(b,d,c,e)