import sqlite3

connection = sqlite3.connect('database.db')

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

connection.commit()
connection.close()