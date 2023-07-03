from flask import Flask
from Router import route_api

app = Flask(__name__)
app.register_blueprint(route_api)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
