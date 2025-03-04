from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import customtkinter as ctk

from pymongo import MongoClient
from bson import ObjectId

from pop_up_selec_update import def_pop_up_update

index_value = None
nome = None
idade = None
contato = None

def on_tree_select(event, tree):
    global index_value, nome, idade, contato  # Declarando que estamos usando as variáveis globais

    selected_item = tree.focus()  # Obtém o item selecionado
    item_values = tree.item(selected_item, "values")
    
    if item_values:
        index_value = item_values[0]  # Agora realmente modifica a variável global
        nome = item_values[1]
        idade = item_values[2]
        contato = item_values[3]
        print(f"Índice selecionado: {index_value}")
        return index_value, nome, idade, contato
    
    return None, None, None, None

def def_update(root):

    def update(root, index_value, nome, idade, contato):

        root.withdraw()
    
        nome_var = ctk.StringVar(value=nome)
        idade_var = ctk.StringVar(value=idade)
        contato_var = ctk.StringVar(value=contato)

        frame = ctk.CTkToplevel()
        frame.title("Cadastro de clientes")
        frame.geometry("650x600")
        frame.resizable(False, False)

        ctk.CTkLabel(frame, text="NOME", width=150, font=("roboto", 14)).place(x=25, y=115)
        ctk.CTkLabel(frame, text="IDADE", width=150, font=("roboto", 14)).place(x=25, y=150)
        ctk.CTkLabel(frame, text="TEL + DDD", width=150, font=("roboto", 14)).place(x=25, y=185)

        label_nome = ctk.CTkEntry(frame, textvariable=nome_var, width=350, font=("roboto", 14))
        label_nome.place(x=200, y=115)

        label_idade = ctk.CTkEntry(frame, textvariable=idade_var, width=350, font=("roboto", 14))
        label_idade.place(x=200, y=150)

        label_contato = ctk.CTkEntry(frame, textvariable=contato_var, width=350, font=("roboto", 14))
        label_contato.place(x=200, y=185)

        def fechar_janela():
            frame.destroy()
            root.deiconify()

        frame.protocol("WM_DELETE_WINDOW", fechar_janela)

        def obter_valores():
            return nome_var.get(), idade_var.get(), contato_var.get()
        
        def salvar_e_atualizar():
            salvar()
            frame.after(750,fechar_janela())
            frame.after(1250, def_pop_up_update(root))

        def salvar():
            nome_editado, idade_editada, contato_editado = obter_valores()
            
            if not index_value:
                print("Erro: index_value indefinido!")
                return
            
            try:
                object_id = ObjectId(index_value)  # Converte para ObjectId
            except Exception as e:
                print(f"Erro ao converter index_value para ObjectId: {e}")
                return

            dados = {
                "Nome": nome_editado,
                "Idade": idade_editada,
                "Contato": contato_editado
            }

            with open('../.gitignore', 'r') as arquivo:
                linhas = arquivo.readlines()

            usuario = linhas[0].strip()
            senha = linhas[1].strip()
            
            uri = f'mongodb+srv://{usuario}:{senha}@n703.dfo9g.mongodb.net/?retryWrites=true&w=majority&appName=N703'
            client = MongoClient(uri)
            db = client['N703-WEB-SERVICE']
            pessoas = db['Pessoas']

            # Agora passamos um ObjectId correto para a consulta
            resultado = pessoas.update_one({"_id": object_id}, {"$set": dados})

            if resultado.modified_count > 0:
                print(f"Registro {index_value} atualizado com sucesso!")
            else:
                print(f"Nenhuma modificação feita para {index_value}.")

            client.close()


        btn_update = ctk.CTkButton(frame, text='SALVAR', command=salvar_e_atualizar)
        btn_update.place(x=50, y=500)

        btn_fechar = ctk.CTkButton(frame, text='FECHAR', command=fechar_janela)
        btn_fechar.place(x=200, y=500)

        frame.mainloop()

    update(root, index_value, nome, idade, contato)
    