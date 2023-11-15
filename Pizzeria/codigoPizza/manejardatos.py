from . import usuarios
import csv

class WebPizzeria:
    '''
    la clase encargada del registro y login de los usuarios a la página. 
    Donde llama a la clase usuario para guardar los datos de los usuarios y de las pizzas.
    '''
    def __init__(self):
        self.usuario = {}
        self.cargando_datos()

    def guardar_datos(self):
        with open('pizza_data.csv', mode='w', newline='') as file:
            escribir = csv.writer(file)
            for usuario in self.usuario.values(): #Recorremos el diccionario de usuarios
                for orden in usuario.ordenes: #Recorremos la lista de pizzas
                    escribir.writerow([usuario.nombre, usuario.contrasenia, orden])

    def cargando_datos(self):
        try:
            with open('pizza_data.csv', mode='r') as file:
                leer = csv.reader(file)
                for fila in leer:
                    #Añadimos al diccionario usuario el nombre (ya está registrado)
                    nombre, contrasenia, pedido = fila
                    if nombre not in self.usuario: #Si el nombre del usuario no está en el diccionario
                        self.usuario[nombre] = usuarios.Usuario(nombre, contrasenia)#añadimos el usuario al diccionario
                    usuario = self.usuario[nombre] #Asociamos a la vaiable usuario el nombre del usuario
                    usuario.pedido_actual(pedido) #Vamos añadiendo las pizzas que tiene el usuario asociadas
        except FileNotFoundError:
            pass
        
    def registrar_usuario(self, nombre, contrasenia):
        if nombre not in self.usuario: #Si el nombre del usuario no está en el diccionario (no está registrado)
            self.usuario[nombre] = usuarios.Usuario(nombre, contrasenia) #añadimos el usuario al diccionario

    def login(self, nombre, contrasenia):
        #Comprobamos que el nombre y la contraseña coinciden con los datos guardados y 
        #devolvemos el nombre del usuario
        if nombre in self.usuario and self.usuario[nombre].contrasenia == contrasenia: 
            return self.usuario[nombre]
        else:
            return None

    def usuario_registrado(self, nombre):
        return nombre in self.usuario


