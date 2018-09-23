import DAO.conn as connection

from config import * 

def insert_event(event):
    conn = connection.connection_mysql()
    query = "INSERT INTO {} VALUES('{}', '{}', {}, '{}', '{}')".format(
            table_name, event['component'], event['version'], event['responsible', event['status']]
        )
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
        except Exception as e:
            return False
        return True