#Built-ins
import sqlite3


class SqliteBuilder():
	"""
	Create, fill, and edit sqlite db with sqlite3 module
	"""
	def __init__(self, filename):
		self.db = filename

	def create(self, tablename, column_setup, primary_key):
		
		#Initial table and columns setup
		num_columns = len(column_setup)
		formatted_columns = []
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
		sql_function = 'CREATE TABLE'
		sql_query = '{} {}({})'.format(sql_function,
			                       tablename,
			                       column_string)

        #Initialize database
		conn = sqlite3.connect(self.db)
		c = conn.cursor()
		try:
			c.execute(sql_query)
		except:
			print("Table already exists.")
		conn.commit()
		conn.close()

	def add_column(self, tablename, column_setup):
		
		#New column setup
		formatted_column = "{} ADD COLUMN {} {}".format(tablename,
			                                        column_setup[0][0],
			                                        column_setup[0][1])
		sql_function = 'ALTER TABLE'
		sql_query = '{} {}'.format(sql_function, formatted_column)
		
		#Add column to database
		conn = sqlite3.connect(self.db)
		c = conn.cursor()
		try:
			c.execute(sql_query)
		except:
			print("Error adding new column.")
		conn.commit()
		conn.close()

	def insert_row(self):
		pass
	def update(self):
		pass

a = SqliteBuilder('test_db.sqlite')
d = 'test'
e = True
c = [("a", "TEXT"),("b", "INTEGER"),("c", "INTEGER")]
f = [("e", "TEXT")]
#a.create(d,c,e)
a.add_column(d,f)
