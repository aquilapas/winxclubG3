from os.path import exists
import time
import csv

class Cliente():
    # def ler_dados(self, id=1, count=0):
    #     file1 = open(f"clients-00{id}.csv", "r", encoding = 'utf8')
    #     #print(f"========== lendo arquivo client_00{id}.csv ===========")
    #     time.sleep(2)

    #     while True:
    #         count += 1
    #         line = file1.readline()
    #         if not line:
    #             break
    #         print("Line {}: {}".format(count, line.strip()))
    #     file1.close()

    #     if exists(f"clients-00{(id+1)}.csv"):
    #         self.ler_dados(id+1, count)

    def salvar_csv(self, id=1, count=0):
        # 1. cria o arquivo
        f = open('clientes.csv', 'a', newline='', encoding='utf-8')
        file1 = open(f"clients-00{id}.csv", "r", encoding = 'utf8')

        # 3. grava as linhas
        for i in file1:
            f.write(i)
        
        # Recomendado: feche o arquivo
        f.close() 
        file1.close()
        if exists(f"clients-00{(id+1)}.csv"):
            self.salvar_csv(id+1, count)

cliente_teste = Cliente()
#cliente_teste.ler_dados()
cliente_teste.salvar_csv()
