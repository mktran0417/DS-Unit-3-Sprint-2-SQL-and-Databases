from os import replace
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import queries

#Method 1
def psycop():
    DBNAME = 'postgres'
    USER = 'postgres'
    PASS = 'root'
    HOST = '127.0.0.1'
    PORT = '5432'
    connection = psycopg2.connect(dbname=DBNAME, user=USER, password=PASS, host=HOST, port=PORT)
    cursor = connection.cursor()

    execute_query_pg(cursor, connection, queries.create_titanic)

    for index, row in data.iterrows():
        insert_statement =  '''
                                INSERT INTO titanic_method_one(SURVIVED, PCLASS, NAME, SEX, AGE, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
                                VALUES({}, {}, '{}', '{}', {}, {}, {}, {});
                            '''.format(row['Survived'], row['Pclass'], row['Name'].replace("'", "''"), row['Sex'], row['Age'], row[
            'Siblings/Spouses Aboard'], row['Parents/Children Aboard'], row['Fare'])
        execute_query_pg(cursor, connection, insert_statement)


def execute_query_pg(curs, conn, query):
    results = curs.execute(query)
    conn.commit()
    return results


#Method 2
def to_sql_alc():
    connection_alch = create_engine('postgresql://postgres:root@localhost:5432/postgres')
    data = pd.read_csv('titanic.csv')
    data.to_sql('titanic_method_2', con=connection_alch, if_exists='replace')
    return


if __name__ == '__main__':

    data = pd.read_csv('titanic.csv')

    to_sql_alc
    psycop()
