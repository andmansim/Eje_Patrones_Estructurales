from . import builders

def menu(web_pizza):
    
    nombre = input("Por favor introduzca su nombre de usuario (0 para salir): ")

    if nombre == "0":
        controlador = False

    if web_pizza.usuario_registrado(nombre):
        '''
        Si el usuario ya está registrado, le pedimos la contraseña para que inicie sesión. 
        Si la contraseña es correcta, le damos la bienvenida y le mostramos su último pedido.
        '''
        contrasenia = input("Introduce contraseña: ")
        usuario = web_pizza.login(nombre, contrasenia)
        if usuario: #Si coincide el nombre y la contraseña (login correcto)
            ultimo_pedido = usuario.ultimo_pedido()
            if ultimo_pedido: #Si hay algún pedido registrado
                print(f"Tu último pedido fue: {ultimo_pedido}")
                pedir = input("Quieres pedir lo mismo? (Si/No) ")
                if pedir == "Si":
                    usuario.pedido_actual(ultimo_pedido)
                    print('El pedido se ha realizado con éxito')
                    return False, usuario
        
            else: #No hay ningún pedido registrado
                print("Aún no tienes ningún pedido registrado")
        else:
            print('\nNombre de usuario o contraseña incorrectos.')
            menu(web_pizza)
    else:
        '''
        El usuario no está registrado, por lo que le pedimos que cree una contraseña.
        Registramos al usuario y le damos la bienvenida.
        '''
        contrasenia = input("Crea una contraseña: ")
        web_pizza.registrar_usuario(nombre, contrasenia)
        usuario = web_pizza.login(nombre, contrasenia) #Abrir sesión
        print("Bienvenido!") 
    return True, usuario

def crear_pizza(usuario, numero):
    director = builders.Director() #Chef
    builder = builders.ConcreteBuilder1() #Tipo de pizza
    director.builder = builder #Le decimos al chef que tipo de pizza queremos
    
    print(f"Pizza {numero} : ")
    director.build_pizza_prueba1() #Le decimos al chef los pasos a seguir para dicha pizza
    builder.pizza.list_parts() #Unimos todo
    a = builder.pizza.get_parts() #Lista con todos los datos de la pizza
    usuario.pedido_actual(a)
    builder.reset() #Reseteamos el builder para que no se acumulen los datos
