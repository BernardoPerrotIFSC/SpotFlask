from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Condicao


views = Blueprint('views', __name__)

# @views.route('/home', )

@views.route('/')
def home():
    return render_template('home.html', usuario=current_user)

@views.route('/algoritmo', methods=['GET', 'POST'])
@login_required
def algoritmo():
    vento = None
    tamanho_swell = None
    direcao_swell = None
    lista = None
    if request.method == 'POST':
        vento = int(request.form.get('vento'))
        tamanho_swell = float(request.form.get('tamanho'))
        direcao_swell = int(request.form.get('swell'))
        guarda = Condicao("Guarda do Embaú", 50, 270, 1.1, 2.8, 80, 180, "fechado")
        gamboa = Condicao("Gamboa",180, 290, 1.4, 2.5, 90, 135, "fechado")
        #garopaba
        garopabinha = Condicao("Garopabinha", 180, 290, 1.1, 1.7, 70, 120, "fechado")
        # lajinha = Condicao()
        silveiranorte = Condicao("Silveira Norte",22, 247, 1.1, 2.0, 70, 140, "fechado")
        tayson = Condicao("Tayson", 65, 360, 1.1, 2.0, 70, 135, "bandeira")
        silveirasul = Condicao("Silveira Sul", 65, 360, 1.6, 4, 80, 190, "bandeira")
        ferrugem = Condicao("Ferrugem", 67, 247, 1.1, 1.9, 80, 190, "aberto")
        barrinha = Condicao("Barrinha", 160, 290, 1.1, 1.7, 70, 190, "fechado")
        barranorte = Condicao("Barra Norte", 180, 380, 1.1, 1.7, 80, 180, "fechado")
        barra = Condicao("Barra SUl", 257, 280, 1.1, 1.8, 70, 190, "fechado")
        ouvidor = Condicao("Ouvidor", 180, 290, 1.1, 1.6, 80, 157, "fechado")
        vermelha = Condicao("Vermelha",180, 280, 1.3, 2.0, 80, 157, "fechado")
            
        #imbituba
        rosanorte = Condicao("Rosa Norte", 75, 135, 1.0, 2.0, 75, 185, "aberto")
        rosasul = Condicao("Rosa Sul",135, 270, 1.0, 4.5, 55, 200, "bandeira")
        luz = Condicao("luz", 120, 270, 1.0, 1.8, 65, 180, "fechado")
        ibiraquera = Condicao("Ibiraquera", 45, 240, 1.0, 2.5, 60, 180, "bandeira")
        ribanceira = Condicao("Ribanceira", 160, 270, 1.0, 3.0, 70, 190, "bandeira")
        praiadagua = Condicao("Praia d'água", 180, 270, 1.1, 1.7, 90, 185, "aberto")
        portinho = Condicao("Portinho",135, 270, 1.1, 2.5, 67.5, 135, "aberto")
        praiadavila = Condicao("Vila",67, 240, 1.1, 3.0, 112, 200, "bandeira")
        # castelinho = Condicao()
        itapirasul = Condicao("Itapiruba Sul",157, 270, 1.2, 2.0, 90, 135, "fechado")
        itapiranorte = Condicao("Itapiruba Norte",67, 315, 1.0, 1.8, 67, 200, "bandeira")
            
        #laguna
        gisul = Condicao("Gi Sul",190, 270, 1.5, 2.2, 70, 130, "aberto")
        ginorte = Condicao("Gi Norte", 10, 290, 1.0, 1.5, 70, 180, "aberto")
        ravena = Condicao("Ravena",150, 270, 1.6, 2.2, 90, 185, "aberto")
        ponta = Condicao("Ponta",170, 270, 1.3, 1.6, 90, 185, "aberto")

        #FarolDeSantaMarta
        tereza = Condicao("Tereza",157, 270, 1.3, 2.5, 90, 190, "aberto")
        ipua = Condicao("Ipuã", 67, 270, 1.1, 2.8, 90, 190, "aberto")
        galheta = Condicao("Galheta", 67, 270, 1.1, 2.8, 90, 190, "aberto")
        cardoso = Condicao("Cardoso", 67, 245, 1.1, 5, 90, 190, "aberto")
        cigana = Condicao("Cigana", 67, 270, 1.1, 2.3, 100, 200, "aberto")

        Picos_Nordeste = [guarda, silveiranorte, ferrugem, barranorte, rosanorte, ibiraquera, praiadavila, itapiranorte,  ginorte, ipua, galheta, cardoso, cigana]

        Picos_Sul = [gamboa, garopabinha, tayson, silveirasul, barrinha, barra, ouvidor, vermelha, rosasul, luz, ribanceira, praiadagua, portinho, itapirasul, gisul, ravena, ponta, tereza]
        lista = []
        
        for pico in Picos_Nordeste:
            if vento <= pico._ventomin or vento >= pico._ventomax:
                if tamanho_swell >= pico._tam_swellmin and tamanho_swell <= pico._tam_swellmax:
                    if direcao_swell >= pico._dir_swellmin and direcao_swell <= pico._dir_swellmax:
                        lista.append(pico._nome)

        for pico in Picos_Sul:
            if vento >= pico._ventomin and vento <= pico._ventomax:
                if tamanho_swell >= pico._tam_swellmin and tamanho_swell <= pico._tam_swellmax:
                    if direcao_swell >= pico._dir_swellmin and direcao_swell <= pico._dir_swellmax:
                        lista.append(pico._nome)
        

    return render_template('algoritmo.html', usuario=current_user, vento = vento, tamanho_swell=tamanho_swell, direcao_swell= direcao_swell, lista=lista)