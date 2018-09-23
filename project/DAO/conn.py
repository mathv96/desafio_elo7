import pymysql

from config import * 

def connection_mysql():
    conn = None
    try:
        conn = pymysql.connect(user=user_mysql, passwd=password_mysql, host=host, port=3306, db=database)
    except Exception as e:
        print (e)
        conn = None
    return conn