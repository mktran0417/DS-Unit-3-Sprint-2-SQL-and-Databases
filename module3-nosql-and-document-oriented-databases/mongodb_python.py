import sqlite3
import pymongo
import queries

PASSWORD = '8m4l5vnwt5CVgXZF'
DBNAME = 'cluster0'
USERNAME = 'test-user'


def create_sl_conn(source_db='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(source_db)
    return sl_conn


def execute_query(curs, query):
    return curs.execute(query).fetchall()

def create_mdb_conn(password, dbname, username, collection_name):
    client = pymongo.MongoClient('mongodb+srv://{0}:{1}@{2}.io4qg.mongodb.net/{2}?retryWrites=true&w=majority'.format(username, password, dbname))
    db = client[dbname]
    col = db[collection_name]
    return col


def char_items_doc(items):
    item_list = []
    for item in items:
        item_doc = {
            'item_name': item[0],
            'value': item[1],
            'weight': item[2]
        }
        item_list.append(item_doc)
    return item_list

def char_doc_creation(collection, char_list):
    for char in char_list:
        items = execute_query(sl_curs, queries.GET_CHARACTERS_ITEMS.format(char[0]))
        weapons = execute_query(sl_curs, queries.GET_CHARACTERS_WEAPONS.format(char[0]))
        character_doc = {
            'name': char[1],
            'level': char[2],
            'exp': char[3],
            'hp': char[4],
            'strength': char[5],
            'intelligence': char[6],
            'dexterity': char[7],
            'wisdom': char[8],
            'items': char_items_doc(items),
            'weapons': char_items_doc(weapons)
        }
        collection.insert_one(character_doc)


if __name__ == '__main__':
    sl_conn = create_sl_conn()
    sl_curs = sl_conn.cursor()

    characters = execute_query(sl_curs, queries.GET_CHARACTERS)
    col = create_mdb_conn(PASSWORD, DBNAME, USERNAME, 'characters')
    char_doc_creation(col, characters)



