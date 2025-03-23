from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import customtkinter as ctk

import requests
import json

def def_pop_up_delete(root):
    root.withdraw()
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    frame_delete = ctk.CTkToplevel()
    frame_delete.title("ONG - VIDAS PET")
    frame_delete.geometry("450x300")
    frame_delete.resizable(False, False)


    cabecalho = ctk.CTkLabel(frame_delete, pady=15, text="ATENÇÃO", width=200, height=25, font=('arial bold', 26))
    cabecalho.pack()

    texto = ctk.CTkLabel(frame_delete, pady=40, text="AMIGO REMOVIDO", width=200, height=25, font=('arial bold', 18))
    texto.pack()

    btn_ok = ctk.CTkButton(frame_delete, text='OK',command=lambda: [fechar_janela(frame_delete, root)])
    btn_ok.place(x=150, y=225)

    frame_delete.protocol("WM_DELETE_WINDOW", lambda: [fechar_janela(frame_delete, root)])

    def fechar_janela(frame_delete, root):
        frame_delete.destroy()
        root.deiconify()  # Reexibe a janela principal

    frame_delete.mainloop()