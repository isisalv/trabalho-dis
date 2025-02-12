from flask import Flask, request
from . import algo

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods = ['POST'])
def post_imagem():
    algo.gerar_imagem(request.files['file'], 
                    request.form.get('user'))
    return "<p>Hello, World!</p>"