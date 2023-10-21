from . import db 
from sqlalchemy import func
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    
class Condicao:
    def __init__(self, id, nome, ventomin_vala, ventomax_vala, ventomin_altas, ventomax_altas, ventomin_classico, ventomax_classico, swellmin_vala, swellmax_vala, swellmin_altas, swellmax_altas, swellmin_classico, swellmax_classico,direcaomin_vala, direcaomax_vala, direcaomin_altas, direcaomax_altas, direcaomin_classico, direcaomax_classico, tainha):
        self.id = id
        self.nome = nome
        self.ventomin_vala = ventomin_vala
        self.ventomax_vala = ventomax_vala
        self.ventomin_altas = ventomin_altas
        self.ventomax_altas = ventomax_altas
        self.ventomin_classico = ventomin_classico
        self.ventomax_classico = ventomax_classico
        self.swellmin_vala = swellmin_vala
        self.swellmax_vala = swellmax_vala
        self.swellmin_altas = swellmin_altas
        self.swellmax_altas = swellmax_altas
        self.swellmin_classico = swellmin_classico
        self.swellmax_classico = swellmax_classico
        self.direcaomin_vala = direcaomin_vala
        self.direcaomax_vala = direcaomax_vala
        self.direcaomin_altas = direcaomin_altas
        self.direcaomax_altas = direcaomax_altas
        self.direcaomin_classico = direcaomin_classico
        self.direcaomax_classico = direcaomax_classico
        self.tainha = tainha