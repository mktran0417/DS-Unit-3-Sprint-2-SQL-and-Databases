'''
Michael Tran
11/5/21

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `demo_data.sqlite3`
- Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
  the above data (name the table `demo`)
- Write and execute appropriate `INSERT INTO` statements to add the data (as
  shown above) to the database

Make sure to `commit()` so your data is saved!
The file size should be non-zero.

Then write the following queries (also with `sqlite3`) to test the demo'
database and save them under the following variables names:

- `row_count`: Count how many rows you have - it should be 3!
- `xy_at_least_5`: How many rows are there where both `x` and `y`
   are at least 5?
- `unique_y`: How many unique values of `y` are there (hint - `COUNT()`
   can accept a keyword
  `DISTINCT`)?
'''
import sqlite3


# queries
CREATE_TABLE = '''
              CREATE TABLE if NOT EXISTS demo(
              s CHAR NOT NULL,
              x INT NOT NULL,
              y INT NOT NULL)
              '''

ADD_VALUES = '''
              INSERT INTO demo(s, x, y)
              VALUES('{}', {}, {})
              '''

VALUES = {'s': ['g', 'v', 'f'],
          'x': [3, 5, 8],
          'y': [9, 7, 7]
          }

row_count = '''SELECT COUNT(*) FROM demo'''

xy_at_least_5 = '''
                  SELECT COUNT(*) FROM demo
                  WHERE x >= 5 and y >=5
                '''

unique_y = '''SELECT COUNT(DISTINCT y) FROM demo'''


def connect_db(name='demo_data.sqlite3'):
    ''' connects to db '''
    return sqlite3.connect(name)


def curs(connection):
    ''' creates cursor to access db '''

    return connection.cursor()


def execute_query(cursor, query):
    ''' executes query on db'''
    return cursor.execute(query).fetchall()


if __name__ == '__main__':
    connection = connect_db()
    cursor = curs(connection)
    execute_query(cursor, CREATE_TABLE)

    for i in range(len(VALUES)):
        execute_query(cursor, ADD_VALUES.format(
            VALUES['s'][i], VALUES['x'][i], VALUES['y'][i]))
        connection.commit()
