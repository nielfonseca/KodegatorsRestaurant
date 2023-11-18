import sqlite3
conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()
cursor.execute('''select * from clientes;''')
resultado = cursor.fetchall()
for i in resultado:
 print(i)
conexao.close()