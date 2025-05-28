from flask import Flask

app_flask = Flask(__name__)

@app_flask.route('/')
def hello_world():
    return 'Hello, World! This is a Flask app running in a Docker container.' 

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port=5000)