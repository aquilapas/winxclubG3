import os
import sys
import pyodbc
import pandas as pd
import time

'''exemplo de como importar funções de outro arquivo(modularização do programa)'''
from fileTreatement.csvReader import preparaDados

'''Treat data''' 
# preparaDados(1, 'data/clients-', 'id,nome,email,data_cadastro,telefone')
# preparaDados(1,'data/transaction-in-' , 'id,cliente_id,valor,data')
# preparaDados(1, 'data/transaction-out-', 'id,cliente_id,valor,data')

'''Connect to database'''
try:
#  cursor = connectToSQLServer()
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLEXPRESS;DATABASE=banco_teste;Trusted_Connection=yes;')
    cursor=connection.cursor()
except:
    print(f"Houve um erro durante tentativa de conexão com base de dados SQL Server")

'''Create Tables'''

print('Criação de tabelas para recebimento de dados')
time.sleep(1)

'''TABELA CLIENTES'''
if cursor.tables(table='clients', tableType='TABLE').fetchone():
    print("TABELA CLIENTE JÁ EXISTE - IGNORANDO CRIAÇÃO")
    time.sleep(1)
else:
    cursor.execute('''
		CREATE TABLE clients ( 
			id int primary key, 
			nome varchar(100), 
            email varchar (100),
			data_cadastro datetimeoffset,
            telefone varchar (18)
			) 
                ''')
                
'''TABELA TRANSACTION IN'''
if cursor.tables(table='transaction_in', tableType='TABLE').fetchone():
    print("TABELA TRANSACTION IN JÁ EXISTE - IGNORANDO CRIAÇÃO")
else:
    cursor.execute('''
		CREATE TABLE transaction_in ( 
			id int primary key, 
			cliente_id int, 
            valor float,			
            Data datetimeoffset
			) 
                ''')

'''TABELA TRANSACTION OUT'''
if cursor.tables(table='transaction_out', tableType='TABLE').fetchone():
    print("TABELA TRANSACTION OUT JÁ EXISTE - IGNORANDO CRIAÇÃO")
else:
    cursor.execute('''
		CREATE TABLE transaction_out ( 
			id int primary key, 
			cliente_id int, 
            valor float,			
            Data datetime
			) 
                ''')
connection.commit()
'''Send data to tables'''

data = pd.read_csv(r'data\clients-001.csv')   
df = pd.DataFrame(data)
print(df['data_cadastro'][1][:19])
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO clients (id, nome, email, data_cadastro, telefone)
                VALUES (?,?,?,?,?)
                ''',
                row.id, 
                row.nome,
                row.email,
                row.data_cadastro[:19],
                row.telefone,
                )
connection.commit()