# importing libraries & modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# Config
app.config['SECRET_KEY'] = 'ed19b073d26ce22b71f0555954ebcbb7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# from flaskblog import blueprint routes
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

# registering blueprints
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

from flaskblog.models import User
