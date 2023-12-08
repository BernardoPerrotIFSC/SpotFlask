from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Condicao, Historico, Condicao2, Historico2
from website import db
from datetime import datetime
import json


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', usuario=current_user)

@views.route('/algoritmo', methods=['GET', 'POST'])
@login_required
def algoritmo():
    vento = None
    swell = None
    direcao = None
    classico = []
    altas = []
    vala = []
    if request.method == 'POST':
        vento = int(request.form.get('vento'))
        swell = float(request.form.get('tamanho'))
        direcao = int(request.form.get('swell'))
        data_str = request.form.get('data')
        data = datetime.strptime(data_str, '%Y-%m-%d')
        
        #Paulo Lopes
        guarda = Condicao(1,"Guarda do Embaú", 65, 270, 45, 270, 22, 270, 1.1, 2.5, 1.4, 2.5, 1.6, 2.5, 45, 180, 45, 180, 45, 180, "fechado")
        gamboa = Condicao(2, "Gamboa", 140, 270, 180, 270, 180, 270, 1.4, 2.2, 1.6, 2.5, 2, 2.5, 67, 135, 67, 110, 67, 110, "fechado")
        #Garopaba
        garopabinha = Condicao(3, "Garopabinha", 157, 270, 180, 270, 200, 270, 1.1, 2, 1.4, 2, 1.6, 2, 67, 135, 67, 120, 67, 110, "fechado")
        silveiranorte = Condicao(4, "Silveira Norte", 45, 200, 22, 225, 15, 240, 1.1, 2.3, 1.4, 2.3, 1.6, 2.3, 45, 180, 45, 150, 45, 135, "fechado")
        tayson = Condicao(5, "Tayson", 150, 300, 170, 300, 190, 300, 1.3, 2, 1.5, 2.2, 1.7, 2.2, 67, 180, 67, 150, 67, 135, "bandeira")
        silveirasul = Condicao(6, "Silveira Sul", 135, 360, 157, 360, 180, 360, 1.6, 4, 2, 4, 2.3, 4, 90, 180, 90, 180, 100, 160, "bandeira")
        ferrugem = Condicao(7, "Ferrugem", 67, 247, 45, 270, 35, 270, 1.1, 1.9, 1.5, 1.9, 1.5, 1.8, 80, 190, 80, 190, 80, 190, "aberto")
        barrinha = Condicao(8, "Barrinha", 160, 10, 180, 270, 200, 270, 1.1, 1.7, 1.4, 1.8, 1.6, 1.8, 70, 190, 70, 180, 70, 160, "fechado")
        barranorte = Condicao(9, "Barra Norte", 30, 180, 22, 200, 10, 220, 1.1, 1.7, 1.4, 1.8, 1.6, 1.8, 70, 190, 70, 180, 70, 160, "fechado")
        barra = Condicao(10, "Barra Sul", 160, 10, 180, 270, 200, 270, 1.1, 1.7, 1.4, 1.8, 1.6, 1.8, 70, 190, 70, 180, 70, 160, "fechado")
        ouvidor = Condicao(11, "Ouvidor", 160, 270, 180, 270, 200, 270, 1.4, 1.8, 1.5, 1.8, 1.5, 1.9, 70, 135, 70, 130, 70, 110, "fechado")
        vermelha = Condicao(12, "Vermelha", 160, 270, 180, 270, 200, 270, 1.4, 1.9, 1.5, 1.9, 1.6, 1.9, 67, 135, 67, 120, 67, 110, "fechado")

        #imbituba
        rosanorte = Condicao(13, "Rosa Norte", 75, 180, 45, 180, 22, 200, 1.1, 2, 1.4, 2, 1.5, 2, 67, 190, 90, 180, 90, 180, "aberto")
        rosasul = Condicao(14, "Rosa Sul", 129, 270, 180, 270, 200, 270, 1.4, 4, 1.6, 4, 1.8, 4, 70, 180, 70, 160, 70, 120, "bandeira")
        luz = Condicao(15, "Luz", 160, 270, 180, 270, 200, 270, 1.1, 1.8, 1.4, 1.8, 1.6, 1.8, 70, 180, 70, 180, 70, 180, "fechado")
        ibiraquera = Condicao(16, "Ibiraquera", 45, 270, 32, 270, 20, 270, 1.1, 2.7, 1.1, 2.7, 1.1, 2.7, 70, 180, 90, 180, 100, 180, "bandeira")
        ribanceira = Condicao(17, "Ribanceira", 160, 270, 180, 270, 200, 270, 1.6, 3, 1.8, 3, 2, 3, 90, 180, 100, 170, 110, 160, "bandeira")
        praiadagua = Condicao(18, "Praia d'água", 157, 270, 180, 270, 200, 270, 1.4, 2, 1.6, 2, 1.8, 2, 135, 180, 135, 180, 135, 180, "aberto")
        portinho = Condicao(19, "Portinho", 57, 270, 180, 270, 200, 270, 1.3, 2.5, 1.6, 2.2, 1.6, 2, 70, 135, 70, 120, 70, 110, "aberto")
        praiadavila = Condicao(20, "Vila", 45, 270, 40, 270, 35, 270, 1.4, 3, 1.8, 3, 2, 3, 90, 180, 100, 180, 110, 180, "bandeira")
        # castelinho = Condicao()
        itapirasul = Condicao(21, "Itapiruba Sul", 160, 270, 180, 270, 200, 270, 1.2, 2.3, 1.5, 2.3, 1.7, 2.3, 90, 180, 90, 180, 90, 180, "fechado")
        itapiranorte = Condicao(22, "Itapiruba Norte", 45, 270, 25, 270, 10, 270, 1.1, 2, 1.4, 2, 1.6, 2, 90, 180, 90, 180, 90, 180, "bandeira")

        #laguna
        gisul = Condicao(23, "Gi Sul",160, 270, 180, 270, 200, 270, 1.3, 2.3, 1.5, 2.3, 1.7, 2.3, 80, 180, 80, 135, 90, 110, "aberto")
        ginorte = Condicao(24, "Gi Norte", 20, 225, 10, 225, 10, 250, 1.1, 1.6, 1.3, 1.6, 1.4, 1.6, 90, 180, 90, 180, 90, 180, "aberto")
        ravena = Condicao(25, "Ravena", 160, 270, 180, 270, 200, 270, 1.6, 2.5, 1.8, 2.5, 2, 2.5, 90, 180, 90, 180, 90, 180, "aberto")
        ponta = Condicao(26, "Ponta", 160, 270, 180, 270, 200, 270, 1.2, 1.8, 1.4, 1.8, 1.6, 1.8, 90, 180, 110, 180, 120, 180, "aberto")

        #FarolDeSantaMarta
        tereza = Condicao(27, "Tereza", 160, 270, 180, 270, 200, 270, 1.6, 2.1, 1.7, 2.1, 1.7, 2.1, 90, 180, 90, 180, 90, 180, "aberto")
        ipua = Condicao(28, "Ipuã", 45, 270, 32, 270, 30, 270, 1.3, 2.2, 1.5, 2.2, 1.7, 2.2, 110, 180, 110, 180, 110, 180, "aberto")
        galheta = Condicao(29, "Galheta", 45, 270, 32, 270, 30, 270, 1.3, 2.4, 1.7, 2.4, 1.7, 2.4, 110, 190, 110, 180, 110, 190, "aberto")
        cardoso = Condicao(30, "Cardoso", 45, 270, 32, 270, 30, 270, 1.3, 4, 1.8, 4, 2, 4, 110, 190, 110, 190, 110, 190, "aberto")
        cigana = Condicao(31, "Cigana", 45, 270, 32, 270, 30, 270, 1.3, 2.2, 1.5, 2.2, 1.7, 2.2, 110, 190, 110, 190, 110, 190, "aberto")

        picos_nordeste = [guarda, silveiranorte, ferrugem, barranorte, rosanorte, ibiraquera, praiadavila, itapiranorte,  ginorte, ipua, galheta, cardoso, cigana]
        picos_sul = [gamboa, garopabinha, tayson, silveirasul, barrinha, barra, ouvidor, vermelha, rosasul, luz, ribanceira, praiadagua, portinho, itapirasul, gisul, ravena, ponta, tereza]

        for pico in picos_nordeste:
            if pico.executarNorte(vento, swell, direcao) == "classico":
                classico.append(pico.nome)
            elif pico.executarNorte(vento, swell, direcao) == "altas":
                altas.append(pico.nome)
            elif pico.executarNorte(vento, swell, direcao) == "vala":
                vala.append(pico.nome)

        for pico in picos_sul:
            if pico.executarSul(vento, swell, direcao) == "classico":
                classico.append(pico.nome)
            elif pico.executarSul(vento, swell, direcao) == "altas":
                altas.append(pico.nome)
            elif pico.executarSul(vento, swell, direcao) == "vala":
                vala.append(pico.nome)
        classicos = ', '.join(classico)
        valas = ', '.join(vala)
        alta = ', '.join(altas)

        novo = Historico(usuario_id = current_user.id, vento=vento, swell=swell, direcao=direcao,data=data, classicos=classicos, altas = alta, vala = valas)
        db.session.add(novo)
        db.session.commit()
    return render_template('algoritmo/algoritmo.html', usuario=current_user, vento = vento, tamanho_swell=swell, direcao_swell= direcao, classico=classico, altas=altas, vala=vala)

@views.route('/view', methods=['GET'])
@login_required
def view():
    return render_template("algoritmo/view.html", usuario=current_user)

@views.route('/remove-Historico', methods=['POST','GET'])
@login_required
def remover_historico():
    data = json.loads(request.data)
    historico_id = data["historicoId"]
    historico = Historico.query.get(historico_id)
    if historico.usuario_id == current_user.id:
        db.session.delete(historico)
        db.session.commit()
    flash("Condição removida!", category="success")
    return jsonify({})

@views.route('/algoritmo-simples', methods=['GET','POST'])
@login_required
def algoritmo2():
    vento = None
    swell = None
    direcao = None
    rolando = []
    if request.method == 'POST':
        vento = int(request.form.get('vento'))
        swell = float(request.form.get('tamanho'))
        direcao = int(request.form.get('swell'))
        data_str = request.form.get('data')
        data = datetime.strptime(data_str, '%Y-%m-%d')

        guarda = Condicao2("Guarda do Embaú", 50, 270, 1.1, 2.8, 80, 180, "fechado")
        gamboa = Condicao2("Gamboa",180, 290, 1.4, 2.5, 90, 135, "fechado")
        #garopaba
        garopabinha = Condicao2("Garopabinha", 180, 290, 1.1, 1.7, 70, 120, "fechado")
        # lajinha = Condicao()
        silveiranorte = Condicao2("Silveira Norte",50, 247, 1.1, 2.3, 70, 140, "fechado")
        tayson = Condicao2("Tayson", 65, 360, 1.1, 2.0, 70, 135, "bandeira")
        silveirasul = Condicao2("Silveira Sul", 65, 360, 1.6, 4, 80, 190, "bandeira")
        ferrugem = Condicao2("Ferrugem", 67, 247, 1.1, 1.9, 80, 190, "aberto")
        barrinha = Condicao2("Barrinha", 160, 290, 1.1, 1.7, 70, 190, "fechado")
        barranorte = Condicao2("Barra Norte", 180, 380, 1.1, 1.7, 80, 180, "fechado")
        barra = Condicao2("Barra SUl", 257, 280, 1.1, 1.8, 70, 190, "fechado")
        ouvidor = Condicao2("Ouvidor", 180, 290, 1.1, 1.6, 80, 157, "fechado")
        vermelha = Condicao2("Vermelha",180, 280, 1.3, 2.0, 80, 157, "fechado")
        #imbituba
        rosanorte = Condicao2("Rosa Norte", 75, 135, 1.0, 2.0, 75, 185, "aberto")
        rosasul = Condicao2("Rosa Sul",135, 270, 1.0, 4.5, 55, 200, "bandeira")
        luz = Condicao2("luz", 120, 270, 1.0, 1.8, 65, 180, "fechado")
        ibiraquera = Condicao2("Ibiraquera", 45, 240, 1.0, 2.5, 60, 180, "bandeira")
        ribanceira = Condicao2("Ribanceira", 160, 270, 1.0, 3.0, 70, 190, "bandeira")
        praiadagua = Condicao2("Praia d'água", 180, 270, 1.1, 1.7, 90, 185, "aberto")
        portinho = Condicao2("Portinho",135, 270, 1.1, 2.5, 67.5, 135, "aberto")
        praiadavila = Condicao2("Vila",67, 240, 1.1, 3.0, 112, 200, "bandeira")
        # castelinho = Condicao()
        itapirasul = Condicao2("Itapiruba Sul",157, 270, 1.2, 2.0, 90, 135, "fechado")
        itapiranorte = Condicao2("Itapiruba Norte",67, 315, 1.0, 1.8, 67, 200, "bandeira")          
        #laguna
        gisul = Condicao2("Gi Sul",190, 270, 1.5, 2.2, 70, 130, "aberto")
        ginorte = Condicao2("Gi Norte", 10, 290, 1.0, 1.5, 70, 180, "aberto")
        ravena = Condicao2("Ravena",150, 270, 1.6, 2.2, 90, 185, "aberto")
        ponta = Condicao2("Ponta",170, 270, 1.3, 1.6, 90, 185, "aberto")
        #FarolDeSantaMarta
        tereza = Condicao2("Tereza",157, 270, 1.3, 2.5, 90, 190, "aberto")
        ipua = Condicao2("Ipuã", 67, 270, 1.1, 2.8, 90, 190, "aberto")
        galheta = Condicao2("Galheta", 67, 270, 1.1, 2.8, 90, 190, "aberto")
        cardoso = Condicao2("Cardoso", 67, 245, 1.1, 5, 90, 190, "aberto")
        cigana = Condicao2("Cigana", 67, 270, 1.1, 2.3, 100, 200, "aberto")

        Picos_Nordeste = [guarda, silveiranorte, ferrugem, barranorte, rosanorte, ibiraquera, praiadavila, itapiranorte,  ginorte, ipua, galheta, cardoso, cigana]

        Picos_Sul = [gamboa, garopabinha, tayson, silveirasul, barrinha, barra, ouvidor, vermelha, rosasul, luz, ribanceira, praiadagua, portinho, itapirasul, gisul, ravena, ponta, tereza]

        for pico in Picos_Nordeste:
            if pico.picoNorte(vento, swell, direcao) == True:
                rolando.append(pico.nome)
        for pico in Picos_Sul:
            if pico.picoSul(vento, swell, direcao) == True:
                rolando.append(pico.nome)
        picos = ', '.join(rolando)
        novo = Historico2(usuario_id = current_user.id, vento=vento, swell=swell, direcao=direcao,data=data, picos = picos)
        db.session.add(novo)
        db.session.commit()
    return render_template("algoritmo2/algoritmo2.html", usuario = current_user, vento = vento, swell = swell, direcao = direcao, rolando = rolando)

@views.route("/hist", methods=["GET","POST"])
@login_required
def hist():
    return render_template("algoritmo2/hist.html", usuario = current_user)