import sqlite3
import queries as q


def connect_db(dbname="rpg_db.sqlite3"):
    return sqlite3.connect(dbname)

def execute(conn, query):
    curs = conn.cursor()
    return curs.execute(query).fetchall()

if __name__ == '__main__':
    conn = connect_db()
    results = execute(conn, q.TOTAL_SUBCLASS)
    print(results[0][0])
