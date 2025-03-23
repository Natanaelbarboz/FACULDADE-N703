from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import customtkinter as ctk

from pymongo import MongoClient
from bson import ObjectId

from pop_up_selec_update import def_pop_up_update
from login import pessoas
from pop_up_selec_vazia import def_pop_up_vazio

index_value = None
nome = None
idade = None
contato = None
rua = None
bairro = None
cidade = None

def on_tree_select(event, tree):
    global index_value, nome, idade, contato, rua, bairro, cidade  # Declarando que estamos usando as variáveis globais

    selected_item = tree.focus()  # Obtém o item selecionado
    item_values = tree.item(selected_item, "values")
    
    if item_values:
        index_value = item_values[0]  # Agora realmente modifica a variável global
        nome = item_values[1]
        idade = item_values[2]
        contato = item_values[3]
        rua = item_values[4]
        bairro = item_values[5]
        cidade = item_values[6]
        print(f"Índice selecionado: {index_value}")
        return index_value, nome, idade, contato, rua, bairro, cidade
    
    return None, None, None, None

def def_update(root, pessoas):

    def update(root, index_value, nome, idade, contato, rua, bairro, cidade):

        root.withdraw()
    
        nome_var = ctk.StringVar(value=nome)
        idade_var = ctk.StringVar(value=idade)
        contato_var = ctk.StringVar(value=contato)
        rua_var = ctk.StringVar(value=rua)
        bairro_var = ctk.StringVar(value=bairro)
        cidade_var = ctk.StringVar(value=cidade)

        frame = ctk.CTkToplevel()
        frame.title("ONG - VIDAS PET")
        frame.geometry("650x600")
        frame.resizable(False, False)

        sub_titulo = ctk.CTkLabel(frame, text="EDITAR AMIGO DOS PETS", font=("roboto", 18))
        sub_titulo.place(x=250, y=10)

        ctk.CTkLabel(frame, text="NOME", width=150, font=("roboto", 14)).place(x=25, y=115)
        ctk.CTkLabel(frame, text="IDADE", width=150, font=("roboto", 14)).place(x=25, y=150)
        ctk.CTkLabel(frame, text="CONTATO", width=150, font=("roboto", 14)).place(x=25, y=185)
        ctk.CTkLabel(frame, text="RUA", width=150, font=("roboto", 14)).place(x=25, y=220)
        ctk.CTkLabel(frame, text="BAIRRO", width=150, font=("roboto", 14)).place(x=25, y=255)
        ctk.CTkLabel(frame, text="CIDADE", width=150, font=("roboto", 14)).place(x=25, y=290)

        label_nome = ctk.CTkEntry(frame, textvariable=nome_var, width=350, font=("roboto", 14))
        label_nome.place(x=200, y=115)

        label_idade = ctk.CTkEntry(frame, textvariable=idade_var, width=350, font=("roboto", 14))
        label_idade.place(x=200, y=150)

        label_contato = ctk.CTkEntry(frame, textvariable=contato_var, width=350, font=("roboto", 14))
        label_contato.place(x=200, y=185)

        label_rua = ctk.CTkEntry(frame, textvariable=rua_var, width=350, font=("roboto", 14))
        label_rua.place(x=200, y=220)

        label_bairro = ctk.CTkEntry(frame, textvariable=bairro_var, width=350, font=("roboto", 14))
        label_bairro.place(x=200, y=255)

        label_cidade = ctk.CTkEntry(frame, textvariable=cidade_var, width=350, font=("roboto", 14))
        label_cidade.place(x=200, y=290)

        def fechar_janela():
            frame.destroy()
            root.deiconify()

        frame.protocol("WM_DELETE_WINDOW", fechar_janela)

        def obter_valores():
            return nome_var.get(), idade_var.get(), contato_var.get(), rua_var.get(), bairro_var.get(), cidade_var.get()
        
        def salvar_e_atualizar():
            if index_value is None:
                print("Erro: index_value indefinido!")
                def_pop_up_vazio(frame)
                return
            else:
                salvar()
                frame.after(750,fechar_janela())
                frame.after(1250, def_pop_up_update(root))

        def salvar():
            nome_editado, idade_editada, contato_editado, rua_editado, bairro_editado, cidade_editado = obter_valores()
            
            # if index_value is None:
            #     print("Erro: index_value indefinido!")
            #     return
                
            
            try:
                object_id = ObjectId(index_value)  # Converte para ObjectId
            except Exception as e:
                print(f"Erro ao converter index_value para ObjectId: {e}")
                return

            dados = {
                "Nome": nome_editado,
                "Idade": idade_editada,
                "Contato": contato_editado,
                "Rua":rua_editado,
                "Bairro":bairro_editado,
                "Cidade":cidade_editado
            }

            # with open('../.gitignore', 'r') as arquivo:
            #     linhas = arquivo.readlines()

            # usuario = linhas[0].strip()
            # senha = linhas[1].strip()
            
            # uri = f'mongodb+srv://{usuario}:{senha}@n703.dfo9g.mongodb.net/?retryWrites=true&w=majority&appName=N703'
            # client = MongoClient(uri)
            # db = client['N703-WEB-SERVICE']
            # pessoas = db['Pessoas']

            # Agora passamos um ObjectId correto para a consulta
            resultado = pessoas.update_one({"_id": object_id}, {"$set": dados})

            if resultado.modified_count > 0:
                print(f"Registro {index_value} atualizado com sucesso!")
            else:
                print(f"Nenhuma modificação feita para {index_value}.")

            # client.close()


        btn_update = ctk.CTkButton(frame, text='SALVAR', command=salvar_e_atualizar)
        btn_update.place(x=50, y=500)

        btn_fechar = ctk.CTkButton(frame, text='FECHAR', command=fechar_janela)
        btn_fechar.place(x=200, y=500)

        frame.mainloop()

    update(root, index_value, nome, idade, contato, rua, bairro, cidade)

def def_val_valor(root, pessoas):
    if index_value is None:
        print("Erro: index_value indefinido!")
        def_pop_up_vazio(root)
    else:
        def_update(root, pessoas)
    return
