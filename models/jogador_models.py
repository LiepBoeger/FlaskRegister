from models.db import db

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', backref='jogadores')
    nome = db.Column(db.String(50))
    total_vitorias = db.Column(db.Integer)

    def __init__(self, id_usuario, nome, total_vitorias):
        self.id_usuario = id_usuario
        self.nome = nome
        self.total_vitorias = total_vitorias