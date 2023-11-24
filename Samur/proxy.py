from abc import ABC, abstractmethod
import datetime

class Subject(ABC):
    """
    Interfaz que declara operaciones comunes para el RealSubject y el Proxy.
    """

    @abstractmethod
    def acceso_documentos(self) -> None:
        pass
    
    @abstractmethod
    def acceso_carpetas(self) -> None:
        pass

    @abstractmethod
    def acceso_enlaces(self) -> None:
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
        self._entrada_log = [] # Lista de registros de acceso.

    def acceso_documentos(self) -> None:
        if self.check_access():
            self._real_subject.acceso_documentos()
            self.log_access()
    
    def acceso_carpetas(self) -> None:
        if self.check_access():
            self._real_subject.acceso_carpetas()
            self.log_access()
    
    def acceso_enlaces(self) -> None:
        if self.check_access():
            self._real_subject.acceso_enlaces()
            self.log_access()
            
    def check_access(self) -> bool:
        print("Proxy: Comprobando el acceso antes de disparar un request.")
        return True

    def log_access(self) -> None:
        #Registramos el acceso en la lista de registros de acceso
        tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entrada = f"Acceso a la información a las {tiempo}"
        self._entrada_log.append(entrada)
        print(entrada)


def client_code(subject: Subject) -> None:
    subject.acceso_carpetas()
    subject.acceso_documentos()
    subject.acceso_enlaces()




if __name__ == "__main__":
    
    print("Client: Ejecutando el código del cliente con un documento real:")
    documento_real = RealSubject.acceso_documentos("Documento Confidencial")
    client_code(documento_real)

    print("")

    print("Client: Ejecutando el mismo código del cliente con un proxy:")
    proxy = Proxy(documento_real, password="contrasena_segura")
    client_code(proxy)

    # Imprimir registros de acceso
    print("\nRegistros de acceso:")
    for log in proxy._access_logs:
        print(log)