'''
Este archivo contiene las rutas de la aplicación web, en otras palabras se encarga de la conexión 
entre el código y a la página web.
'''
import sys
sys.path.append('C:/Users/andre/Documents/GitHub2/Eje_Patrones_Estructurales/Pizzeria')
from flask import render_template, request,  Flask, flash
from codigoPizza import builders
from codigoPizza.guard_pedido import guardar_pedido
from codigoPizza import datos_usuario
from codigoPizza import composite
from codigoPizza import menus
from codigoPizza import datos_usuario
import secrets

#Dicccionario que contiene todos los precios de los productos
precios_dict = {'Sin bebida': 0, 'Sin postre':0, 'agua':1.5, 'sopresa':3, 'vino_blaco':2.5, 'cerveza':2.5, 'zumo':1.5, 'leche':1.5, 
           'cafe': 2, 'infusion':1, 'licor':4, 'cava':4, 'batido':2, 'smoothie':2.25, 'granizado':2, 
           'te': 3, 'fanta':6, 'coca_cola':7, 'pepsi':5, 'yogurt':3, 'helado':6, 'tarta':9, 'fruta':1, 
           'galletas':3, 'postre_del_dia':6, 'flan':2, 'tarta_de_queso':8, 'tarta_de_chocolate':5, 
           'pizza': 15, 'barbacoa': 12, 'napolitana':13, 'cuatro_quesos':16, 'margarita':10, 
           'carbonara':16, 'cuatro_estaciones':18, 'especial':20, 'vegetal':15, 'hawaiana':15,}

#Creamos la aplicación web
app = Flask(__name__)


# Genera una clave secreta hexadecimal de 16 bytes, necesaria para las alertas flash
app.secret_key = secrets.token_hex(16)  

#Establecemos las llamadas necesarias para los builders
director = builders.Director() #Chef
builder = builders.ConcreteBuilder1() #Tipo de pizza

directormenu = menus.Director() #Chef
buildermenu = menus.ConcreteBuilderMenu1() #Tipo de menu


#Rutas para las distintas páginas

@app.route('/home') #página principal
def home():
    return render_template('index.html')

@app.route('/pizzapersonalizada', methods=['GET', 'POST']) #página para la pizza personalizada
def pizzapersonalizada():
    return render_template('Pizzassueltas.html')

@app.route('/inicio_sesion', methods=['GET', 'POST']) #página para el login
def inicio_sesion():
    return render_template('login.html')

@app.route('/registro_usuario', methods=['GET', 'POST']) #página para el registro
def registro_usuario():
    return render_template('registro.html')

@app.route('/combos_general', methods=['GET', 'POST']) #página para los combos
def combos_general():
    return render_template('Combos.html')

@app.route('/combos_per', methods=['GET', 'POST']) #página para los combos personalizados
def combos_per():
    return render_template('CombosPersonalizados.html')

@app.route('/mensaje_procesado') #página para mostrar el mensaje de confirmación
def mensaje_procesado():
    mensaje = flash('success')  # Recupera el mensaje almacenado con flash
    return render_template('mensaje_procesado.html', mensaje=mensaje)




#Función para calcular el precio total del pedido

#Se encarga de conectar con el composite y calcular el precio total
def precios_funct(precios, dato):
    padre = composite.Composite()
    #Recorremos el diccionario de precios y comprobamos si el dato coincide con la clave
    for j in dato:
        for key in precios:
            if j == key:
                #Si coincide, añadimos el precio al composite
                hoja = composite.Leaf(precios[key])
                padre.add(hoja)
    #Calculamos el precio total
    precio_total = composite.client_code(padre)      
    return precio_total



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

    #Calculamos el precio total del pedido
    precio1 = precios_funct(precios_dict, [bebida, 'pizza', postre])
    
    #Contruimos la pizza
    director.builder = builder #Le decimos al chef que tipo de pizza queremos
    director.build_pizza(masa, salsa, str(ingredientes), coccion, presentacion, bebida, postre) #Le decimos al chef los pasos a seguir para dicha pizza
    builder.pizza.list_parts()
    a = builder.pizza.get_parts() #Lista con todos los datos de la pizza

    
    # Guardamos los datos del pedido en el archivo CSV asociado al ID del cliente
    guardar_pedido(id_cliente, a, 'pizza')

    # Redirige a una nueva página para mostrar el mensaje
    mensaje = f'¡Datos del pedido procesados con éxito! Precio {precio1}€'
    flash(mensaje, 'success')  # Almacena el mensaje para mostrarlo en la siguiente solicitud

    # Redirige a una nueva página para mostrar el mensaje
    return render_template('mensaje_procesado.html', mensaje=mensaje)



#Ruta para coger los datos del login  
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #recogemos los datos en las dinstintas variables
        nombre = request.form.get('username')
        contrasenia = request.form.get('password')

        # Creamos un objeto usuario con los datos del formulario
        usuario = datos_usuario.Usuario(nombre, '', '', '', contrasenia)
        
        #Comprobamos si el usuario es válido
        if usuario.usuario_valido():
            # Si el usuario es válido, redirige a la página principal
            return render_template('index.html')
        else:
            # Si el usuario no es válido, redirige a la página de inicio de sesión
            print('Usuario no valido')
            return render_template('login.html')
        
        
    

#registro ususario
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        #recogemos los datos en las dinstintas variables
        nombre = request.form.get('username')
        contrasenia = request.form.get('password')
        correo = request.form.get('email')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')

        # Creamos un objeto usuario con los datos del formulario
        usuario = datos_usuario.Usuario(nombre, direccion, telefono, correo, contrasenia)

        # Comprobamos la existencia del usuario
        if usuario.usuario_existe():
            # Si el usuario ya existe, redirige a la página de registro
            print('Usuario ya existe')
            return render_template('registro.html')
        else:
            # Si el usuario no existe, lo registra y redirige a la página principal
            usuario.registrar_usuario()
            return render_template('index.html')


@app.route('/datos_combo_per', methods=['POST']) 
def datos_combo_per():
    #generamos un id para cada pedido
    id_menu = secrets.token_hex(4)
    
    #recogemos los datos en las dinstintas variables
    nombre = 'Combo personalizado'
    bebida = request.form.get('bebida')
    pizza = request.form.get('pizza')
    postre = request.form.get('postre')
    
    #Calculamos el precio total del pedido
    precio1 = precios_funct(precios_dict, [bebida, pizza, postre])
    
    #Contruimos el combo
    directormenu.builder = buildermenu
    directormenu.build_menu(nombre, bebida, postre, pizza, precio1)
    buildermenu.menu.list_parts()
    a = buildermenu.menu.get_parts()
    
    # Guardamos los datos del pedido en el archivo CSV asociado al ID del cliente
    guardar_pedido(id_menu, a, 'combo')
    
    #Mensaje de confirmación
    mensaje = f'¡Datos del pedido procesados con éxito! Precio {precio1}€'
    flash(mensaje, 'success')  # Almacena el mensaje para mostrarlo en la siguiente solicitud

    # Redirige a una nueva página para mostrar el mensaje
    return render_template('mensaje_procesado.html', mensaje=mensaje)


@app.route('/datos_combo', methods=['POST'])
def datos_combo():
    if request.method == 'POST':
        #generamos un id para cada pedido
        id_menu = secrets.token_hex(4)
        
        #recogemos el nombre del combo seleccionado
        combo = request.form.get('combo')

        #Comprobamos el combo seleccionado y asignamos los valores correspondientes
        if combo == 'Combo 1':
            nombre = 'Combo 1'
            bebida = 'pepsi'
            pizza = 'barbacoa'
            postre= 'helado'
            
        if combo == 'Combo 2':
            
            nombre = 'Combo 2'
            bebida = 'coca_cola'
            pizza = 'napolitana'
            postre= 'fruta'
            
        if combo == 'Combo 3':
            nombre = 'Combo 3'
            bebida = 'fanta'
            pizza = 'cuatro_quesos'
            postre= 'flan'
        
        #Calculamos el precio total del pedido
        precio1 = precios_funct(precios_dict, [bebida, pizza, postre])
        
        #Contruimos el combo
        directormenu.builder = buildermenu
        directormenu.build_menu(nombre, bebida, postre, pizza, precio1)
        buildermenu.menu.list_parts()
        a = buildermenu.menu.get_parts()
        
        # Guardamos los datos del pedido en el archivo CSV asociado al ID del cliente
        guardar_pedido(id_menu, a, 'combo')
        
        #Mensaje de confirmación
        mensaje = f'¡Datos del pedido procesados con éxito! Precio {precio1}€'
        flash(mensaje, 'success')  # Almacena el mensaje para mostrarlo en la siguiente solicitud

        # Redirige a una nueva página para mostrar el mensaje
        return render_template('mensaje_procesado.html', mensaje=mensaje)
        
        
