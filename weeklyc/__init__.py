from flask import Flask
from flask.ext.login import LoginManager
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] =\
    "zI\xd6{\xdd\xabr5\xcdt\xe1\xe7\x8c\x83\xc7\xf0\x86\xb1N\x05\xa9" +\
    "1\r\xd9uG\x8f\xe8\x8c\xa1`6\xcdE8\xf1\xfe\x9dQ[\xc0&rNa\xd1\xcd" +\
    "\x8f \x0c5\xd1\xf7\xd1\xcc,\xd7\xd9\xe5\x9d\xd8\x98\x10\xb4\xfe"

login_manager = LoginManager()
#login_manager.login_view = 'login'
login_manager.setup_app(app)

import weeklyc.views

@app.teardown_request
def shutdown_session(exception=None):
    from weeklyc.database import db_session
    db_session.remove()
