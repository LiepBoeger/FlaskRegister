from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.db import db
from models.jogador_models import Jogador

cadastro_jogador_route_bp = Blueprint('cadastro_jogador_route', __name__)

@cadastro_jogador_route_bp.route('/cadastro-jogador', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        if not nome:
            flash('Preencha o nome do jogador', 'danger')
        else:
            jogador = Jogador(nome, 0)
            db.session.add(jogador)
            db.session.commit()
            return redirect(url_for('cadastro_jogador_route.cadastro'))
    jogador = Jogador.query.all()
    return render_template('cadastro_jogador.html', jogadores=jogador)
