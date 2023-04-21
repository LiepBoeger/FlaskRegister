from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

# configuração da aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuario.sqlite3'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)


# criacao da tabela de usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)

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
        if senha != confirma_senha:
            db.session.rollback()
            flash("As senhas não coincidem", "error")
        if not nome or not email or not senha:
            flash("Preencha todos os campos do formulário", "error")
        else:
            usuario = Usuario(nome, email, senha)
            db.session.add(usuario)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                flash('Erro no cadastro', 'error')
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('cadastro'))
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
