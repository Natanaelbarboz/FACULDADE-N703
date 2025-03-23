from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import customtkinter as ctk


import requests
import json

def def_pop_up_update(root):
    root.withdraw()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    frame_update = ctk.CTkToplevel()
    frame_update.title("ATENÇÃO!!!")
    frame_update.geometry("450x300")
    frame_update.resizable(False, False)


    cabecalho = ctk.CTkLabel(frame_update, pady=15, text="ATENÇÃO", width=200, height=25, font=('arial bold', 26))
    cabecalho.pack()

    texto = ctk.CTkLabel(frame_update, pady=40, text="AMIGO EDITADO COM SUCESSO", width=200, height=25, font=('arial bold', 18))
    texto.pack()

    btn_ok = ctk.CTkButton(frame_update, text='OK',command=lambda: [fechar_janela(frame_update, root)])
    btn_ok.place(x=150, y=225)

    frame_update.protocol("WM_DELETE_WINDOW", lambda: [fechar_janela(frame_update, root)])

    def fechar_janela(frame_update, root):
        frame_update.destroy()
        root.deiconify()  # Reexibe a janela principal

    frame_update.mainloop()