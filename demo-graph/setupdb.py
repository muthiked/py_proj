import csv
import mysql.connector
from mysql.connector import Error

def connect_to_db():
    conn = None
    try:
        conn = mysql.connector.connect(
            host= 'localhost',
            user = 'root',
            password = 'Ytrewq12.',
            database = 'world')
        if conn.is_connected():
            print('Connected to database')
        return conn
    except Error as e:
        print(e)

def select_all():
    cn = connect_to_db()
    cs = cn.cursor()
    cs.execute("select * from city order by name")
    rows = cs.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    select_all()



