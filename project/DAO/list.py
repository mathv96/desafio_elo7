import DAO.conn as connection
from datetime import datetime

from config import * 

def lis_events():
    conn = connection.connection_mysql() 
    query = "SELECT * FROM {}".format(table_name)

    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            result_list = [list(line) for line in cursor.fetchall()]
            for line in result_list:
                print(line)
            conn.close()
        except Exception as e:
            conn.close()
            print(e.__context__)
            return False
        return True
    else:
        return False