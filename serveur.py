from flask import Flask 


app = Flask(__name__)

@app.route('/')
def hello(0):
    return "hello world"