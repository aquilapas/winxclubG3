import pandas as pd
import pyodbc

# importando csv
clientes_df = pd.read_csv(r'C:\Users\Acer\Desktop\desafio_accenture\clientes.csv', sep = ';')
clientes = pd.DataFrame(clientes_df)

transaction_in_df = pd.read_csv(r'C:\Users\Acer\Desktop\desafio_accenture\transaction_in.csv', sep = ';')
transaction_in = pd.DataFrame(transaction_in_df)

transaction_out_df = pd.read_csv(r'C:\Users\Acer\Desktop\desafio_accenture\transaction_out.csv', sep = ';')
transaction_out = pd.DataFrame(transaction_out_df)

# Conectando SQL Server
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-GSPLJUA;DATABASE=migracao;Trusted_Connection=yes;')

cursor=connection.cursor()

# Criando Tabela
cursor.execute('''
		CREATE TABLE clientes (
			id int primary key,
			nome varchar(200),
            email varchar(200),
            data_cadastro varchar(200),
			telefone varchar(100)
			)
            ''')

cursor.execute('''
		CREATE TABLE transaction_in (
			id int primary key,
			cliente_id int,
            valor float,
            data varchar(200),
			)
            ''')

cursor.execute('''
		CREATE TABLE transaction_out (
			id int primary key,
			cliente_id int,
            valor float,
            data varchar(200),
			)
            ''')

# insiro dados no banco
for index, row in clientes.iterrows():
    print(index, row)
    cursor.execute('''
    insert into clientes(id, nome, email, data_cadastro, telefone)
    values(?, ?, ?, ?, ?)''',
    row.id,
    row.nome,
    row.email,
    row.data_cadastro,
    row.telefone)

for index, row in transaction_in.iterrows():
    cursor.execute('''
    insert into transaction_in(id, cliente_id, valor, data)
    values(?, ?, ?, ?)''',
    row.id,
    row.cliente_id,
    row.valor,
    row.data)

for index, row in transaction_out.iterrows():
    cursor.execute('''
    insert into transaction_out(id, cliente_id, valor, data)
    values(?, ?, ?, ?)''',
    row.id,
    row.cliente_id,
    row.valor,
    row.data)

connection.commit()

# busco dados no banco
# dados_clientes = cursor.execute("SELECT * from clientes")
# while 1:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print("-------------------")
#     print(f"Texto: {row}")

cursor.close()
connection.close()