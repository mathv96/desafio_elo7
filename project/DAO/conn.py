import mysql.connector

from config import * 

def connection_mysql():
    conn = None
    try:
        conn = mysql.connector.connect(user=user, password=password,
                                  host=host,
                                  database=database)
    except Exception as e:
        print (e)
        conn = None
    return conn