from flask import Flask, jsonify, request
import os
import sys

sys.path.append('..')  # ugly hack TODO lol dont fix it :)
import CheckCases

app = Flask(__name__, static_url_path='/static/')


class InvalidUsage(Exception):  # from https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/health/')
def health():
    return jsonify({'message': 'Hello, World! I am a web API.',
                    'health': 'OK'})


@app.route('/api/getCovidJSONByIllinoisCounty')
def getCovidJSONByIllinoisCounty():
    if 'county' not in request.args:
        raise InvalidUsage('You must specify the "county" parameter', status_code=422)

    try:
        result: dict = (CheckCases.get_covid_info_for_county_ILLINOIS(request.args.get('county')))
    except CheckCases.CountyNotFoundException as e:
        raise InvalidUsage('County "' + request.args.get('county') + '" does not exist!')

    return jsonify(result)


if __name__ == '__main__':
    print("Try 'flask run'.")
