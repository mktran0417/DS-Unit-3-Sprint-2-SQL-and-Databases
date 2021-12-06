import sqlite3
import pandas as pd
import rpg_db

connection = rpg_db.connect_db('buddymove_holidayiq.sqlite3')
#pd.read_csv('buddymove_holidayiq.csv').to_sql('review', connection)

results = rpg_db.execute(connection, 'SELECT count(*) FROM review')
print(results[0][0])

results = rpg_db.execute(connection, '''SELECT COUNT(*) FROM review
                         WHERE review.Nature >= 100 AND review.Shopping >= 100''')
print(results[0][0])
