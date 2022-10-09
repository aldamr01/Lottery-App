from flask import Blueprint, redirect, url_for, render_template, flash
from apps.auth.models import User
from apps.auth.forms import LoginForm, RegisterForm
from extensions import db, login_manager
from flask_login import login_user, login_required, current_user, logout_user

import bcrypt

auth_blueprint = Blueprint('auth', __name__, template_folder="templates")

@auth_blueprint.route('/login', methods=["GET", "POST"])
def login():    
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:            
            
            if bcrypt.checkpw(form.password.data.encode('utf-8'), user.password.encode('utf-8')):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("dashboard.index"))
        
        
        flash("Credentials not match!", "danger")
        return redirect(url_for("auth.login"))
        
    return render_template("login.html", form=form)

@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))

    form = RegisterForm()
    
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        
        if user:
            flash("Email has already been registered!", "danger")
            return redirect(url_for('auth.register'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, name=name, password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash("Register new user success!", "success")
        return redirect(url_for('auth.register'))
            
    return render_template("register.html", form=form)

@auth_blueprint.route('/logout', methods=["GET"])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("auth.login"))

@login_manager.user_loader
def user_loader(user_id):   
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth.login"))