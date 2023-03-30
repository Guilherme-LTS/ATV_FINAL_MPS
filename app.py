from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página de login
@app.route('/login')
def login():
    return render_template('index.html')

# Rota para validar o login
@app.route('/login', methods=['POST'])
def validar_login():
    # Recupera os dados do formulário
    username = request.form['username']
    password = request.form['password']

    # Valida o usuário e senha (exemplo simples)
    if username == 'admin' and password == '123':
        return 'Login realizado com sucesso!'
    else:
        return 'Usuário ou senha inválidos.'
