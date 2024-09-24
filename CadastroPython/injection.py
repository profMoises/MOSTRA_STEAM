import mysql.connector

# Conexão com o banco de dados (segura)
conexao = mysql.connector.connect(
    host='localhost',
    database='sistema_produtos',
    user='root',
    password=''
)

cursor = conexao.cursor()

# Entrada do usuário (que será tratada de forma segura)
nome_produto = input("Digite o nome do produto: ")

# Usando SQL parametrizado para evitar SQL Injection
query = "SELECT * FROM produtos WHERE nome = %s"
cursor.execute(query, (nome_produto,))  # O %s será substituído pelo valor de forma segura

# Exibe os resultados
for produto in cursor.fetchall():
    print(produto)

cursor.close()
conexao.close()
