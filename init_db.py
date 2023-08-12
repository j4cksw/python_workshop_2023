import pprint
import sqlite3

connection = sqlite3.connect('database.db')
connection.row_factory = sqlite3.Row
with open('schema.sql') as schema_file:
    connection.executescript(schema_file.read())


cur = connection.cursor()

cur.execute("INSERT INTO TYPE (id, type, whitelisted) VALUES (1, 'book', TRUE)")
cur.execute("INSERT INTO TYPE (id, type, whitelisted) VALUES (2, 'stationary', TRUE)")
cur.execute("INSERT INTO TYPE (id, type, whitelisted) VALUES (3, 'otop', TRUE)")
cur.execute("INSERT INTO TYPE (id, type, whitelisted) VALUES (4, 'liquor', FALSE)")

cur.execute("INSERT INTO ITEM (id, title, price) VALUES (1, 'Stress Python#1', 999)")
cur.execute("INSERT INTO ITEM (id, title, price) VALUES (2, 'Stray Dog', 499)")

cur.execute("INSERT INTO ITEM_TYPE (item_id, type_id) VALUES (1, 1)")
cur.execute("INSERT INTO ITEM_TYPE (item_id, type_id) VALUES (2, 4)")
cur.execute("INSERT INTO ITEM_TYPE (item_id, type_id) VALUES (2, 3)")

raw_types = ['book', 'otop']
joined_types = ','.join(f'"{type}"' for type in raw_types)
types = cur.execute(f"SELECT * FROM TYPE WHERE type in ({joined_types})" ).fetchall()

connection.commit()
connection.close()