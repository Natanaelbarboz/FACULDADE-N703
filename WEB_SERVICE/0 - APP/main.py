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
from update import def_update
from delete import def_delete


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("CADASTRO DE CLIENTES")
root.geometry("800x500")
# root.resizable(False, False)


cabecalho = ctk.CTkLabel(root, pady=15, text="SISTEMA DE CADASTRO DE CLIENTES", width=200, height=25, font=('arial bold', 26))
cabecalho.pack()

frame = ctk.CTkFrame(root, width=500, height=400)
frame.pack(expand=False, fill="both", padx=15, pady=10)
frame.pack_propagate(False)

def_get(frame)


btn_post = ctk.CTkButton(root, text='CRIAR NOVO CLIENTE',command=lambda:[def_post(root)])
btn_post.place(x=50, y=500)

btn_update = ctk.CTkButton(root, text='EDITAR CLIENTE',command=lambda:[def_update(root)])
btn_update.place(x=200, y=500)

btn_delete = ctk.CTkButton(root, text='EXCLUIR',command=lambda:[def_delete(root)])
btn_delete.place(x=350, y=500)


root.mainloop()