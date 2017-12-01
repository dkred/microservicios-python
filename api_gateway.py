# coding=utf-8
# !/usr/bin/env python


import os
import requests
from flask import request, render_template
from flask.ext.api import FlaskAPI



app = FlaskAPI(__name__)


# Ruta que llama al microservicio sv_information para que busque información
# por medio de la API de OMDb acerca de la serie o película cuyo título se
# recibe como parámetro y devuelve un JSON con los resultados.
@app.route("/api/movie/information", methods=['GET'])
def obtener_information():
    url = 'http://localhost:8087/information'
    response = requests.get(url, request.args)
    return response.json(), response.status_code


# Ruta que llama al microservicio sv_gestor_tweets para que busque los tweets
# acerca de la serie o película cuyo título se recibe como parámetro y
# devuelva un JSON con los resultados.
@app.route("/api/tweet/search", methods=['GET'])
def obtener_tweets():
    url = 'http://localhost:8084/api/tweet/search'
    response = requests.get(url, request.args)
    return response.json(), response.status_code


# Ruta que llama al microservicio sv_analizador_tweets para que analice los
# tweets que son recibidos como parámetro y devuelva un JSON con el análisis
# hecho.
@app.route("/api/tweet/analizar", methods=['POST'])
def analizar_tweets():
    url = 'http://localhost:8086/api/tweet/analizar'
    response = requests.post(url, request.form)
    return response.json(), response.status_code


'''
--------------------------------------------------------------------------------
Ejecución del API Gateway
--------------------------------------------------------------------------------
'''

if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'API Gateway'
    print '--------------------------------------------------------------------'
    port = int(os.environ.get('PORT', 8085))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
