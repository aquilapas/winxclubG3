import os
import pyodbc
import pandas as pd

'''exemplo de como importar funções de outro arquivo (modularização do programa)'''
from fileTreatement.csvReader import preparaDados


'''Treat data'''
preparaDados(1, 'data/clients-', 'id,nome,email,data_cadastro,telefone')
preparaDados(1,'data/transaction-in-' , 'id,cliente_id,valor,data')
preparaDados(1, 'data/transaction-out-', 'id,cliente_id,valor,data')


'''Connect to database SQL AZURE'''
try:
    connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:servidorsqldesafio.database.windows.net,1433;Database=mov_bancarias;Uid=flaviascarlate;Pwd=12345Ab!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=3000;')
    cursor=connection.cursor()

    '''Create Tables'''
    print('Criando as tabelas para recebimento de dados')

    '''TABELA CLIENTES'''
    if cursor.tables(table='clients', tableType='TABLE').fetchone():
        print("TABELA CLIENTE JÁ EXISTE - IGNORANDO CRIAÇÃO")

    else:
        print("CRIANDO TABELA CLIENTS")
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
        print(f"TABELA TRANSACTION IN JÁ EXISTE - IGNORANDO CRIAÇÃO")
    else:
        print(f"CRIANDO TABELA TRANSACTION IN")
        cursor.execute('''
            CREATE TABLE transaction_in ( 
                id int primary key, 
                cliente_id int, 
                valor float,			
                data datetime
                ) 
                    ''')

    '''TABELA TRANSACTION OUT'''
    if cursor.tables(table='transaction_out', tableType='TABLE').fetchone():
        print("TABELA TRANSACTION OUT JÁ EXISTE - IGNORANDO CRIAÇÃO")
    else:
        print("CRIANDO TABELA TRANSACTION OUT")
        cursor.execute('''
            CREATE TABLE transaction_out ( 
                id int primary key, 
                cliente_id int, 
                valor float,			
                data datetime
                ) 
                    ''')
    connection.commit()


    '''Send data to tables'''

    file_list=os.listdir(r'data')
    '''Send data to clients'''
    print("Inserindo dados de:")
    for item in file_list:
        if 'client' in item:
            get_fileName = "data/" + item
            print(get_fileName)        
            data = pd.read_csv(get_fileName)   
            df = pd.DataFrame(data)
            df = df.astype({'data_cadastro':'datetime64[ns]'})
            print(df)

            for row in df.itertuples(): 

                try:
                    cursor.execute('''
                            INSERT INTO clients (id, nome, email, data_cadastro, telefone)
                            VALUES (?,?,?,?,?)
                            ''',
                            row.id, 
                            row.nome,
                            row.email,
                            row.data_cadastro,
                            row.telefone,
                            )
                except:
                        is_Field_exists_query = f"SELECT id FROM clients WHERE id = '{row.id}'"
                        cursor.execute(is_Field_exists_query)
                        results = cursor.fetchone()
                        connection.commit()

                        if len(results) >=1:
                            print(f'Conflito com id já existente. Ignorando inserção de dados em {row.id}')
                        else:
                            print (f"Houve erro crítico durante tentativa de inserção de dados de {row.id} na base de dados")
                connection.commit()
        else:
            pass

    for item_transaction_in in file_list:
        if 'in' in item_transaction_in:
            get_fileName = "data/" + item_transaction_in
            print(get_fileName)       
            data = pd.read_csv(get_fileName)   
            df = pd.DataFrame(data)
            df = df.astype({'data':'datetime64[ns]'})
            print(df)
            
            for row in df.itertuples(): 

                try:
                    cursor.execute('''
                            INSERT INTO transaction_in (id, cliente_id, valor, data)
                            VALUES (?,?,?,?)
                            ''',
                            row.id, 
                            row.cliente_id,
                            row.valor,
                            row.data
                            )
                except:
                        is_Field_exists_query = f"SELECT id FROM transaction_in WHERE id = '{row.id}'"
                        cursor.execute(is_Field_exists_query)
                        results = cursor.fetchone()
                        connection.commit()
                        if len(results) >=1:
                            print(f'Conflito com id já existente. Ignorando inserção de dados em {row.id}')
                        else:
                            print (f"Houve erro crítico durante tentativa de inserção de dados de id:{row.id} em {get_fileName} na base de dados")
                connection.commit()
        else:
            pass

    for item_transaction_out in file_list:
        if 'out' in item_transaction_out:
            get_fileName = "data/" + item_transaction_out
            print(get_fileName)        
            data = pd.read_csv(get_fileName)   
            df = pd.DataFrame(data)
            df = df.astype({'data':'datetime64[ns]'}) 
            print(df)

            for row in df.itertuples(): 

                try:
                    cursor.execute('''
                            INSERT INTO transaction_out (id, cliente_id, valor, data)
                            VALUES (?,?,?,?)
                            ''',
                            row.id, 
                            row.cliente_id,
                            row.valor,
                            row.data
                            )
                except:
                        is_Field_exists_query = f"SELECT id FROM transaction_out WHERE id = '{row.id}'"
                        cursor.execute(is_Field_exists_query)
                        results = cursor.fetchone()
                        connection.commit()
                        if len(results) >=1:
                            print(f'Conflito com id já existente. Ignorando inserção de dados em {row.id}')
                        else:
                            print (f"Houve erro crítico durante tentativa de inserção de dados de {row.id} na base de dados")
                connection.commit()
        else:
            pass

except NameError as err:
    print(f"Houve um erro durante tentativa de conexão com base de dados SQL Server.\n {err}")


