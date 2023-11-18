import sqlite3
conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()
a_nome = 'lucas rodegheri'
a_id = 3
sql = """
 update clientes
 set nome = ?
 where id = ?
"""
cursor.execute(sql, [a_nome, a_id])
conexao.commit()
conexao.close()