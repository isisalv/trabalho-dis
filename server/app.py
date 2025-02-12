from flask import Flask, request, jsonify
from .algo import gerar_imagem
import psutil, csv
from celery.result import AsyncResult
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods = ['POST'])
def post_imagem():
    try:
        result = gerar_imagem.delay(
                    request.files['file'].read(), 
                    request.form.get('user'))
        return {'cpu': psutil.cpu_percent(), 'ram': psutil.virtual_memory().percent, 'result_id' : result.id}
    except Exception as e:
        print(e)
    
@app.route("/<string:result_id>")
def get_result(result_id):
    result = AsyncResult(result_id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.get(),
    }