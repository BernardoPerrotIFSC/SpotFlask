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

class Condicao2:
    def __init__(self, nome, ventomin, ventomax, tam_swellmin, tam_swellmax, dir_swellmin, dir_swellmax, tainha):
        self._nome = nome
        self._ventomin = ventomin
        self._ventomax = ventomax
        self._tam_swellmin = tam_swellmin
        self._tam_swellmax = tam_swellmax
        self._dir_swellmin = dir_swellmin
        self._dir_swellmax = dir_swellmax
        self._tainha = tainha

    def __str__(self):
        return f'Nome do pico: {self._nome}, Direção de Vento mínima: {self._ventomin}, Direção de vento Máxima: {self._ventomax}, tamanho de swell mínimo: {self._tam_swellmin},tamanho de swell máximo: {self._tam_swellmax},  Direção de swell mínimo: {self._dir_swellmin}, Direção de swell: {self._dir_swellmax}, Tainha: {self._tainha}'
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def ventomin(self):
        return self._ventomin

    @ventomin.setter
    def ventomin(self,ventomin):
        self._ventomin = ventomin

    @property
    def ventomax(self):
        return self._ventomax

    @ventomax.setter
    def ventomax(self, ventomax):
        self._ventomax = ventomax

    @property
    def tam_swellmin(self):
        return self._tam_swellmin

    @tam_swellmin.setter
    def tam_swellmin(self, tam_swellmin):
        self._tam_swellmin = tam_swellmin

    @property
    def tam_swellmax(self):
        return self._tam_swellmax

    @tam_swellmax.setter
    def tam_swellmax(self, tam_swellmax):
        self.tam_swellmax = tam_swellmax

    @property
    def dir_swellmin(self):
        return self._dir_swellmin

    @dir_swellmin.setter
    def dir_swellmin(self, dir_swellmin):
        self._dir_swellmin = dir_swellmin

    @property
    def dir_swellmax(self):
        return self._dir_swellmax

    @dir_swellmax.setter
    def dir_swellmax(self, dir_swellmax):
        self._dir_swellmax = dir_swellmax

    @property
    def tainha(self):
        return self._tainha
    
    @tainha.setter
    def tainha(self, tainha):
        self._tainha = tainha

    def picoNorte(self, vento, swell, direcao):
        if vento <= self._ventomin or vento >= self._ventomax:
            if swell >= self._tam_swellmin and swell <= self._tam_swellmax:
                if direcao >= self._dir_swellmin and direcao <= self._dir_swellmax:
                    return True
                
    def picoSul(self, vento, swell, direcao):
        if vento >= self._ventomin and vento <= self._ventomax:
            if swell >= self._tam_swellmin and swell <= self._tam_swellmax:
                if direcao >= self._dir_swellmin and direcao <= self._dir_swellmax:
                    return True

admin.add_view(ModelView(Usuario, db.session))
admin.add_view(ModelView(Historico, db.session))