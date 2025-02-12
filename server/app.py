from flask import Flask, request, jsonify
from . import algo
import psutil

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods = ['POST'])
def post_imagem():
    algo.gerar_imagem(
                request.files['file'], 
                request.form.get('user'))
    return jsonify(cpu = psutil.cpu_percent(), ram = psutil.virtual_memory().percent)
    