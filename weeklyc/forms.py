from wtforms import Form, TextField, PasswordField, validators,\
ValidationError
from weeklyc.models import User
from weeklyc.database import db_session
from flask.ext.bcrypt import Bcrypt
from weeklyc import app

bcrypt = Bcrypt(app)

class LoginForm(Form):
    login = TextField('Username', [
        validators.Required(message='Username is required.'),
        validators.Length(max=64, 
            message='Username must be less than 64 characters')])
    password = PasswordField('Password', [
        validators.Required(message='Password is required.'),
        validators.Length(min=6, message='Invalid password.')])

    def isUser(self):
        user = db_session.query(User).filter_by(login=self.login.data).first()
        if (user is not None and \
            bcrypt.check_password_hash(user.password, self.password.data)):
            return user
        else:
            return None

class RegisterForm(Form):
    login = TextField('Username', [
        validators.Required(message='Username is required.'),
        validators.Length(max=64,
            message='Username must be less than 64 characters')])
    password = PasswordField('Password', [
        validators.Required(message='Password is required.'),
        validators.Length(min=6,
            message='Password must be at least 6 characters'),
        ])
    confirm = PasswordField('Confirm Password', [
        validators.EqualTo('password', message='Passwords must match')])

    def check_login(self):
        if db_session.query(User).filter_by(login=self.login.data).count():
            return False
        else:
            return True

    def register_user(self):
        user = User(login=self.login.data,
                password = bcrypt.generate_password_hash(self.password.data))
        try:
            db_session.add(user)
            db_session.commit()
            return user
        except:
            return None

class ChallengeForm(Form):
    name = TextField('Challenge Name', [
        validators.Required(message='Challenge name required.'),
        validators.Length(max=64,
            message="Challenge name must be less than 64 characters.")])
    link = TextField('Challenge Link', [
        validators.Required(message='Link is required.')])

