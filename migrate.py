from os.path import exists
import time
import pyodbc

def converterData(data):#converte a data para ser aceita como datetime no sql (desconsiderando o -03:00 do fuso horário)
    data1 = data[:10]
    data2 = data[11:19]
    return data1+'T'+data2

def importaDados(file, line, count, id):#insere dados na tabela já criada manualmente no sql
    dados = line.split(';')
    if file == 'clients-':
        if id == 1 and count == 1:
            pass
        else: 
            cursor.execute("INSERT INTO Clients(id, nome, email, data_cadastro, telefone) VALUES (?, ?, ?, ?, ?)", dados[0], dados[1], dados[2], converterData(dados[3]), dados[4])
            connection.commit()
    if file == 'transaction-in-':
        if id == 1 and count == 1:
            pass
        else: 
            cursor.execute("INSERT INTO Transaction_In(id, cliente_id, valor, data) VALUES (?, ?, ?, ?)", dados[0], dados[1], dados[2], converterData(dados[3]))
            connection.commit()
    if file == 'transaction-out-':
        if id == 1 and count == 1:
            pass
        else:
            cursor.execute("INSERT INTO Transaction_Out(id, cliente_id, valor, data) VALUES (?, ?, ?, ?)", dados[0], dados[1], dados[2], converterData(dados[3]))
            connection.commit()
    print('Dados carregados')

def treatNum(num, size=3):
    num = str(num)
    return num.zfill(size)

def lerDados(id, file):    
    idx=treatNum(id)       
    filename = file+idx+".csv"
    file1 = open(filename, 'r', encoding="utf-8")
    print(f"======= lendo arquivo {filename} =========")
    
    time.sleep(2)
    count = 0
    while True:
        count += 1
        line = file1.readline()
        if not line:
            break
        #print("Line {}: {}".format(count,line.strip()))
        importaDados(file, line, count, id) 
        
    file1.close()

    idx=treatNum(id+1)
    filename = file+idx+".csv"
    if exists(filename): 
            lerDados(id+1, file)

# Conexão com meu banco de dados
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=SAMSUNG\MSSQLSERVER01;DATABASE=teste;Trusted_Connection=yes;')

cursor=connection.cursor()
print('Conectou no banco')

lerDados(1, 'clients-')
lerDados(1, 'transaction-in-')
lerDados(1, 'transaction-out-')