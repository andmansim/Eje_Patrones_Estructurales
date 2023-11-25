
import datetime

class Documentos:
    def __init__(self, nombre, tipo, tamanio, sensible ):
        self.nombre = nombre
        self.tipo = tipo
        self.tamnio = tamanio
        self.sensible = sensible
        self.fecha_creacion = datetime.datetime.now()
        self.fecha_modificacion = None
        self.acceso_registro = []
        
    def acceso(self, usuario):  
        #añadimos el usuario que ha entrado al documento
        self.acceso_registro.append(usuario)
        if self.sensible:
            #actualizamos la fecha de modificacion
            self.fecha_modificacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Enlaces: #Son referencias a otros documentos o carpetas
    def __init__(self, nombre, url, tamanio ):
        self.nombre = nombre
        self.url = url
        self.tamnio = tamanio #es simbólico, no corresponde con el tamaño real del enlace

class Carpetas:
    def __init__(self, nombre ):
        self.nombre = nombre
        self.contenido = [] #lista de documentos, carpetas y enlaces que contiene la carpeta
        
    def tamanio_total(self):
        #Calculamos el tamaño total de la carpeta
        tamanio = 0
        for elemento in self.contenido:
            tamanio += elemento.tamanio
        return tamanio  
    
    def añadir_contenido(self, contenido):
        self.contenido.append(contenido)
        
    def eliminar_contenido(self, contenido):
        self.contenido.remove(contenido)
        
    def mostrar_contenido(self):
        print(f"La carpeta {self.nombre} contiene:")
        for elemento in self.contenido:
            print(elemento.nombre)
            
    def buscar_contenido(self, nombre):
        for elemento in self.contenido:
            if elemento.nombre == nombre:
                return elemento
        return None
