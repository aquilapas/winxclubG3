import pyodbc 
import pandas as pd

#Conectar ao SQL
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLEXPRESS;DATABASE=mov_bancarias;Trusted_Connection=yes;')

cursor=connection.cursor()




# #Importar
# data = pd.read_csv (r"C:/Users/f_sca/Desktop/python_desafio/arquivos_csv/clients-001.csv")   
# df = pd.DataFrame(data)

# print(df)

# #Criar tabela
# cursor.execute('''
# 		CREATE TABLE clients ( 
# 			id int primary key, 
# 			nome varchar(100), 
#             email varchar (100),
# 			data_cadastro datetime,
#             telefone varchar (11),
# 			) 
#                 ''')

# # Insira DataFrame na tabela 
# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO products (id, nome, email, data_cadastro, telefone)
#                 VALUES (?,?,?,?,?)
#                 ''',
#                 row.id, 
#                 row.nome,
#                 row.email,
#                 row.data_cadastro,
#                 row.telefone,
#                 )
# connection.commit()


def connectToMySQL():
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLEXPRESS;DATABASE=mov_bancarias;Trusted_Connection=yes;')
    cursor=connection.cursor()
    return cursor

