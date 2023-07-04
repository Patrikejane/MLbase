from flask import Flask
from Router import route_api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.register_blueprint(route_api)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
