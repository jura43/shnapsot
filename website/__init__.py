from flask import Flask
from flask_socketio import SocketIO, send

class start_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    socketio = SocketIO(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')