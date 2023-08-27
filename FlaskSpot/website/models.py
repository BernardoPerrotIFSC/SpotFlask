from . import db 
from sqlalchemy import func
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    
class Condicao:
    def __init__(self, nome, ventomin, ventomax, tam_swellmin, tam_swellmax, dir_swellmin, dir_swellmax, tainha):
        self._nome = nome
        self._ventomin = ventomin
        self._ventomax = ventomax
        self._tam_swellmin = tam_swellmin
        self._tam_swellmax = tam_swellmax
        self._dir_swellmin = dir_swellmin
        self._dir_swellmax = dir_swellmax
        self._tainha = tainha