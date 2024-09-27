# app/auth/routes.py
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user

from models import db, User
from utils.forms.LoginForm import LoginForm

loginBlueprint = Blueprint('login', __name__)


@loginBlueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.matchPassword(form.password.data):
            login_user(user)
            user.addLogin()
            db.session.commit()
            print('Login successful!')
            return redirect(url_for('index.index'))
        else:
            print('Invalid username or password.')
    return render_template('login.jinja.html', form=form)
