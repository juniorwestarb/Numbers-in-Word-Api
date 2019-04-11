# _*_ coding: utf-8 _*_
from flask import Flask, jsonify
import extenso as ex

app =  Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Não encontrado'}), 404


@app.route('/<string:numero>', methods=['GET'])
def get(numero):
    try:
        inteiro = numero.replace("-","")
        if inteiro.isdigit() and len(inteiro) <= 5:
            num = ex.converter(numero)
            print(num)
            return jsonify({'extenso': '{0}'.format(num)}), 200
        else:    
            return jsonify({'error': 'numero invalido, entre com um numero entre -99999 e 99999'}), 200
    except:
        return jsonify({'error': 'erro ao processar requisicao'}), 500


if __name__ == '__main__':
    app.run(port=3000)