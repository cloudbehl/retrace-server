from flask import Flask
from flask import request
from rest.tasks import test

app = Flask(__name__)

@app.route('/api/v1/tasks')
def hello_world():
    return test()

if __name__ == '__main__':
    app.run(port=5001)