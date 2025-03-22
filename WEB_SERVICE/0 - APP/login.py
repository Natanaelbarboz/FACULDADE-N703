from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import customtkinter as ctk

from pymongo import MongoClient
from bson import ObjectId

from pop_up_wrong import def_pop_up_wrong

pessoas = None  

def sessao():
    global pessoas
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    frame = ctk.CTk()
    # frame = ctk.CTkToplevel()
    frame.title("VIDA PET")
    frame.geometry("450x300")
    frame.resizable(False, False)


    titulo = ctk.CTkLabel(frame, text="BEM VINDO(A) A CAUSA PET", font=("roboto", 20))
    titulo.place(x=90, y=40)

    sub_titulo = ctk.CTkLabel(frame, text="LOGIN", font=("roboto", 14))
    sub_titulo.place(x=30, y=110)

    text_login = ctk.CTkLabel(frame, text="SENHA", font=("roboto", 14))
    text_login.place(x=30, y=150)

    label_login = ctk.CTkEntry(frame, placeholder_text="Informe seu login", width=250, font=("roboto", 14))
    label_login.place(x=100, y=115)

    label_senha = ctk.CTkEntry(frame, placeholder_text="Informe sua senha", width=250, font=("roboto", 14), show="*")
    label_senha.place(x=100, y=150)

    def limpar(label_login, label_senha):
        label_login.delete(0, "end")
        label_senha.delete(0, "end")



    def conexao(label_login, label_senha ):
        global pessoas
        login = label_login.get()
        senha = label_senha.get()
        if not login or not senha:  # Verifica se os campos estão vazios
            print('Informe os valores')
            return  # Sai da função
        
        try:
            uri = f'mongodb+srv://{login}:{senha}@n703.dfo9g.mongodb.net/?retryWrites=true&w=majority&appName=N703'
            print("Usuário ok")
            print(f'login: {login}, senha: {senha}')
            login = None
            senha = None            
            client = MongoClient(uri)
            db = client['N703-WEB-SERVICE']
            limpar(label_login, label_senha)
            db.list_collection_names()
            pessoas = db['Pessoas']
            # resultado = pessoas.find_one({"_id": ObjectId("67c61e8d1d49a561339fc8b9")})
            # print(resultado)
            fechar_janela(frame)
        except Exception as e:
            print(f'Erro: {e}')
            def_pop_up_wrong(frame)
            limpar(label_login, label_senha)
                

    btn = ctk.CTkButton(frame, text='ENTRAR',command=lambda: [conexao(label_login, label_senha)])
    btn.place(x=100, y=250)

    btn_fechar = ctk.CTkButton(frame, text="FECHAR", fg_color="red", hover_color="darkred",  command=lambda: fechar_janela(frame))
    btn_fechar.place(x=250, y=250)

    frame.protocol("WM_DELETE_WINDOW", lambda: [fechar_janela(frame)])

    def fechar_janela(frame):
        frame.destroy()

    frame.mainloop()
    return pessoas