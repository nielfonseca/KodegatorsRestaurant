import sqlite3
conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()
i_login = 'lucas broxa'
i_senha = 20
sql = """
 INSERT INTO clientes (login, senha)
 VALUES (?, ?)
"""
cursor.execute(sql, [i_login, i_senha])
conexao.commit()
conexao.close()
