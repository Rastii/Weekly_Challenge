from weeklyc import app, login_manager
from weeklyc.database import db_session
from weeklyc.models import *
from weeklyc.forms import *
from weeklyc.controllers import *
from flask import render_template, redirect, url_for,\
    flash, request, session, json, abort
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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("challenges"))


@app.route('/register', methods=['GET'])
def render_register(form=None):
    if form:
        return render_template('register.html', form=form)
    else:
        form = RegisterForm(request.form)
        return render_template('register.html', form=form)

@app.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate():
        if form.check_login():
            user = form.register_user()
            if user:
                login_user(user)
                return redirect(request.args.get('next') or url_for('index'))
            else:
                form.confirm.errors.append("Error in registration")
                return render_register(form)
        else:
            form.login.errors.append("Username already exists!")
            return render_register(form)
    else:
        return render_register(form)

""" Primary App Routes
"""
@app.route('/')
@login_required
def index():
    return redirect(url_for("challenges"))

@app.route('/challenges')
@login_required
def challenges():
    return render_template('challenges.html', user=current_user)

@app.route('/scoreboard')
@login_required
def scoreboard():
    return render_template('scoreboard.html', user=current_user)


""" Api App Routes
"""
@app.route('/api/challenges', methods=['GET'])
@login_required
def challenges_json():
    return json.dumps(get_challenges())

@app.route('/api/challenges/<challenge_id>/users', methods=['GET'])
@login_required
def challenge_info_json(challenge_id):
    challenge_data = get_challenge_users(challenge_id)
    if challenge_data:
        return json.dumps(challenge_data)
    else:
        abort(404)

@app.route('/api/users', methods=['GET'])
@login_required
def users_json():
    users = get_users();
    if users:
        return json.dumps(users)
    else:
        return json.dumps("")

@app.route('/api/challenges/submissions', methods=['GET'])
@login_required
def challenge_submissions_json():
    return json.dumps(get_challenge_submission_info())

@app.route('/submit/challenges/<challenge_id>', methods=['POST'])
def submit_challenge(challenge_id):
    user = current_user
    challenge = db_session.query(Challenge).filter_by(id=challenge_id).first()
    if challenge:
        if challenge in user.submissions:
            #Already solved!
            return "0"
        else:
            if request.form['key'] == challenge.flag:
                user.submissions.append(challenge)
                db_session.commit()
                return "1"
            else:
                return "0"
    else:
        abort(404)
