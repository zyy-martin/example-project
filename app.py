from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/status')
def status():
    return jsonify({
        "status": "online",
        "message": "Hello from the Python backend!",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
