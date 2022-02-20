import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLEXPRESS;DATABASE=migracao2;Trusted_Connection=yes;')

cursor=connection.cursor()

#insiro dados no banco
cursor.execute("insert into importacao(texto) values ('teste python')")
connection.commit()

# # busco dados no banco
# dados=cursor.execute("SELECT * FROM importacao")


# while 1:
#     row = cursor.fetchone()
#     if not row:
#         break

#     print("----------")
#     print(f"texto: {row.texto}")

    
cursor.close()
connection.close()
