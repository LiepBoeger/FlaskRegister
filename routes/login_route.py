from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.db import db
from models.usuario_models import Usuario
from werkzeug.security import generate_password_hash

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
    return render_template('login.html')
