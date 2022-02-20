'''TODO ---------------------------------------------------------------- EVERTYHING, LOL'''
import os
import sys
import pandas as pd

#exemplo de como importar funções de outro arquivo(modularização do programa)
from fileTreatement.csvReader import preparaDados
from db_connection.sql_server_connect.handlerDatabase import *

# Treat data
preparaDados(1, 'data/clients-', 'id,nome,email,data_cadastro,telefone')
preparaDados(1,'data/transaction-in-' , 'id,cliente_id,valor,data')
preparaDados(1, 'data/transaction-out-', 'id,cliente_id,valor,data')

# Connect to database


# Create Tables


# Send data to tables

# data = pd.read_csv(r'data\transaction-out-001.csv')   
# df = pd.DataFrame(data)

# print(df['data'])
