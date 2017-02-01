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
		values = [str(i[1]) for i in row_setup]
		values.insert(0, str(count[0][0] + 1))
		formatted_columns = ', '.join(columns)
		formatted_values = ', '.join(values)
		insert_function = 'INSERT INTO'
		insert_query = '{} {} ({}) VALUES ({})'.format(insert_function,
			                                       tablename,
			                                       formatted_columns,
			                                       formatted_values)
	
		#Insert row to database
		conn = sqlite3.connect(self.db)
		c = conn.cursor()
		try:
			c.execute(insert_query)
		except:
			print("Error adding new row.")
		conn.commit()
		conn.close()

	def update(self):
		pass

a = SqliteBuilder('test_db.sqlite')
d = 'test'
e = True
c = [("a", "TEXT"),("b", "INTEGER"),("c", "INTEGER")]
f = [("d", "TEXT")]
g = [("b", 2),("c", 3),("d", 4)]
h = [("b", 3),("c", 4),("d", 5)]
a.create(d,c,e)
a.add_column(d,f)
a.add_row(d,g)
a.add_row(d,h)
