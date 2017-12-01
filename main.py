# coding=utf-8
# !/usr/bin/env python

import os
import webbrowser



def run_python_program(program_name):
    os.system("gnome-terminal -e 'bash -c \"python " + program_name + "\"'")



print 'Levantando el microservicio sv_gestor_tweets.py'
run_python_program('servicios/sv_gestor_tweets.py')
print 'Levantando el microservicio sv_analizador_tweets.py'
run_python_program('servicios/sv_analizador_tweets.py')
print 'Levantando el microservicio sv_information.py'
run_python_program('servicios/sv_information.py')

# Se levanta el API Gateway.
print 'Levantando el api_gateway.py'
run_python_program('api_gateway.py')

# Se levanta la GUI.
print 'Levantando el gui.py'
run_python_program('gui.py')

# Se acabó la inicialización del sistema
print 'SE levnato correctamente'

webbrowser.open('http://localhost:8088', new=0)
