from flask import Blueprint, render_template, session, request, redirect, url_for
from flask_login import login_required
from models.jogador_models import Jogador
from models.db import db

home_route_bp = Blueprint('home_route', __name__)

@home_route_bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    id_usuario = session.get('id')
    jogadores = Jogador.query.filter_by(id_usuario=id_usuario).all()

    if request.method == 'POST':
        total_vitorias = request.form.getlist('total_vitorias')
        for i, jogador in enumerate(jogadores):
            jogador.total_vitorias = int(total_vitorias[i])
            db.session.add(jogador)
        db.session.commit()
        return redirect(url_for('home_route.home'))

    jogadores_ordenados = sorted(jogadores, key=lambda j: j.total_vitorias, reverse=True)
    return render_template('home.html', jogadores=jogadores_ordenados)
