from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required
from models.jogador_models import Jogador
from models.db import db

atualiza_vitoria_bp = Blueprint('atualiza_vitoria_route', __name__)

@atualiza_vitoria_bp.route('/<int:id>/atualiza-vitoria', methods=['GET', 'POST'])
@login_required
def atualiza_vitoria(id):
    if request.method == 'POST':
        total_vitorias = request.form['total_vitorias']
        Jogador.query.filter_by(id=id).first().update({'total_vitorias': total_vitorias})
        db.session.commit()
    return render_template('home.html')