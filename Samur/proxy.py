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
        self._composite_carpeta = composite_carpeta
    
    def acceso_documentos(self, nombre_documento):
        documento= self._composite_carpeta.buscar(nombre_documento)
    
        #Revisar los if pq el buscar devuelve el elemento o none
        if documento:
            print(f"Accediendo al documento {nombre_documento}.")
            print(f"Documento: {documento.nombre}")
            print(f"Tipo: {documento.tipo}")
            print(f"Tamaño: {documento.tamanio}")
            print(f"Sensible: {documento.sensible}")
            print(f"Fecha de creación: {documento.fecha_creacion}")
            print(f"Fecha de modificación: {documento.fecha_modificacion}")
        else:
            print(f"El documento {nombre_documento} no existe.")
    
    def acceso_enlaces(self, nombre_enlace):
        enlace = self._composite_carpeta.buscar(nombre_enlace)
        if enlace:
            print(f"Accediendo al enlace {nombre_enlace}.")
            print(f"Enlace: {enlace.nombre}")
            print(f"Destino: {enlace.destino}")
        else:
            print(f"El enlace {nombre_enlace} no existe.")
    
    def acceso_carpetas(self, nombre_carpetas):
        carpeta = self._composite_carpeta.buscar(nombre_carpetas)
        if carpeta:
            print(f"Accediendo a la carpeta {nombre_carpetas}.")
            print(f"Carpeta: {carpeta.nombre}")
            print(f"Tamaño total: {carpeta.tamanio_total()}")
        else:
            print(f"La carpeta {nombre_carpetas} no existe.")

class Proxy(Subject):
    """
    Controla el acceso a la clase RealSubject. Puede ser responsable de crear y
    eliminarlo.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject
        self._contrasenia = "1234"  # Contraseña de acceso.
        self._entrada_log = []  # Lista de registros de acceso.

    def acceso_documentos(self, nombre_documento) -> None:
        if self.check_access():
            self._real_subject.acceso_documentos(nombre_documento)
            self.log_access()

    def acceso_carpetas(self, nombre_carpetas) -> None:
        if self.check_access():
            self._real_subject.acceso_carpetas(nombre_carpetas)
            self.log_access()

    def acceso_enlaces(self, nombre_enlace) -> None:
        if self.check_access():
            self._real_subject.acceso_enlaces(nombre_enlace)
            self.log_access()

    def check_access(self) -> bool:
        contrasenia = input("Introduzca la contraseña: ")
        if contrasenia == self._contrasenia:
            print("Proxy: Acceso concedido.")
            return True
        else:
            print("Proxy: Acceso denegado.")
            return False

    def log_access(self) -> None:
        # Registramos el acceso en la lista de registros de acceso
        tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entrada = f"Acceso a la información a las {tiempo}"
        self._entrada_log.append(entrada)
        print(entrada)


def client_code(subject: Subject, tipo_acceso, nombre) -> None:
    if tipo_acceso == "carpeta":
        subject.acceso_carpetas(nombre)
    elif tipo_acceso == "documento":
        subject.acceso_documentos(nombre)
    elif tipo_acceso == "enlace":
        subject.acceso_enlaces(nombre)


if __name__ == "__main__":
    print("Client: Ejecutando el código del cliente con un documento real:")
    documento_real = RealSubject()
    documento_real.acceso_documentos("Documento Confidencial")
    client_code(documento_real, tipo_acceso="documento", nombre="Documento Confidencial")

    print("")

    print("Client: Ejecutando el mismo código del cliente con un proxy:")
    proxy = Proxy(documento_real)
    client_code(proxy, tipo_acceso="carpeta", nombre="Carpeta Confidencial")

    # Imprimir registros de acceso
    print("\nRegistros de acceso:")
    for log in proxy._entrada_log:
        print(log)
