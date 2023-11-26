from abc import ABC, abstractmethod
from datetime import datetime
from composite import CompositeCarpeta

class Subject(ABC):
    """
    Interfaz que declara operaciones comunes para el RealSubject y el Proxy.
    """

    @abstractmethod
    def acceso_documentos(self, nombre_documento) -> None:
        pass
    
    @abstractmethod
    def acceso_carpetas(self, nombre_carpetas) -> None:
        pass

    @abstractmethod
    def acceso_enlaces(self, nombre_enlace) -> None:
        pass
    
    
class RealSubject(Subject):
    """
    Clase real que contiene la información que se quiere proteger.
    """
    def __init__(self, composite_carpeta:CompositeCarpeta):
        #le damos acceso a la carpeta principal
        self._composite_carpeta = composite_carpeta
    
    def acceso_documentos(self, documento):
        #accede al docmumento, lo muestra y pregunta si se quiere modificar
        print(f"Accediendo al documento {documento.nombre}.")
        documento.mostrar()
        respuesta = input("¿Desea modificar el documento? (s/n): ")
        if respuesta == "s":
            documento.fecha_modificacion = datetime.now()
            print(f"El documento {documento.nombre} ha sido modificado.")
            documento.mostrar()
        else:
            print(f"El documento {documento.nombre} no ha sido modificado.")
            documento.mostrar()
        
    def acceso_enlaces(self, nombre_enlace):
        #busca el enlace
        enlace = self._composite_carpeta.buscar_contenido(nombre_enlace)
        if enlace:#existe en nombre del enlace
            print(f"Accediendo al enlace {nombre_enlace}.")
            enlace.mostrar() #muestra la información del enlace
        else:#no existe el nombre del enlace
            print(f"El enlace {nombre_enlace} no existe.")
    
    def acceso_carpetas(self, nombre_carpetas):
        #busca la carpeta
        carpeta = self._composite_carpeta.buscar_contenido(nombre_carpetas)
        if carpeta: #existe el nombre de la carpeta
            print(f"Accediendo a la carpeta {nombre_carpetas}.")
            carpeta.mostrar() #muestra la información de la carpeta
        else: #no existe el nombre de la carpeta
            print(f"La carpeta {nombre_carpetas} no existe.")

class Proxy(Subject):
    """
    Controla el acceso a la clase RealSubject. Puede ser responsable de crear y
    eliminarlo.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject
        self._usuario = 'admin' # Usuario de acceso a documentos sensibles
        self._contrasenia = "1234"  # Contraseña de acceso a documentos sensibles
        self._entrada_log = []  # Lista de registros de acceso.

    def acceso_documentos(self, nombre_documento, usuario):
        #buscamos el documento
        documento = self._real_subject._composite_carpeta.buscar_contenido(nombre_documento)
        if documento: #existe el nombre del documento
            #mira si es sensible
            es_sensible = documento.sensible
            if self.check_access(es_sensible, usuario): #chequea si se puede acceder o no
                #accede al documento
                self._real_subject.acceso_documentos(documento)
                self.log_access(nombre_documento, usuario) #registra el acceso
                
        else: #no existe el nombre del documento
            print(f"El documento {nombre_documento} no existe.")
            
    def acceso_carpetas(self, nombre_carpetas, usuario) -> None:
        #permite acceder a la carpeta
        self._real_subject.acceso_carpetas(nombre_carpetas)
        self.log_access(nombre_carpetas, usuario) #registra el acceso

    def acceso_enlaces(self, nombre_enlace, usuario) -> None:
        #permite acceder al enlace
        self._real_subject.acceso_enlaces(nombre_enlace)
        self.log_access(nombre_enlace, usuario) #registra el acceso

    def check_access(self, es_sensible: bool, usuario) -> bool:
        #comprueba se es sensible
        if es_sensible:
            # Si es sensible, pide contraseña
            contrasenia = input("Introduzca la contraseña: ")
            if contrasenia == self._contrasenia and usuario == self._usuario:
                print("Proxy: Acceso concedido.")
                return True
            else:
                print("Proxy: Acceso denegado.")
                return False
        else: # Si no es sensible, no se necesita contraseña.
            print("Proxy: Acceso concedido.")
            return True

    def log_access(self, nombre_dato, usuario):
        # Registramos el acceso en la lista de registros de acceso
        tiempo = datetime.now()
        entrada = f"Acceso a la información de {nombre_dato} a las {tiempo} el usuario {usuario}."
        self._entrada_log.append(entrada)
        print(entrada)


def client_code(subject: Subject, tipo_acceso, nombre) -> None:
    #pide el usuario y manda al lugar correspondiente dependiendo del tipo de acceso
    usuario = input("Introduzca el usuario: ")
    if tipo_acceso == "carpeta":
        subject.acceso_carpetas(nombre, usuario)
    elif tipo_acceso == "documento":
        subject.acceso_documentos(nombre, usuario)
    elif tipo_acceso == "enlace":
        subject.acceso_enlaces(nombre, usuario)

