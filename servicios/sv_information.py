# coding=utf-8
# !/usr/bin/env python

import json
import os
import requests
from flask import request
from flask.ext.api import FlaskAPI, status

app = FlaskAPI(__name__)


@app.route("/information")
def get_information():
    if 'titulo' in request.args.keys():
        titulo = request.args['titulo']
        url = 'http://www.omdbapi.com/?t=' + titulo + '&plot=full&r=json'
        response_omdb = requests.get(url, request.args)
        if 'Error' in response_omdb.json():
            error_response = {'message': response_omdb.json()['Error']}
            return error_response, status.HTTP_404_NOT_FOUND
        return response_omdb.json(), response_omdb.status_code
    else:
        error_response = {'message': 'Parámetros incompletos'}
        return  error_response, status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'Servicio sv_information'
    print '--------------------------------------------------------------------'
    port = int(os.environ.get('PORT', 8087))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
