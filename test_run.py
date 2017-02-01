from sqliteBuilder.sqliteBuilder import SqliteBuilder

a = SqliteBuilder('test_db.sqlite')
d = 'test'
e = True
c = [("a", "TEXT"),("b", "INTEGER"),("c", "INTEGER")]
f = [("d", "TEXT")]
g = [("b", 2),("c", 3),("d", 4)]
h = [("b", 3),("c", 4),("d", 5)]
i = [("a", 1),("b", 3),("c", 4),("d", 5)]
q = "SELECT b FROM test WHERE a=1"
a.create(d,c,e)
a.add_column(d,f)
a.add_row(d,g)
a.add_row(d,h)
a.update(d,i)
z = a.query(d, q, False)
print(z)