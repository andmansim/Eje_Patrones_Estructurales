'''
Este archivo se encarga de conectar la web con el código
'''
from flask import render_template, request, redirect, Flask
from codigoPizza import builders, manejardatos

app = Flask(__name__)

director = builders.Director() #Chef
builder = builders.ConcreteBuilder1() #Tipo de pizza
web_pizza = manejardatos.WebPizzeria()

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/pizzapersonalizada', methods=['GET', 'POST'])
def pizzapersonalizada():
    return render_template('Pizzassueltas.html')

@app.route('/form   ', methods=['POST']) #recibimos los datos en el fichero procesar_pizza
def procesar_pizza():
    print(request.get_data()) #imprimimos los datos recibidos
    #recogemos los datos en las dinstintas variables
    masa = request.form.get('masa')
    salsa = request.form.get('salsa')
    ingredientes = request.form.get('ingredientes')
    coccion = request.form.get('coccion')
    presentacion = request.form.get('presentacion')
    bebida = request.form.get('bebida')
    postre = request.form.get('postre')

    
    #Contruimos la pizza
    director.builder = builder #Le decimos al chef que tipo de pizza queremos
    director.build_pizza(masa, salsa, ingredientes, coccion, presentacion, bebida, postre) #Le decimos al chef los pasos a seguir para dicha pizza
    builder.pizza.list_parts()
    a = builder.pizza.get_parts() #Lista con todos los datos de la pizza

#registro ususario
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    
from apps import routes