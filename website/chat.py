from flask_socketio import emit, join_room, leave_room
from . import socketio

@socketio.on('message')
def handleMessage(data):
    message = data['message']
    room = data['room']
    print('Message: ' + message)
    emit('message', message, to=room)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('join_announcement', username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('leave_announcement', username + ' has left the room.', to=room)