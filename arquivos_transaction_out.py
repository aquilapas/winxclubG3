from os.path import exists
import time

class Transaction_out ():
    def treat_num(self, num, size=3):
        num = str(num)
        return num.zfill(size)

    def ler_dados(self, id, file):
        idx=self.treat_num(id)
        filename = file+idx+".csv"
        try:
            file1 = open(filename, "r", encoding = 'utf8')
            #print(f"========== lendo arquivo {filename} ===========")

            time.sleep(2)
            count = 0
            while True:
                count += 1
                line = file1.readline()
                if not line:
                    break
                print("Line {}: {}\n".format(count, line.strip()))
            file1.close()
        except:
            print(f"Erro ao tentar carregar dados de {filename}")
            print("Continuação execução...\n\n")
            time.sleep(1)
        
        idx = self.treat_num(id+1)
        filename=file+idx+".csv"

        if exists(filename):
            self.ler_dados(id+1, file)

    def salvar_csv(self, id, file):
        # 1. cria o arquivo
        def treat_num(self, num, size=3):
            num = str(num)
            return num.zfill(size)
        idx=self.treat_num(id)
        filename = file+idx+".csv"
        f = open('transaction_out.csv', 'a', newline='', encoding='utf-8')
        file1 = open(filename, "r", encoding = 'utf8')

        # 3. grava as linhas
        for i in file1:
            f.write(i)
        
        # Recomendado: feche o arquivo
        f.close() 
        file1.close()
        if exists(filename):
            self.salvar_csv(id+1, file)

transaction_out = Transaction_out()
#transaction_out.ler_dados(1, 'transaction-out-')
transaction_out.salvar_csv(1, 'transaction-out-')
