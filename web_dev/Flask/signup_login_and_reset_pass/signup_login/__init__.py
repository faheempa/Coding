from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from signup_login.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from signup_login import routes

# creating dabaase and tables if not already
with app.app_context():
    db.create_all()
    db.session.commit()