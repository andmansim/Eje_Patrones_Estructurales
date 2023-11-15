'''
Este archivo contiene las rutas específicas de la applicación
Puedo definir las rutas y funciones asociadas a ellas aquí
'''
from flask import render_template
from app import app, director
from codigoPizza import funciones_main

@app.route('/')
def home():
    return render_template('index.html')

def pizzapersonalizada():
    pizza = director.build_pizza() #Le decimos al chef los pasos a seguir para dicha pizza
    return render_template('Pizzassueltas.html', pizza = pizza)