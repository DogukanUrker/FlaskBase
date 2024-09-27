from flask import Blueprint, render_template, request, redirect, url_for, flash

from models import db, User
from utils.forms.RegisterForm import RegistrationForm
from utils.generateID import generateID
from utils.passwordHash import hashPassword

signUpBlueprint = Blueprint('signup', __name__)


@signUpBlueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashedPassword = hashPassword(form.password.data)
        newUser = User(
            id=generateID(form.username.data),
            username=form.username.data,
            email=form.email.data,
            password=hashedPassword,
            firstName=form.firstName.data,
            lastName=form.lastName.data
        )
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("index.index"))
    elif request.method == 'POST':
        flash("Please fill out all fields correctly.", "danger")
    return render_template("signup.jinja.html", form=form)
