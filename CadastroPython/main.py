import tkinter as tk
from interface import Interface

# Inicializa a janela principal
root = tk.Tk()
root.title("Sistema de Cadastro de Produtos")
root.geometry("600x500")

# Inicializa a interface
app = Interface(root)

# Inicia o loop da aplicação
root.mainloop()
