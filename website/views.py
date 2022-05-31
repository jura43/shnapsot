from flask import Blueprint, render_template
from flask_login import current_user, login_required

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html', user=current_user)

@views.route('/users')
@login_required
def users():
    return render_template('users.html', user=current_user)

@views.route('/user/<user_id>')
def user(user_id):
    return render_template('user.html', user=current_user)

@views.route('/online')
@login_required
def online():
    return render_template('online.html', user=current_user)