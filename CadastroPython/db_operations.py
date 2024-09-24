import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            # Conexão ao banco de dados MySQL
            self.conexao = mysql.connector.connect(
                host='localhost',
                database='sistema_produtos',
                user='root',
                password=''
            )
            if self.conexao.is_connected():
                print("Conectado ao banco de dados.")
        except Error as e:
            print("Erro ao conectar ao banco de dados", e)

    def inserir_produto(self, nome, preco, quantidade):
        try:
            cursor = self.conexao.cursor()
            sql = "INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)"
            valores = (nome, preco, quantidade)
            cursor.execute(sql, valores)
            self.conexao.commit()
            print(f"Produto '{nome}' inserido com sucesso!")
        except Error as e:
            print("Erro ao inserir produto", e)

    def ler_produtos(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM produtos")
            produtos = cursor.fetchall()
            return produtos
        except Error as e:
            print("Erro ao ler produtos", e)
            return []

    def atualizar_produto(self, id, nome, preco, quantidade):
        try:
            cursor = self.conexao.cursor()
            sql = "UPDATE produtos SET nome=%s, preco=%s, quantidade=%s WHERE id=%s"
            valores = (nome, preco, quantidade, id)
            cursor.execute(sql, valores)
            self.conexao.commit()
            print(f"Produto ID {id} atualizado com sucesso!")
        except Error as e:
            print("Erro ao atualizar produto", e)

    def deletar_produto(self, id):
        try:
            cursor = self.conexao.cursor()
            sql = "DELETE FROM produtos WHERE id=%s"
            valores = (id,)
            cursor.execute(sql, valores)
            self.conexao.commit()
            print(f"Produto ID {id} excluído com sucesso!")
        except Error as e:
            print("Erro ao deletar produto", e)

    def fechar_conexao(self):
        if self.conexao.is_connected():
            self.conexao.close()
            print("Conexão com o banco de dados encerrada.")
