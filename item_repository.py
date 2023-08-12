from pprint import pprint
from item import make_item
import sqlite3

class MemoryItemsRepository():
    _item_list = []

    def add_item(self, raw_item):
        self._item_list.append(make_item(raw_item))
    
    def delete_all(self):
        self._item_list = []
    
    def get_all(self):
        return self._item_list


class SQLiteItemsRepository():
    
    def __init__(self):
        self._connection = sqlite3.connect('database.db')
        self._connection.row_factory = sqlite3.Row

    def __del__(self):
        self._connection.close()


    def add_item(self, raw_item):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO ITEM (title, price) VALUES (?, ?)", (raw_item["title"], raw_item["price"]))
        item_id = cursor.lastrowid

        joined_types = ','.join(f'"{type}"' for type in raw_item["type"])
        types = cursor.execute(f"SELECT * FROM TYPE WHERE type in ({joined_types})").fetchall()

        for type in types:
            cursor.execute("INSERT INTO ITEM_TYPE (item_id, type_id) VALUES (?, ?)", (item_id, type['id']))
        
        self._connection.commit()
    
    def delete_all(self):
        self._connection.execute("DELETE FROM ITEM")
        self._connection.commit()

    
    def get_all(self):
        final_results = []

        raw_sql_items = self._connection.execute("SELECT * FROM ITEM").fetchall()
        for raw_sql_item in raw_sql_items:
            item_types = self._connection.execute("SELECT TYPE.type FROM TYPE INNER JOIN ITEM_TYPE ON ITEM_TYPE.item_id=? AND ITEM_TYPE.type_id=TYPE.id", (raw_sql_item["id"],)).fetchall()
            final_results.append({
                "title": raw_sql_item["title"],
                "price": raw_sql_item["price"],
                "type": set(type["type"] for type in item_types)
            })

        return final_results