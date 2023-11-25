from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import datetime

class Component(ABC):
    '''
    Declaramos la interfaz de los objetos tanto hoja como compuesto. 
    Contiene los métodos que se aplican a los objetos hoja y compuesto, en este 
    caso es mostrar el documento
    '''
    @abstractmethod
    def mostrar(self) -> float:
        pass


class Leaf(Component): #Documentos
    '''
    lo más simple del árbol son las hojas, que no tienen hijos. En nuestro código
    esto son los documentos. 
    '''
    def __init__(self, nombre, tipo, tamanio, sensible) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.tamnio = tamanio
        self.sensible = sensible
        self.fecha_creacion = datetime.datetime.now()
        self.fecha_modificacion = None


    def mostrar(self) -> None:
        print(f"Documento: {self._nombre}")
        print(f"Tipo: {self._tipo}")
        print(f"Tamaño: {self._tamanio}")
        print(f"Sensible: {self._sensible}")
        print(f"Fecha de creación: {self._fecha_creacion}")
        print(f"Fecha de modificación: {self._fecha_modificacion}")
        

class CompositeCarpeta(Component): #Carpetas
    '''
    Nos permite acceder a los hijos de los compuestos y definir las operaciones. 
    Aquí van a ser las carpetas
    '''
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        self._hijo: List[Component] = []

    def add(self, component: Component) -> None:
        self._hijo.append(component)

    def remove(self, component: Component) -> None:
        self._hijo.remove(component)

    def tamanio_total(self):
        #Calculamos el tamaño total de la carpeta
        tamanio = 0
        for elemento in self.contenido:
            tamanio += elemento.tamanio
        return tamanio 
    
    def buscar_contenido(self, nombre):
        for elemento in self.contenido:
            if elemento.nombre == nombre:
                return elemento
        return None
    def mostrar(self) -> None:
        print(f'Carpeta: {self._nombre}')
        for component in self._hijo:
            component.mostrar()

class CompositeEnlace(Component): #Enlaces
    '''
    Nos permite acceder a los hijos de los compuestos y definir las operaciones. 
    Aquí van a ser los enlaces.
    '''
    def __init__(self, destino) -> None:
        self._destino = destino
        self._tamanio = 0
      
    def mostrar(self) -> None:
        print(f'Enlace {self._destino}')
       

def client_code(component: Component):
    print(f"RESULT: {component.mostrar()}", end="")
    
if __name__ == "__main__":
    doc1 = Leaf("Documento 1")
    doc2 = Leaf("Documento 2")
    
    carp1 = CompositeCarpeta("Carpeta 1")
    carp2 = CompositeCarpeta("Carpeta 2")
    
    carp1.add(doc1)
    carp2.add(doc2)
    
    enlace_doc1 = CompositeEnlace("Carpeta1-->Documento1")
    
    carp_principal = CompositeCarpeta("Carpeta Principal")
    carp_principal.add(carp1)
    carp_principal.add(carp2)
    carp_principal.add(enlace_doc1)
    
    print("Mostrando el contenido de la carpeta principal:")
    client_code(carp_principal)
    
    print('Agregando un nuevo documento a la carpeta 2')
    nuevo_doc = Leaf("Documento 3")
    carp2.add(nuevo_doc)
    client_code(carp_principal)
    
    



