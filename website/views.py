from flask import Blueprint, render_template
from flask_login import current_user, login_required

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html', user=current_user)

@views.route('/rooms')
@login_required
def rooms():
    rooms = ['general', 'test', 'demo', 'random']
    return render_template('chat_rooms.html', user=current_user, rooms=rooms)

@views.route('/room/<room_id>')
@login_required
def join_room(room_id):
    room = room_id
    return render_template('chatroom.html', user=current_user, room=room)

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