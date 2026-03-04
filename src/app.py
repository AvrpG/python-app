from datetime import datetime
import socket

from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/api/v1/details')
def details():
    return jsonify({"time": datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
                    "message": "This is the endpoint for details API  -- testing ARGO deployment is successful !!! <3 <3 <3", "host": socket.gethostname()}), 200

@app.route('/api/v1/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")