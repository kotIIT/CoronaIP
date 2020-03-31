from flask import Flask, jsonify
import os
import sys

sys.path.append('..')  # ugly hack TODO lol dont fix it :)
import CheckCases

app = Flask(__name__, static_url_path='/static/')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/health/')
def health():
    return jsonify({'message': 'Hello, World! I am a web API.',
                    'health': 'OK'})


@app.route('/api/getCountyByZIP')
def getCountyByMyIP():
    return jsonify({'to': 'do'})


if __name__ == '__main__':
    print("Try 'flask run'.")
