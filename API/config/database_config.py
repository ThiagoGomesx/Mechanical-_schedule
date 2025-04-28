import psycopg2


def connection():
    return psycopg2.connect(host='localhost', database= 'databasegomes', user= 'dbusergomes', password= 'root',port= '5432')




