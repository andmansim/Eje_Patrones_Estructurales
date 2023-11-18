'''
Este archivo contiene las rutas específicas de la applicación
Puedo definir las rutas y funciones asociadas a ellas aquí
'''
from flask import render_template, request, redirect, url_for
from app import app, director
from codigoPizza import builders

@app.route('/')
def home():
    return render_template('index.html')


def pizzapersonalizada():
    pizza = director.build_pizza() #Le decimos al chef los pasos a seguir para dicha pizza
    return render_template('Pizzassueltas.html', pizza = pizza)

@app.route('/procesar_pizza', methods=['POST']) #rcibimos los datos en el fichero procesar_pizza
def procesar_pizza():
    masa = request.form['masa']
    salsa = request.form['salsa']
    ingredientes = request.form['ingredientes']
    coccion = request.form['coccion']
    presentacion = request.form['presentacion']
    bebida = request.form['bebida']
    postre = request.form['postre']
    
    #le pasamos los datos a la clase builder
    director = builders.Director() #Chef
    builder = builders.ConcreteBuilder1() #Tipo de pizza
    director.builder = builder #Le decimos al chef que tipo de pizza queremos
    director.build_pizza(masa, salsa, ingredientes, coccion, presentacion, bebida, postre) #Le decimos al chef los pasos a seguir para dicha pizza
    builder.pizza.list_parts()
    a = builder.pizza.get_parts() #Lista con todos los datos de la pizza
    return redirect(url_for('index.html')) #redirigimos a la página principal