import os
from flask import Flask, jsonify, request
from math import sqrt


app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    contador = 0
    primeiro = 0
    proximo = 1
    fibo = 0
    result = "Sequencia Fibonacci"

    while contador < 50:
        fibo = primeiro + proximo
        primeiro = proximo
        proximo = fibo
        contador = contador + 1
        result = result + str(fibo) + "   -   "
    return result

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
