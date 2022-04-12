from website import start_app
from flask_socketio import send

app = start_app().socketio

@app.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    app.run(start_app().app, debug=True)