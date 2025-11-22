from flask import Flask, render_template
from flask_socketio import SocketIO
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    username = data["username"]
    message = data["message"]
    current_time = datetime.now().strftime("%I:%M %p")

    socketio.emit(
        'new_message',
        {
            "sender": username,
            "message": message,
            "time": current_time
        },
        broadcast=True
    )

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
