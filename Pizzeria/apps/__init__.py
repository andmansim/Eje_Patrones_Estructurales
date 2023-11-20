'''
Este archivo se encarga de conectar la web con el código
'''
import sys
sys.path.append('C:/Users/andre/Documents/GitHub2/Eje_Patrones_Estructurales/Pizzeria')
from flask import render_template, request, redirect, Flask, flash
from codigoPizza import builders
from codigoPizza import manejardatos
from codigoPizza.pedido_pizza import guardar_pedido_en_csv
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Genera una clave secreta hexadecimal de 16 bytes

director = builders.Director() #Chef
builder = builders.ConcreteBuilder1() #Tipo de pizza
web_pizza = manejardatos.WebPizzeria()

#Rutas para las distintas página

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/pizzapersonalizada', methods=['GET', 'POST'])
def pizzapersonalizada():
    return render_template('Pizzassueltas.html')

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def inicio_sesion():
    return render_template('login.html')

@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    return render_template('registro.html')

@app.route('/combos_general', methods=['GET', 'POST'])
def combos_general():
    return render_template('Combos.html')

@app.route('/combos_per', methods=['GET', 'POST'])
def combos_per():
    return render_template('CombosPersonalizados.html')

@app.route('/mensaje_procesado')
def mensaje_procesado():
    mensaje = flash('success')  # Recupera el mensaje almacenado con flash
    return render_template('mensaje_procesado.html', mensaje=mensaje)

#Ruta para recoger los datos de la pizza personalizada
@app.route('/datos_pizza_per', methods=['POST']) #recibimos los datos en el fichero procesar_pizza
def datos_pizza_per():
    #generamos un id para cada pedido
    id_cliente = secrets.token_hex(4)
    #recogemos los datos en las dinstintas variables
    masa = request.form.get('masa')
    salsa = request.form.get('salsa')
    ingredientes = [request.form.get('ingredientes_queso'), request.form.get('ingredientes_jamon'), 
                    request.form.get('ingredientes_bacon'), request.form.get('ingredientes_cebolla'), 
                    request.form.get('ingredientes_pimiento'), request.form.get('ingredientes_champinon'), 
                    request.form.get('ingredientes_pina'), request.form.get('ingredientes_atun'), 
                    request.form.get('ingredientes_aceitunas'), request.form.get('ingredientes_carne'), 
                    request.form.get('ingredientes_salchicha'), request.form.get('ingredientes_pollo'), 
                    request.form.get('ingredientes_tomate'), request.form.get('ingredientes_piña'),
                    request.form.get('ingredientes_maiz'), request.form.get('ingredientes_pepperoni'), 
                    request.form.get('ingredientes_oregano'), request.form.get('ingredientes_albahaca'), 
                    request.form.get('ingredientes_rucula'), request.form.get('ingredientes_perejil'),
                    ]
    
    #en caso de no elegir los ingredientes, se le asigna un valor vacio
    for i in range(len(ingredientes)):
        if ingredientes[i] == None:
            ingredientes[i]=''
            
    coccion = request.form.get('coccion')
    presentacion = request.form.get('presentacion')
    bebida = request.form.get('bebida')
    postre = request.form.get('postre')

    
    #Contruimos la pizza
    director.builder = builder #Le decimos al chef que tipo de pizza queremos
    director.build_pizza(masa, salsa, str(ingredientes), coccion, presentacion, bebida, postre) #Le decimos al chef los pasos a seguir para dicha pizza
    builder.pizza.list_parts()
    a = builder.pizza.get_parts() #Lista con todos los datos de la pizza
    print(a)
    
    # Guardamos los datos del pedido en el archivo CSV asociado al ID del cliente
    guardar_pedido_en_csv(id_cliente, a)

    mensaje = '¡Datos de la pizza procesados con éxito!'
    flash(mensaje, 'success')  # Almacena el mensaje para mostrarlo en la siguiente solicitud

    # Redirige a una nueva página para mostrar el mensaje
    return redirect('/mensaje_procesado')   

#Ruta para coger los datos del login  
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('username')
        contrasenia = request.form.get('password')
        print(usuario, contrasenia)
        if web_pizza.login(usuario, contrasenia):
            return redirect('/home')
        else:
            return render_template('login.html')
    return render_template('index.html')

#registro ususario
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form.get('username')
        contrasenia = request.form.get('password')
        #Debe comprobar la contraseña que sea la misma en los dos campos
        correo = request.form.get('email')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')
        print(usuario, contrasenia, correo, telefono, direccion)
    
    return render_template('index.html')
        


if __name__ == '__main__':
    app.run(debug=True)
    
