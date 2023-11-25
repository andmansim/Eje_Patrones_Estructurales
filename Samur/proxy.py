from abc import ABC, abstractmethod
from datetime import datetime

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

    def acceso_documentos(self, nombre_documento):
        print(f"Accediendo al documento {nombre_documento}.")
    
    def acceso_enlaces(self, nombre_enlace):
        print(f"Accediendo al enlace {nombre_enlace}.")
    
    def acceso_carpetas(self, nombre_carpetas):
        print(f"Accediendo a la carpeta {nombre_carpetas}.")


class Proxy(Subject):
    """
    Controla el acceso a la clase RealSubject. Puede ser responsable de crear y
    eliminarlo.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject
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
        print("Proxy: Comprobando el acceso antes de disparar un request.")
        return True

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
