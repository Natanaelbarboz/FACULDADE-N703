from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import customtkinter as ctk

import requests
import json

def def_pop_up_post(root):
    root.withdraw()
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    frame_post = ctk.CTkToplevel()
    frame_post.title("Pop_up_post")
    frame_post.geometry("300x250")
    frame_post.resizable(False, False)


    cabecalho = ctk.CTkLabel(frame_post, pady=15, text="SUCESSO!!", width=200, height=25, font=('arial bold', 26))
    cabecalho.pack()

    texto = ctk.CTkLabel(frame_post, pady=40, text="Pessoa Adicionada Com Sucesso!", width=200, height=25, font=('arial bold', 18))
    texto.pack()

    btn_ok = ctk.CTkButton(frame_post, text='OK',command=lambda: [fechar_janela(frame_post, root)])
    btn_ok.place(x=80, y=175)

    frame_post.protocol("WM_post_WINDOW", lambda: [fechar_janela(frame_post, root)])

    def fechar_janela(frame_post, root):
        frame_post.destroy()
        root.deiconify()  # Reexibe a janela principal

    frame_post.mainloop()