import os

from flask import Blueprint, render_template, request, jsonify, abort
from werkzeug.utils import secure_filename
from from_root import from_root
from flask_cors import cross_origin

route_api = Blueprint('router', __name__)


UPLOAD_FOLDER = from_root('soundFiles')

APP_ROOT = os.path.abspath(os.curdir)

@route_api.route("/hello")
def hello():
    return "hello"


@route_api.route('/upload')
def upload_file():
    return render_template('upload.html')


@route_api.route('/uploader', methods=[ 'POST'])
@cross_origin()
def upload_file_api():
    try:
        if request.method == 'POST':
            f = request.files['file']
            f.save(os.path.join(UPLOAD_FOLDER,secure_filename(f.filename)))

            return jsonify({
                'status' : 200,
                'success': True,
                'filename': f.filename
            })
    except:
        return jsonify({
            'status': 404,
            'success': False,
            'filename': "No file Saved"
        })


@route_api.route('/process', methods=['POST'])
def process_file_api():

    try:
        if request.method == 'POST':
            ##TODO do the processing here get the result and set the outCom

            return jsonify({
                'status': 200,
                'success': True,
                'message': "Process Sucess",
                'outcome' : "Vehicle Sound"
            })
    except:
        return jsonify({
            'status': 404,
            'success': False,
            'filename': "No file Saved"
        })

@route_api.errorhandler(400)
@route_api.errorhandler(404)
def error_handler(error):
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code