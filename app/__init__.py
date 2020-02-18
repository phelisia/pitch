from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config_options
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()
migrate = Migrate()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
   app = Flask(__name__)
   app.config.from_object(config_options[config_name])

   #  Initializing flask extensions
   bootstrap.init_app(app)
   migrate.init_app(app, db)
   db.init_app(app)
   login_manager.init_app(app)

   from .auth import auth as auth_blueprint
   app.register_blueprint(auth_blueprint,url_prefix = '/authenticate') 
   from .main import main as main_blueprint
   app.register_blueprint(main_blueprint)

   # setting config

   return app