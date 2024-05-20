import tkinter as tk
from tkinter import ttk
import sqlite3

def criar_tabela():
    conn = sqlite3.connect('informacoes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (id INTEGER PRIMARY KEY, nome TEXT, email TEXT, telefone TEXT)''')
    conn.commit()
    conn.close()

def salvar_informacoes():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    conn = sqlite3.connect('informacoes.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
    conn.commit()
    conn.close()

    print("Informações salvas com sucesso!")

def visualizar_informacoes():
    conn = sqlite3.connect('informacoes.db')
    cursor = conn.cursor()

    janela_tabela = tk.Toplevel()
    janela_tabela.title("Informações Cadastradas")
    janela_tabela.geometry("400x300")

    tabela = ttk.Treeview(janela_tabela, columns=("Nome", "Email", "Telefone"), show="headings")
    tabela.heading("Nome", text="Nome")
    tabela.heading("Email", text="Email")
    tabela.heading("Telefone", text="Telefone")

    cursor.execute("SELECT * FROM usuarios")
    for row in cursor.fetchall():
        tabela.insert("", "end", values=row[1:])

    tabela.pack(padx=10, pady=10, fill="both", expand=True)

    conn.close()

# Criar janela
janela = tk.Tk()
janela.title("Inserir e Visualizar Informações")
janela.geometry("400x200")
janela.configure(bg="#f0f0f0")

# Criar e posicionar widgets
label_nome = tk.Label(janela, text="Nome:", bg="#f0f0f0")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(janela, text="Email:", bg="#f0f0f0")
label_email.grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_telefone = tk.Label(janela, text="Telefone:", bg="#f0f0f0")
label_telefone.grid(row=2, column=0, padx=10, pady=5)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

botao_salvar = tk.Button(janela, text="Salvar Informações", command=salvar_informacoes)
botao_salvar.grid(row=3, column=0, columnspan=2, pady=10)

botao_visualizar = tk.Button(janela, text="Visualizar Informações", command=visualizar_informacoes)
botao_visualizar.grid(row=4, column=0, columnspan=2, pady=10)

# Criar tabela no banco de dados
criar_tabela()

# Executar aplicação
janela.mainloop()
