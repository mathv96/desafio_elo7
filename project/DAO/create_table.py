import DAO.conn as connection

from config import * 

def create_table():
    conn = connection.connection_mysql()
    query = "CREATE TABLE IF NOT EXISTS {} ({} VARCHAR (200) NOT NULL,{} VARCHAR (20) NOT NULL,{} VARCHAR (200) NOT NULL,{} VARCHAR (20) NOT NULL, {} DATETIME NOT NULL)".format(
            table_name, 'component', 'version', 'responsible', 'status', 'date')
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
        except Exception as e:
            return False
        return True