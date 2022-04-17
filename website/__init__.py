from flask import Flask
from flask_socketio import SocketIO, send
from flask_meld import Meld

class start_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    socketio = SocketIO(app)

    meld = Meld()
    meld.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')