import psycopg2
import json

con = psycopg2.connect(host='172.17.0.3',
                            database='aplication',
                            user='postgres',
                            password='270495')




cursor = con.cursor()



nome = input('Digite o nome do colaborador: ')

formatacao = nome.capitalize()

filtro = formatacao


sql_consulta = ('select * from seguidores where nome like %s',(path,))


cursor.execute(sql_consulta,filtro)

print(cursor.fetchall())