from flask import Blueprint, render_template

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

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/register')
def register():
    return render_template('register.html')

@views.route('/demo')
def demo():
    return render_template('demo_chat.html')

