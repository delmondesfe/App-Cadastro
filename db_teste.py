import psycopg2

def conecta_db():
    con = psycopg2.connect(host='localhost',
                           database='aplication',
                           user='postgres',
                           password='270495')
    return con

conecta_db()