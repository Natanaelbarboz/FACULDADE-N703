

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import customtkinter as ctk

from pymongo import MongoClient

from get import def_get
from pop_up_post import def_pop_up_post
from login import pessoas

def def_post(root, pessoas):

    root.withdraw()
    

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # frame = ctk.CTk()
    frame = ctk.CTkToplevel()
    frame.title("ONG - VIDAS PET")
    frame.geometry("650x600")
    frame.resizable(False, False)

    sub_titulo = ctk.CTkLabel(frame, text="CADASTRO AMIGO DOS PETS", font=("roboto", 18))
    sub_titulo.place(x=250, y=10)

    text_nome = ctk.CTkLabel(frame, text="NOME", width=150, font=("roboto", 14))
    text_nome.place(x=25, y=115)

    text_idade = ctk.CTkLabel(frame, text="IDADE", width=150, font=("roboto", 14))
    text_idade.place(x=25, y=150)

    text_contato = ctk.CTkLabel(frame, text="CONTATO", width=150, font=("roboto", 14))
    text_contato.place(x=25, y=185)

    text_rua = ctk.CTkLabel(frame, text="RUA", width=150, font=("roboto", 14))
    text_rua.place(x=25, y=220)

    text_bairro = ctk.CTkLabel(frame, text="BAIRRO", width=150, font=("roboto", 14))
    text_bairro.place(x=25, y=255)

    text_cidade = ctk.CTkLabel(frame, text="CIDADE", width=150, font=("roboto", 14))
    text_cidade.place(x=25, y=290)

    label_nome = ctk.CTkEntry(frame, placeholder_text="Informe o nome", width=350, font=("roboto", 14))
    label_nome.place(x=200, y=115)

    label_idade = ctk.CTkEntry(frame, placeholder_text="Informe a idade", width=350, font=("roboto", 14))
    label_idade.place(x=200, y=150)

    label_contato = ctk.CTkEntry(frame, placeholder_text="Informe o contato com DDD", width=350, font=("roboto", 14))
    label_contato.place(x=200, y=185)

    label_rua = ctk.CTkEntry(frame, placeholder_text="Informe a rua com número", width=350, font=("roboto", 14))
    label_rua.place(x=200, y=220)

    label_bairro = ctk.CTkEntry(frame, placeholder_text="Informe o bairro", width=350, font=("roboto", 14))
    label_bairro.place(x=200, y=255)

    label_cidade = ctk.CTkEntry(frame, placeholder_text="Informe a cidade", width=350, font=("roboto", 14))
    label_cidade.place(x=200, y=290)

    def limpar(label_nome, label_idade, label_contato, label_rua, label_bairro, label_cidade):
        label_nome.delete(0, "end")
        label_idade.delete(0, "end")
        label_contato.delete(0, "end")
        label_rua.delete(0, "end")
        label_bairro.delete(0, "end")
        label_cidade.delete(0, "end")
        #print('Limpo')



    def get(label_nome, label_idade, label_contato, label_rua, label_bairro, label_cidade):
        nome = label_nome.get()
        idade = label_idade.get()
        contato = label_contato.get()
        rua = label_rua.get()
        bairro = label_bairro.get()
        cidade = label_cidade.get()
        if nome == '' or idade == '' or contato == '':
            print('Informe os valores')
        else:
            get_base = {"Nome": nome, "Idade": idade, "Contato": contato, "Rua":rua, "Bairro":bairro, "Cidade":cidade}

            # with open('../.gitignore', 'r') as arquivo:
            #     linhas = arquivo.readlines()

            # usuario = linhas[0].strip()
            # senha = linhas[1].strip()
            # linhas = None
            # uri = f'mongodb+srv://{usuario}:{senha}@n703.dfo9g.mongodb.net/?retryWrites=true&w=majority&appName=N703'
            # usuario = None
            # senha = None            
            # client = MongoClient(uri)
            # db = client['N703-WEB-SERVICE']
            # pessoas = db['Pessoas']
            pessoas.insert_one(get_base)

            print(f'Nome: {nome}, Idade: {idade}, Contato: {contato}')
            limpar(label_nome, label_idade, label_contato, label_rua, label_bairro, label_cidade)
            def_pop_up_post(frame)

    btn = ctk.CTkButton(frame, text='SALVAR',command=lambda: [get(label_nome, label_idade, label_contato,
                                                                  label_rua, label_bairro, label_cidade)])
    btn.place(x=200, y=350)

    btn_fechar = ctk.CTkButton(frame, text="FECHAR", fg_color="red", hover_color="darkred",  command=lambda: fechar_janela(frame, root))
    btn_fechar.place(x=350, y=350)

    frame.protocol("WM_DELETE_WINDOW", lambda: [fechar_janela(frame, root)])

    def fechar_janela(frame, root):
        frame.destroy()
        root.deiconify()  # Reexibe a janela principal

    frame.mainloop()