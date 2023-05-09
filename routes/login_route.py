from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import usuario_models
from werkzeug.security import check_password_hash
from flask_login import login_user

login_route_bp = Blueprint('login_route', __name__)

def valida_campos(email, senha):
    if not email or not senha:
        flash('Preencha todos os campos do formulário', 'danger')
        return False
    return True

@login_route_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if not valida_campos(email, senha):
            return redirect(url_for('login_route.login'))
        usuario = usuario_models.Usuario.query.filter_by(email=email).first()
        if not usuario or not check_password_hash(usuario.senha, senha):
            flash('Email ou senha inválidos', 'danger')
            return redirect(url_for('login_route.login'))

        login_user(usuario)
        return redirect(url_for('home_route.home'))

    return render_template('login.html')
