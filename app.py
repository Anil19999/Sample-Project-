from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def hello_world():
    app.logger.info('Hello World endpoint was reached')
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return 'webapp_requests_total{path="/"} 1\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
