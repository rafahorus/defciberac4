import os
from flask import Flask, jsonify, request
from math import sqrt


app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    anterior = 0
    proximo = 0

    while(proximo < 50):
        print(proximo)
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
        proximo = proximo + 1


if __name__ == "__main__":
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
    
