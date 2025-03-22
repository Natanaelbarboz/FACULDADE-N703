from tkinter import Tk, Frame, ttk
import pandas as pd

from pymongo import MongoClient
from bson import ObjectId

import update  # Importa o módulo inteiro
from pop_up_delete import def_pop_up_delete
from pop_up_selec_vazia import def_pop_up_vazio
from login import pessoas

def def_delete(root, pessoas):
    try:
        if update.index_value is None:            
            print('Não há valor selecionado')
            def_pop_up_vazio(root)
            return
        
        try:
            object_id = ObjectId(update.index_value)  # Converte para ObjectId
        except Exception as e:
            print(f"Erro ao converter index_value para ObjectId: {e}")
            return

        # Lendo credenciais do arquivo
        # try:
        #     with open('../.gitignore', 'r') as arquivo:
        #         linhas = arquivo.readlines()
        #         usuario = linhas[0].strip()
        #         senha = linhas[1].strip()
        # except Exception as e:
        #     print(f"Erro ao ler credenciais: {e}")
        #     return

        # # Conectando ao banco
        # uri = f'mongodb+srv://{usuario}:{senha}@n703.dfo9g.mongodb.net/?retryWrites=true&w=majority&appName=N703'
        # client = MongoClient(uri)
        # db = client['N703-WEB-SERVICE']
        # pessoas = db['Pessoas']

        # Tentando excluir o documento
        resultado = pessoas.delete_one({"_id": object_id})

        if resultado.deleted_count > 0:
            print(f'Id excluído: {update.index_value}')
            def_pop_up_delete(root)
            print(f"Registro {update.index_value} excluído com sucesso!")
            update.index_value = None
        else:
            print(f"Não houve exclusão para o index {update.index_value}.")

    except Exception as e:
        print(f'Erro ao excluir: {e}')
