import os

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from from_root import from_root

route_api = Blueprint('router', __name__)


UPLOAD_FOLDER = from_root('soundFiles')

APP_ROOT = os.path.abspath(os.curdir)

@route_api.route("/hello")
def hello():
    return "hello"


@route_api.route('/upload')
def upload_file():
    return render_template('upload.html')


@route_api.route('/uploader', methods=['GET', 'POST'])
def upload_file_api():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER,secure_filename(f.filename)))
        return 'file uploaded successfully'