import tkinter as tk
from tkinter import messagebox
from db_operations import Database

class Interface:
    def __init__(self, root):
        self.root = root
        self.db = Database()

        # Criando os widgets da interface
        self.label_title = tk.Label(root, text="Cadastro de Produtos", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        # Formulário para Inserir e Atualizar Produto
        self.label_nome = tk.Label(root, text="Nome do Produto")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_preco = tk.Label(root, text="Preço do Produto")
        self.label_preco.pack()
        self.entry_preco = tk.Entry(root)
        self.entry_preco.pack()

        self.label_quantidade = tk.Label(root, text="Quantidade")
        self.label_quantidade.pack()
        self.entry_quantidade = tk.Entry(root)
        self.entry_quantidade.pack()

        # Botão de Inserção
        self.btn_inserir = tk.Button(root, text="Inserir Produto", command=self.inserir_produto)
        self.btn_inserir.pack(pady=5)

        # Formulário para Atualização/Exclusão
        self.label_id = tk.Label(root, text="ID do Produto (para atualizar/excluir)")
        self.label_id.pack()
        self.entry_id = tk.Entry(root)
        self.entry_id.pack()

        # Botões de Atualizar e Excluir
        self.btn_atualizar = tk.Button(root, text="Atualizar Produto", command=self.atualizar_produto)
        self.btn_atualizar.pack(pady=5)

        self.btn_deletar = tk.Button(root, text="Deletar Produto", command=self.deletar_produto)
        self.btn_deletar.pack(pady=5)

        # Área de exibição de produtos cadastrados
        self.label_lista = tk.Label(root, text="Produtos Cadastrados")
        self.label_lista.pack(pady=10)
        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack()

        # Atualiza a lista de produtos ao iniciar
        self.listar_produtos()

    def inserir_produto(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        quantidade = self.entry_quantidade.get()

        if not nome or not preco or not quantidade:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos")
            return

        try:
            preco = float(preco)
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser numérico e quantidade deve ser inteiro")
            return

        self.db.inserir_produto(nome, preco, quantidade)
        self.limpar_campos()
        self.listar_produtos()

    def atualizar_produto(self):
        id = self.entry_id.get()
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        quantidade = self.entry_quantidade.get()

        if not id or not nome or not preco or not quantidade:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos")
            return

        try:
            id = int(id)
            preco = float(preco)
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "ID deve ser numérico, preço deve ser numérico e quantidade deve ser inteiro")
            return

        self.db.atualizar_produto(id, nome, preco, quantidade)
        self.limpar_campos()
        self.listar_produtos()

    def deletar_produto(self):
        id = self.entry_id.get()

        if not id:
            messagebox.showwarning("Erro", "O campo ID deve ser preenchido")
            return

        try:
            id = int(id)
        except ValueError:
            messagebox.showerror("Erro", "ID deve ser numérico")
            return

        self.db.deletar_produto(id)
        self.limpar_campos()
        self.listar_produtos()

    def listar_produtos(self):
        produtos = self.db.ler_produtos()
        self.text_area.delete('1.0', tk.END)
        for produto in produtos:
            self.text_area.insert(tk.END, f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]:.2f}, Quantidade: {produto[3]}\n")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)
