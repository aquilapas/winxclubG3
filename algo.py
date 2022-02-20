from os.path import exists
import time
import pyodbc

# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=SAMSUNG\MSSQLSERVER01;DATABASE=teste;Trusted_Connection=yes;')

cursor=connection.cursor()
print('Conectou no banco')

def treatNum(num, size=3):
    num = str(num)
    return num.zfill(size)

def lerDados(id, file):    
    idx=treatNum(id)       
    filename = file+idx+".csv"
    try: 
        file1 = open(filename, 'r', encoding="utf-8")
        print(f"======= lendo arquivo {filename} =========")
        
        time.sleep(2)
        count = 0
        while True:
            count += 1
            line = file1.readline()
            if not line:
                break
            if count > 1 :#pula a primeira linha
                dados = line.split(';')
                if file == 'clients-':
                    #insere dados na tabela já criada manualmente no sql
                    cursor.execute("INSERT INTO Clients(id, nome, email, data_cadastro, telefone) VALUES (?, ?, ?, ?, ?)", dados[0], dados[1], dados[2], str(dados[3]), dados[4])
                    connection.commit()
                elif file == 'transaction-in-':
                    cursor.execute("INSERT INTO Transaction_In(id, cliente_id, valor, data) VALUES (?, ?, ?, ?)", dados[0], dados[1], dados[2], str(dados[3]))
                    connection.commit()
                else:
                    cursor.execute("INSERT INTO Transaction_Out(id, cliente_id, valor, data) VALUES (?, ?, ?, ?)", dados[0], dados[1], dados[2], str(dados[3]))
                    connection.commit()
                print('Dados carregados')
            #print("Line {}: {}".format(count,line.strip())) 
            
        file1.close()
    except:
        print(f"Erro ao tentar carregar dados de {filename} ")
        print("Continuando execução....\n\n")
        time.sleep(1)

    idx=treatNum(id+1)
    filename = file+idx+".csv"
    if exists(filename): 
            lerDados(id+1, file)

lerDados(1, 'clients-')
#lerDados(1, 'transaction-in-')
#lerDados(1, 'transaction-out-')


# Here's something to get you going in the right direction.

# with open('path/to/filename') as filehandler_name:
#     # this is how you open a file for reading

# with open('path/to/filename', 'w') as filehandler_name:
#     # this is how you open a file for (over)writing
#     # note the 'w' argument to the open built-in

# import csv
# # this is the module that handles csv files

# reader = csv.reader(filehandler_name)
# # this is how you create a csv.reader object
# writer = csv.writer(filehandler_name)
# # this is how you create a csv.writer object

# for line in reader:
#     # this is how you read a csv.reader object line by line
#     # each line is effectively a list of the fields in that line
#     # of the file.
#     # # XXXX-XXXX, 0 --> ['XXXX-XXXX', '0']
# # For small files, you could do something like:

# # import csv

# # with open('path/to/filename') as inf:
# #     reader = csv.reader(inf.readlines())

# # with open('path/to/filename', 'w') as outf:
# #     writer = csv.writer(outf)
# #     for line in reader:
# #         if line[1] == '0':
# #             writer.writerow(line[0], '1')
# #             break
# #         else:
# #             writer.writerow(line)
# #     writer.writerows(reader)

# # new_file_content = ""
# # for line in reading_file:
# #   stripped_line = line.strip()
# #   new_line = stripped_line.replace("old string", "new string")
# #   new_file_content += new_line +"\n"
# # reading_file.close()

# # writing_file = open("sample.txt", "w")
# # writing_file.write(new_file_content)
# # writing_file.close()
