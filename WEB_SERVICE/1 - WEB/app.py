from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId

app = Flask(__name__)

with open('../.gitignore', 'r') as arquivo:
    linhas = arquivo.readlines()

usuario = linhas[0].strip()
senha = linhas[1].strip()
linhas = None

uri = f'mongodb+srv://{usuario}:{senha}@n703.dfo9g.mongodb.net/?retryWrites=true&w=majority&appName=N703'
usuario = None
senha = None
client = MongoClient(uri)
db = client['N703-WEB-SERVICE']
pessoas = db['Pessoas']

# Rota para exibir todos os registros
@app.route('/')
def index():
    todos = pessoas.find()  # Busca todos os documentos da coleção
    return render_template('index.html', pessoas=todos)

# Rota para adicionar um novo registro
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['Nome']
        idade = request.form['Idade']
        contato = request.form['Contato']
        pessoa = {
            'Nome': nome,
            'Idade': idade,
            'Contato': contato
        }
        pessoas.insert_one(pessoa)  # Inserir no MongoDB
        return redirect(url_for('index'))
    return render_template('adicionar.html')

# Rota para editar um registro
@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    try:
        pessoa = pessoas.find_one({'_id': ObjectId(id)})
    except InvalidId:
        return redirect(url_for('index'))

    if request.method == 'POST':
        nome = request.form['Nome']
        idade = request.form['Idade']
        contato = request.form['Contato']
        pessoas.update_one({'_id': ObjectId(id)}, {'$set': {
            'Nome': nome,
            'Idade': idade,
            'Contato': contato
        }})
        return redirect(url_for('index'))
    
    return render_template('editar.html', pessoa=pessoa)

# Rota para deletar um registro
@app.route('/deletar/<id>', methods=['GET'])
def deletar(id):
    try:
        pessoas.delete_one({'_id': ObjectId(id)})
    except InvalidId:
        return redirect(url_for('index'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)