from flask import Blueprint, render_template
from forms.login_form import LoginForm

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/rooms')
def rooms():
    return render_template('chat_rooms.html')

@views.route('/users')
def users():
    return render_template('users.html')

@views.route('/login', methods=['GET', 'POST'])
def login():
    login = LoginForm()
    return render_template('login.html', login=login, errors=login.errors)

@views.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@views.route('/demo')
def demo():
    return render_template('demo_chat.html')

