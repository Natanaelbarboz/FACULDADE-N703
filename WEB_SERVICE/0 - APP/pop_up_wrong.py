from tkinter import *
from tkinter import filedialog
import customtkinter as ctk

def def_pop_up_wrong(frame):
    frame.withdraw()
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    frame_wrong = ctk.CTkToplevel()
    frame_wrong.title("VIDA PET")
    frame_wrong.geometry("450x300")
    frame_wrong.resizable(False, False)


    cabecalho = ctk.CTkLabel(frame_wrong, pady=15, text="ATENÇÃO", width=200, height=25, font=('arial bold', 26))
    cabecalho.pack()

    texto = ctk.CTkLabel(frame_wrong, pady=40, text="Usuário ou senha incorreto, tente novamente", width=200, height=25, font=('arial bold', 18))
    texto.pack()

    btn_ok = ctk.CTkButton(frame_wrong, text='OK',command=lambda: [fechar_janela(frame_wrong, frame)])
    btn_ok.place(x=150, y=225)

    frame_wrong.protocol("WM_wrong_WINDOW", lambda: [fechar_janela(frame_wrong, frame)])

    def fechar_janela(frame_wrong, frame):
        frame_wrong.destroy()
        frame.deiconify()  # Reexibe a janela principal

    frame_wrong.mainloop()