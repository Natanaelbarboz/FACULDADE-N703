from tkinter import Tk, Frame, ttk
import pandas as pd
from pymongo import MongoClient
from update import on_tree_select
from login import pessoas

# Variável global para armazenar a Treeview
tree = None

def def_get(frame, pessoas):
    global tree  

    # Ler credenciais
    # with open('../.gitignore', 'r') as arquivo:
    #     usuario, senha = [linha.strip() for linha in arquivo.readlines()]

    # # Conectar ao MongoDB
    # uri = f'mongodb+srv://{usuario}:{senha}@n703.dfo9g.mongodb.net/?retryWrites=true&w=majority&appName=N703'
    # client = MongoClient(uri)
    # db = client['N703-WEB-SERVICE']
    # pessoas = db['Pessoas']

    # Pegar os dados do MongoDB
    dic = list(pessoas.find())  # Buscar todos os documentos

    # Converter _id para string
    for doc in dic:
        doc["_id"] = str(doc["_id"])  

    base = pd.DataFrame(dic)

    # Renomear _id para ID
    if '_id' in base.columns:
        base.rename(columns={'_id': 'ID'}, inplace=True)

    # Ajustar a ordem das colunas
    if {'ID', 'Nome', 'Idade', 'Contato'}.issubset(base.columns):
        base = base[['ID', 'Nome', 'Idade', 'Contato', 'Rua', 'Bairro', 'Cidade']]
    else:
        print("Erro: Algumas colunas esperadas não foram encontradas!")
        return  

    # Criar a Treeview apenas uma vez
    if tree is None:
        tree = ttk.Treeview(frame, columns=list(base.columns), show="headings")

        # Criar cabeçalhos das colunas
        for col in base.columns:
            tree.heading(col, text=col)
            tree.column(col, width=150 if col == "ID" else 100)  # Deixar a coluna ID um pouco maior

        tree.pack(expand=True, fill="both")

        # Vincular evento de clique à função on_tree_select
        tree.bind("<ButtonRelease-1>", lambda event: on_tree_select(event, tree))

    # Atualizar os dados da Treeview
    for i in tree.get_children():
        tree.delete(i)

    for _, row in base.iterrows():
        tree.insert("", "end", values=list(row))

    # print("Tabela atualizada com sucesso!")

    # Atualizar a cada 5 segundos
    frame.after(5000, lambda: def_get(frame, pessoas))