from flask import Flask, render_template
from flask_cors import CORS
from monitor.api import api_bp
from monitor.capture import start_capture
from monitor.database import init_db
import threading

app = Flask(__name__)
CORS(app)

app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    init_db()

    capture_thread = threading.Thread(target=start_capture)
    capture_thread.daemon = True
    capture_thread.start()

    app.run(debug=True)