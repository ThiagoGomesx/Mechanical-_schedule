from app.config.database_config import connection

def execute_select(query):

    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(query)
        print(cursor.fetchall())
    except Exception as e:
        print(e)

def insert (query):

    try:
      conn = connection()
      cursor = conn.cursor()
      cursor.execute(query)
      conn.commit()
    except Exception as e:
        print(e)


