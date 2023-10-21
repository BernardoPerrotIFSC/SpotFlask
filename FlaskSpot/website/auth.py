from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

from website import db 
from .models import Usuario

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario:
            if check_password_hash(usuario.senha, senha):
                flash("Login efetuado!", category='success')
                login_user(usuario, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Senha incorreta. Tente novamente.", category=True)
        else:
            flash("Email não existe!", category='error')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods= ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        senha2 = request.form.get('senha2')

        usuario = Usuario.query.filter_by(email=email).first()

        if len(email)<10:
            flash('Email deve ter mais de 10 caracteres', category='error')
        elif len(nome)<2:
            flash('Nome deve ter mais de 2 caracteres',category='error')
        elif senha != senha2:
            flash('Sua senha não confere', category='error')
        elif len(senha)<7:
            flash('Senha de ter mais de 7 caracteres', category='error')
        else:
            usuario = Usuario(email=email, nome = nome, senha = generate_password_hash(senha,method='sha256'))
            db.session.add(usuario)
            db.session.commit()
            login_user(usuario, remember=True)
            flash('Conta Criada', category='success')
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html")
