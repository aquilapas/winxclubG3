import pandas as pd
import pyodbc
import pymysql.cursors

# data = pd.read_csv (r'C:\Users\f_sca\Desktop\python_desafio\arquivos_csv\products.csv')    
# df = pd.DataFrame(data) 

# print(df)

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(server='.\SQLEXPRESS',
                             user='',
                             password='',
                             database='banco_teste',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)



# # Conectar ao SQL Server 
# conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 
#                       'Server=.\SQLEXPRESS;' 
#                       'Database=banco_teste;' 
#                       'Trusted_Connection=yes;') 
# cursor = conn.cursor() 

# # Create Table
# # cursor.execute('''
# #             CREATE TABLE products (
# #                 product_id int primary key,
# #                 product_name nvarchar(50),
# #                 price int
# #                 )
# #             ''')

# # df[['product_id', 'product_name', 'price']].astype(str)
# # Insert DataFrame to Table
# for row in df.itertuples():
#     print(row.product_id, row.product_name, row.price)    
#     cursor.execute(
#                 '''
#                 INSERT INTO products (product_id, product_name, price)
#                 VALUES (?,?,?)
#                 ,
#                 row.product_id, 
#                 row.product_name,
#                 row.price
#                 ''')
# conn.commit()