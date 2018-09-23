import conn

def insert_event(event):
    conn = conn.connection_mysql()
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