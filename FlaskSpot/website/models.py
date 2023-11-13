from . import db 
from sqlalchemy import func
from flask_login import UserMixin
import datetime
from . import admin
from flask_admin.contrib.sqla import ModelView

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    historico = db.relationship('Historico')
    
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

    def verifica_tainha(self):
        current_month = datetime.datetime.now().month
        if current_month == 5 or current_month == 6:
            if self.tainha == "fechado":
                return False
            elif self.tainha == "aberto":
                return True
            elif self.tainha == "bandeira":
                return
        else:
            return True

    def executarNorte(self, vento, swell, direcao):
        if self.verifica_tainha() ==  True:
            if (vento <= self.ventomin_classico) or (vento >= self.ventomax_classico):
                if swell >= self.swellmin_classico and swell <= self.swellmax_classico:
                    if direcao >= self.direcaomin_classico and direcao <= self.direcaomax_classico:
                        return "classico"
            if (vento <= self.ventomin_altas) or (vento >= self.ventomax_altas):
                if swell >= self.swellmin_altas and swell <= self.swellmax_altas:
                    if direcao >= self.direcaomin_altas and direcao <= self.direcaomax_altas:
                        return "altas"
            elif (vento <= self.ventomin_vala) or (vento >= self.ventomax_vala):
                if swell >= self.swellmin_vala and swell <= self.swellmax_vala:
                    if direcao >= self.direcaomin_vala and direcao <= self.direcaomax_vala:
                        return "vala"
                    
    def executarSul(self, vento, swell, direcao):
        if self.verifica_tainha() == True:
            if (vento >= self.ventomin_classico) and (vento <= self.ventomax_classico):
                if swell >= self.swellmin_classico and swell <= self.swellmax_classico:
                    if direcao >= self.direcaomin_classico and direcao <= self.direcaomax_classico:
                        return "classico"
            if (vento >= self.ventomin_altas) and (vento <= self.ventomax_altas):
                if swell >= self.swellmin_altas and swell <= self.swellmax_altas:
                    if direcao >= self.direcaomin_altas and direcao <= self.direcaomax_altas:
                        return "altas"
            elif (vento >= self.ventomin_vala) and (vento <= self.ventomax_vala):
                if swell >= self.swellmin_vala and swell <= self.swellmax_vala:
                    if direcao >= self.direcaomin_vala and direcao <= self.direcaomax_vala:
                        return "vala"
                    

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    vento = db.Column(db.Float)
    swell = db.Column(db.Float)
    direcao = db.Column(db.Float)
    data = db.Column(db.Date)
    classicos = db.Column(db.String)
    altas = db.Column(db.String)
    vala = db.Column(db.String)

admin.add_view(ModelView(Usuario, db.session))
admin.add_view(ModelView(Historico, db.session))