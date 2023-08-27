from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Condicao


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', usuario=current_user)

@views.route('/algoritmo', methods=['GET', 'POST'])
@login_required
def algoritmo():
    if request.method == 'POST':
        vento = request.form.get('vento')
        tamanho_swell = request.form.get('tamanho')
        direcao_swell = request.form.get('swell')

    return render_template('algoritmo.html', usuario= current_user, vento=vento)