import psycopg2

#Fazendo a conexão com o banco de dados
con = psycopg2.connect(
    host='localhost',
    database='MrPandous_database',
    user='postgres',
    password='pabd',
    options='-c search_path=dbo,blog'
)

#Curso da conexão
cur = con.cursor()