from weeklyc import app, login_manager
from weeklyc.database import db_session
from weeklyc.models import *
from weeklyc.forms import *
from weeklyc.controllers import *
from flask import render_template, redirect, url_for,\
    flash, request, session, json
from flask.ext.login import login_required, login_user,\
    logout_user, current_user
from flask.ext.principal import Principal, Permission, RoleNeed
from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt(app)

""" User Auth Routes
"""
@login_manager.user_loader
def load_user(uid):
    return db_session.query(User).get(uid)

@app.route('/login', methods=['GET'])
def render_login(form=None):
    if form:
        return render_template('login.html', form=form)
    else:
        form = LoginForm(request.form)
        return render_template('login.html', form=form)

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        user = form.isUser()
        if (user is not None):
            login_user(user)
            return redirect(request.args.get("next") or url_for('index')) 
        else:
            return render_login(form)
    else:
        return render_login(form)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for("render_login"))


@app.route('/register', methods=['GET'])
def render_egister():
    return "Not Done"

@app.route('/register', methods=['POST'])
def register():
    return "Not Done"

""" Primary App Routes
"""
@app.route('/')
@login_required
def index():
    if current_user:
        print current_user
    return render_template('index.html', user=current_user)
