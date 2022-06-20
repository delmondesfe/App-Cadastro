from email.mime import base
import psycopg2
from faker import Faker

con = psycopg2.connect(host='172.17.0.3',
                            database='aplication',
                            user='postgres',
                            password='270495')

cur = con.cursor()

fake = Faker(locale='pt-br')


base_sql = '''
    insert into seguidores
        (nome, email, usuario)
    values
        ('{}','{}','{}')
'''

for i in range(500):
    nome = fake.name()
    email = fake.email()
    usuario = fake.user_name()
    sql = base_sql.format(nome, email, usuario)
    print('Inserindo dados na tabela ...')
    cur.execute(sql)

con.commit()
con.close()