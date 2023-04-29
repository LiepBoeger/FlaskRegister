from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.db import db
from models.usuario_models import Usuario
from werkzeug.security import generate_password_hash

user_routes_bp = Blueprint('user_routes', __name__)

def valida_campos(nome, email, senha, confirma_senha):

    verifica_email = Usuario.query.filter_by(email=email).first()
    if verifica_email:
        flash('Email já cadastrado!', 'danger')
        return False

    if senha != confirma_senha:
        flash('As senhas não coincidem!', 'danger')
        return False

    if not nome or not email or not senha:
        flash('Preencha todos os campos do formulário', 'danger')
        return False

    return True

@user_routes_bp.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirma_senha = request.form['confirm']

        if valida_campos(nome, email, senha, confirma_senha):
            senha = generate_password_hash(request.form['senha'])
            usuario = Usuario(nome, email, senha)
            db.session.add(usuario)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                flash('Erro no cadastro', 'danger')

            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('user_routes.cadastro'))
    return render_template('index.html')
