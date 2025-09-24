from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    ip = '192.168.35.130'
    # app.run(host=ip, port=5000, debug=True)
    app.run(debug=True)
