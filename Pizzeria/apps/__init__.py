'''
Este archivo se encarga de conectar la web con el código
'''
import sys
sys.path.append('C:/Users/andre/Documents/GitHub2/Eje_Patrones_Estructurales/Pizzeria')
from flask import render_template, request, redirect, Flask, flash, url_for
from codigoPizza import builders
from codigoPizza.pedido_pizza import guardar_pedido_en_csv
from codigoPizza import datos_usuario
from codigoPizza import composite
from codigoPizza import menus
from codigoPizza import datos_usuario
import csv

import secrets

precios = {'agua':1.5, 'sopresa':3, 'vino_blaco':2.5, 'cerveza':2.5, 'zumo':1.5, 'leche':1.5, 
           'cafe': 2, 'infusion':1, 'licor':4, 'cava':4, 'batido':2, 'smoothie':2.25, 'granizado':2, 
           'te': 3, 'fanta':6, 'coca_cola':7, 'pepsi':5, 'yogurt':3, 'helado':6, 'tarta':9, 'fruta':1, 
           'galletas':3, 'postre_del_dia':6, 'flan':2, 'tarta_de_queso':8, 'tarta_de_chocolate':5, 
           'pizza': 15, 'barbacoa': 12, 'napolitana':13, '4_quesos':16, 'margarita':10, 
           'carbonara':16, 'cuatro_estaciones':18, 'especial':20}
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Genera una clave secreta hexadecimal de 16 bytes

director = builders.Director() #Chef
builder = builders.ConcreteBuilder1() #Tipo de pizza

directormenu = menus.Director() #Chef
buildermenu = menus.ConcreteBuilderMenu1() #Tipo de menu

with open('usuarios.csv', mode='w', newline='') as file:
    writer= csv.writer(file)
    writer.writerow(['usuario', 'contrasenia', 'correo', 'telefono', 'direccion'])

#Rutas para las distintas páginas

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



#Rutas para recolectar y manejar datos
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

    mensaje = '¡Datos del pedido procesados con éxito!'
    flash(mensaje, 'success')  # Almacena el mensaje para mostrarlo en la siguiente solicitud

    # Redirige a una nueva página para mostrar el mensaje
    return redirect('/mensaje_procesado')   



#Ruta para coger los datos del login  
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form.get('username')
        contrasenia = request.form.get('password')

        usuario = datos_usuario.Usuario(nombre, '', '', '', contrasenia)
        if usuario.usuario_valido():
            return render_template('index.html')
        else:
            print('Usuario no valido')
            return render_template('login.html')
        # Comprobar si el usuario y la contraseña coinciden en el archivo CSV de usuarios
        
    

#registro ususario
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('username')
        contrasenia = request.form.get('password')
        correo = request.form.get('email')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')

        usuario = datos_usuario.Usuario(nombre, direccion, telefono, correo, contrasenia)
        if usuario.usuario_existe():
            print('Usuario ya existe')
            return render_template('registro.html')
        else:
            usuario.registrar_usuario()
            return render_template('index.html')

def precios_funct(precios, dato):
    padre = composite.Composite()
    for j in dato:
        for key, value in precios:
            if j == key:
                hoja = composite.Leaf(value)
                padre.add(hoja)
    precio_total = composite.client_code(padre)      
    return precio_total

@app.route('/datos_combo_per', methods=['POST']) 
def datos_combo_per():
    #generamos un id para cada pedido
    id_menu = secrets.token_hex(4)
    combo = [request.form.get('combo1'), request.form.get('combo2'), 
            request.form.get('combo3')]
    for i in range(len(combo)):
            if combo[i] == None:
                combo[i]=''
            if combo[i] =='combo1':
                nombre = request.form.get('combo')
                pizza = 'Barbacoa'
                bebida = request.form.get('bebida')
                postre = request.form.get('postre')
            elif combo[i] == 'combo2':
                nombre = request.form.get('combo')
                bebida = 'Fanta'
                postre = 'Flan'
                pizza = request.form.get('pizza')
            elif combo[i] == 'combo3':
                nombre = request.form.get('combo')
                pizza = 'Napolitana'
                bebida = request.form.get('bebida')
                postre = request.form.get('postre')
            
    
    precio1 = precios_funct(precios, [bebida, pizza, postre])
    #Contruimos el combo
    directormenu.builder = buildermenu
    directormenu.build_menu(nombre, bebida, postre, pizza, precio1)
    buildermenu.menu.list_parts()
    a = buildermenu.menu.get_parts()
    print(a)
    guardar_pedido_en_csv(id_menu, a)
    mensaje = '¡Datos del pedido se han procesado con éxito!'
    flash(mensaje, 'success')  # Almacena el mensaje para mostrarlo en la siguiente solicitud

    # Redirige a una nueva página para mostrar el mensaje
    return redirect('/mensaje_procesado')   

@app.route('/datos_combo', methods=['POST'])
def datos_combo():
    if request.method == 'POST':
        #generamos un id para cada pedido
        id_menu = secrets.token_hex(4)
        combo = [request.form.get('combo1'), request.form.get('combo2'), 
                 request.form.get('combo3'), request.form.get('combo4'),
                 request.form.get('combo5'), request.form.get('combo6')]
        for i in range(len(combo)):
            if combo[i] == None:
                combo[i]=''
            if combo[i] == 'combo1':
                nombre = 'Combo 1'
                bebida = 'Pepsi'
                pizza = 'Barbacoa'
                postre= 'Helado'
                
            elif combo[i] == 'combo2':
                nombre = 'Combo 2'
                bebida = 'Coca-Cola'
                pizza = 'Napolitana'
                postre= 'Fruta'
            elif combo[i] == 'combo3':
                nombre = 'Combo 3'
                bebida = 'Fanta'
                pizza = '4 Quesos'
                postre= 'Flan'
            elif combo[i] == 'combo4':
                nombre = 'Combo 4'
                bebida = 'Granizado'
                pizza = 'Margarita'
                postre= 'Tarta de queso'
            elif combo[i] == 'combo5':
                nombre = 'Combo 5'
                bebida = 'Agua'
                pizza = 'Carbonara'
                postre= 'Tarta de chocolate'
            elif combo[i] == 'combo6':
                nombre = 'Combo 6'
                bebida = 'Cerveza'
                pizza = 'Cuatro estaciones'
                postre= 'Galletas'
        precio1 = precios_funct(precios, [bebida, pizza, postre])
        directormenu.builder = buildermenu
        directormenu.build_menu(nombre, bebida, postre, pizza, precio1)
        buildermenu.menu.list_parts()
        a = buildermenu.menu.get_parts()
        print(a)
        guardar_pedido_en_csv(id_menu, a)
        mensaje = '¡Datos del pedido se han procesado con éxito!'
        flash(mensaje, 'success')  # Almacena el mensaje para mostrarlo en la siguiente solicitud

        # Redirige a una nueva página para mostrar el mensaje
        return redirect('/mensaje_procesado')     
        
        
if __name__ == '__main__':
    app.run(debug=True)
    