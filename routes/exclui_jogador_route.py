from flask import Blueprint, redirect, url_for
from models.db import db
from models.jogador_models import Jogador

exclui_jogador_route_bp = Blueprint('exclui_jogador_route', __name__)

@exclui_jogador_route_bp.route('/<int:id>/exclui-jogador')
def exclui_jogador(id):
    jogador = Jogador.query.filter_by(id=id).first()
    db.session.delete(jogador)
    db.session.commit()
    return redirect(url_for('cadastro_jogador_route.cadastro'))
