import sqlite3
conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()
d_id = 3
sql = """
 delete from clientes
 where id = ?;
"""
cursor.execute(sql, [d_id])
conexao.commit()
conexao.close()