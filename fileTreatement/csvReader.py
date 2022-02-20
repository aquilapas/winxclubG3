from os.path import exists
import sys
import time
import pandas as pd
#from ..db_connection.sql_server_connect.handlerDatabase import *



#treat numbers to match with file description
def treatNum(num, size=3):
    num = str(num)
    return num.zfill(size)



#read files from data directory
def preparaDados(id, file, fields):
    print(f"VERIFICAÇÃO E TRATAMENTO DE DADOS EM {file}.csv")
    fields = fields.replace(";", ",")    
    idx=treatNum(id)       
    filename = file+idx+".csv"
    try: 
        file1 = open(filename, 'r+', encoding='utf8')
        print(f"======= lendo arquivo {filename} =========")
        
        time.sleep(1)
        count = 0
        new_file_content = ""
        while True:
            count += 1
            line = file1.readline()

            if not line:
                file1.close()
                file1 = open(filename, "w", encoding='utf8')
                file1.write(new_file_content)
                break    

            new_line = line.strip()
            if (count == 1):
                new_line = fields                
            else:
                new_line = new_line.replace(";", ",")
            new_file_content += new_line +"\n"
                #print("Line {}: {}\n".format(count,line.strip())) 
        file1.close()
    except:
        print(f"Erro ao tentar carregar dados de {filename} ")
        print("Continuando execução....\n\n")
        time.sleep(0)

    idx=treatNum(id+1)
    filename = file+idx+".csv"
    if exists(filename): 
            preparaDados(id+1, file, fields)
    print(f"{file}.csv está pronto para carregamento na base de dados")


# read data to load to database
def carregarDados(id, file):
    print(f"Carregando dados de {file}.csv")  
    idx=treatNum(id)       
    filename = file+idx+".csv"
    try: 
        file1 = open(filename, 'r', encoding='utf8')
        print(f"======= lendo arquivo {filename} =========")        
        time.sleep(1)
        count = 0
        while True:
            count += 1
            line = file1.readline()
            if not line:
                break   

            print("Line {}: {}\n".format(count,line.strip())) 
        file1.close()
    except:
        print(f"Erro ao tentar carregar dados de {filename} ")
        print("Continuando execução....\n\n")
        time.sleep(0)

    idx=treatNum(id+1)
    filename = file+idx+".csv"
    if exists(filename): 
            carregarDados(id+1, file)    