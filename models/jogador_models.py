from models.db import db

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    total_vitorias = db.Column(db.Integer)

    def __init__(self, nome, total_vitorias):
        self.nome = nome
        self.total_vitorias = total_vitorias