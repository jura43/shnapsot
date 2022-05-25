from flask import request
from flask_socketio import emit
from flask_login import current_user
from . import socketio

users = {}
users_priv = {}

@socketio.on('connect', namespace='/')
def connect_handler():
    if current_user.is_authenticated:
        data = current_user.username
        users[data] = request.sid
        emit('join_announcement', data, broadcast=True)
        emit('user_list', users)
    else:
        return False

@socketio.on('connect', namespace='/private')
def connect_handler():
    data = current_user.username
    users_priv[data] = request.sid

@socketio.on('message', namespace='/private')
def handleMessage(data):
    print(data)
    recepient = users_priv[data['recepient']]
    emit('deliver_message', data, to=recepient)


@socketio.on('disconnect')
def disconnect():
    data = current_user.username
    emit('leave_announcement', data, broadcast=True)


@socketio.on('tooltip', namespace='/private')
def tooltip(data):
    recepient = users_priv[data['recepient']]
    emit('notification', data, to=recepient)