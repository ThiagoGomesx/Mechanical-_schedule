from API.config.database_config import connection

if __name__ == '__main__':
    try:
        connection = connection()
        cursor = connection.cursor()
        cursor.execute( 'select * from tipo_usuario')
        print (cursor.fetchall())
    except Exception as e:
        print(e)