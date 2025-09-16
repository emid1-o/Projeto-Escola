from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))




app = Flask(__name__)
app.config['SECRET_KEY'] = '0a6666ca7be09ffc36e16fe5ed2ce898'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

migrate = Migrate(app, db)

MAIL_USERNAME = os.environ.get('EMAIL_USER')
MAIL_PASSWORD = os.environ.get('EMAIL_PASS')






from siteMain.users.routes import users
from siteMain.posts.routes import posts
from siteMain.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)