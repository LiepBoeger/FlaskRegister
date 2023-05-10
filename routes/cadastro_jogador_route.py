from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.db import db
from models.usuario_models import Usuario
from flask_login import login_user

cadastro_jogador_route_bp = Blueprint('cadastro_jogador_route', __name__)

@cadastro_jogador_route_bp.route('/cadastro-jogador', methods=['GET', 'POST'])
def cadastro():
    return render_template('cadastro_jogador.html')
