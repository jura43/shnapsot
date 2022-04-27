from flask import Blueprint, render_template
from flask_login import current_user, login_required
from forms.login_form import LoginForm

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html', user=current_user)

@views.route('/rooms')
@login_required
def rooms():
    return render_template('chat_rooms.html', user=current_user)

@views.route('/users')
@login_required
def users():
    return render_template('users.html', user=current_user)

@views.route('/demo')
def demo():
    return render_template('demo_chat.html')

