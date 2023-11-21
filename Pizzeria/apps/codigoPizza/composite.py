

from abc import ABC, abstractmethod

class Component(ABC):
    '''
    Clase abstracta encargada de calcular el preco de los combos
    '''
    @abstractmethod
    def obtener_precio(self):
        pass

class Leaf(Component):
    '''
    Al ser un elemento inidividual se le considera una hoja, 
    no tiene hijos
    '''
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

class Composite(Component):
    '''
    Es el elemento compuesto, que contiene los elementos individuales
    y compuestos
    '''
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def obtener_precio(self):
        return sum(elemento.obtener_precio() for elemento in self.elementos)
