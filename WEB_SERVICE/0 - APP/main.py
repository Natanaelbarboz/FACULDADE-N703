from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import customtkinter as ctk

import pandas as pd
import numpy as np
import openpyxl
from datetime import datetime

import requests
import json

from post import def_post
from get import def_get
from update import def_val_valor
import update
from delete import def_delete
from login import sessao
from login import pessoas


pessoas = sessao()
if pessoas is None:
    print("Erro: Login não realizado! Encerrando programa.")
    exit()

# Se login deu certo, inicia a aplicação
def iniciar_aplicacao():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("ONG - VIDAS PET")
    root.geometry("900x600")

    cabecalho = ctk.CTkLabel(root, pady=15, text="VIDAS PET - ONG DE RESGATE", width=200, height=25, font=('arial bold', 26))
    cabecalho.pack()

    frame = ctk.CTkFrame(root, width=500, height=400)
    frame.pack(expand=False, fill="both", padx=15, pady=10)
    frame.pack_propagate(False)

    def_get(frame, pessoas)  # Chama a função apenas agora, com `pessoas` já definido

    btn_post = ctk.CTkButton(root, text='CADASTRAR', command=lambda: def_post(root, pessoas))
    btn_post.place(x=50, y=500)

    btn_update = ctk.CTkButton(root, text='EDITAR', command=lambda: def_val_valor(root, pessoas))
    btn_update.place(x=200, y=500)

    btn_delete = ctk.CTkButton(root, text='EXCLUIR', command=lambda: def_delete(root, pessoas))
    btn_delete.place(x=350, y=500)

    root.mainloop()

# Agora só inicia a aplicação se `pessoas` existir
iniciar_aplicacao()