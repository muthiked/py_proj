from flask import Flask
from flask_cors import CORS
from app import api
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'My First API !!'
