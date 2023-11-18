class meu_banco:
    def __init__(self, banco):
        import sqlite3
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def fecharDB(self):
        self.conexao.close()

    def criarTabela(self):
        sql = """
        CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Login TEXT NOT NULL,
        Senha INTEGER
        );
        """
        self.cursor.execute(sql)
        print('Tabela criada...')

        

    #ler tabela
    def selecionar(self):
        sql = """
            SELECT * FROM clientes;
        """
        resultado = self.cursor.execute(sql)

        return resultado.fetchall()

            
    

        #inserir registro
    def inserir(self,login,senha):
        
        sql = """
        INSERT INTO clientes (login, senha)
        VALUES (?, ?)
        """
        self.cursor.execute(sql, (login,senha))
        self.conexao.commit()
      

        #alterar registro
    def alterar(self, id, login,senha):
        
        sql = """
        update clientes
        set login = ?, senha = ?
        where id = ?
        """
        self.cursor.execute(sql, (login,senha,id))
        self.conexao.commit()


        #Deletar registro
    def deletar(self,id):

        sql = """
        delete from clientes
        where id = ?;
        """
        self.cursor.execute(sql,(id))
        self.conexao.commit()

