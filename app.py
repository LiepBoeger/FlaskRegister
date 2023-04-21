from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# configuração da aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuario.sqlite3'
app.config['SECRET_KEY'] = 'secretkey'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String, unique=True)
    senha = db.Column(db.String(250))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# criação da rota main
@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirma_senha = request.form['confirm']
        verifica_email = Usuario.query.filter_by(email=email).first()

        if verifica_email:
            flash('Email já cadastrado!', 'danger')
            return redirect(url_for('cadastro'))

        if senha != confirma_senha:
            flash('As senhas não coincidem!', 'danger')
            return redirect(url_for('cadastro'))

        if not nome or not email or not senha:
            flash('Preencha todos os campos do formulário', 'danger')
            return redirect(url_for('cadastro'))
        else:
            senha = generate_password_hash(request.form['senha'])
            usuario = Usuario(nome, email, senha)
            db.session.add(usuario)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                flash('Erro no cadastro', 'danger')
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('cadastro'))
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
