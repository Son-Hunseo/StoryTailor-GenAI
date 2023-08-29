from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
import json

app = Flask(__name__)
CORS(app)


@app.route('/tailor/chat', methods=['POST'])
def make_quiz():
    return 0


@app.route('/tailor/make_story', methods=['POST'])
def make_chat():
    return 0


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')