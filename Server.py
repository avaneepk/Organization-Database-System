import psycopg2

def connectSql():
    conn = psycopg2.connect(    #need to add your own connection here
        host="localhost",
        database="aether",
        user="postgres",
        password="avaneep")

    return conn
