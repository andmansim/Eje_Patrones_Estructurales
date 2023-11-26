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
        self.tamanio = tamanio
        self.sensible = sensible
        self.fecha_creacion = datetime.datetime.now()
        self.fecha_modificacion = None


    def mostrar(self) -> None:
        #muestra la información del documento
        print(f"Nombre del documento: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Tamaño: {self.tamanio}")
        print(f"Sensible: {self.sensible}")
        print(f"Fecha de creación: {self.fecha_creacion}")
        print(f"Fecha de modificación: {self.fecha_modificacion}")
        

class CompositeCarpeta(Component): #Carpetas
    '''
    Nos permite acceder a los hijos de los compuestos y definir las operaciones. 
    Aquí van a ser las carpetas
    '''
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self._hijo: List[Component] = []

    def add(self, component: Component) -> None:
        self._hijo.append(component)

    def remove(self, component: Component) -> None:
        self._hijo.remove(component)

    def tamanio_total(self):
        #Calculamos el tamaño total de la carpeta
        tamanio = 0
        for elemento in self._hijo:
            tamanio += elemento.tamanio
        return tamanio 
    
    def buscar_contenido(self, nombre):
        #buscamos elementos dentro de la carpeta
        for elemento in self._hijo:
            if elemento.nombre == nombre:
                return elemento
            elif isinstance(elemento, CompositeCarpeta):
                # Si el elemento es otra carpeta, realiza la búsqueda dentro de ella recursivamente
                resultado = elemento.buscar_contenido(nombre)
                if resultado:
                    return resultado
        return None
    
    def mostrar(self):
        #muestra la información de la carpeta
        print(f'Carpeta: {self.nombre}')
        print(f'Tamaño total: {self.tamanio_total()}')
        for componente in self._hijo:
            componente.nombre

class CompositeEnlace(Component): #Enlaces
    '''
    Nos permite acceder a los hijos de los compuestos y definir las operaciones. 
    Aquí van a ser los enlaces.
    '''
    def __init__(self, nombre, destino) -> None:
        self.nombre = nombre
        self.destino = destino
      
    def mostrar(self):
        print(f'Nombre enlace: {self.nombre}')
        print(f'Enlace: {self.destino}')
       

