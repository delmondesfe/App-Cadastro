from logging import exception
import psycopg2




def teste_db():
    try:
        con = psycopg2.connect(host='172.17.0.3',
                            database='aplication',
                            user='postgres',
                            password='270495')
        return print('Conexão realizada com sucesso !!')
    except:
        return print('Erro ao conectar')


teste_db()