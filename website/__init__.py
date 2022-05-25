from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
socketio = SocketIO(logger=True)

def start_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jura@10.10.10.100/shnapsot'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.debug = True

    socketio.init_app(app)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from models.model import Users

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'You need to login to access this page.'
    login_manager.login_message_category = 'error'
    login_manager.session_protection = 'strong'
    login_manager.init_app(app, socketio)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    from . import chat

    return app