from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any #tipado dinámigo 


class Builder(ABC):
    """
    Es una clase abstracta que contiene la estructura básica de una pizza. 
    Teniendo el propio producto (la pizza) y los métodos para construir las distintas 
    partes de la pizza, como la masa, la salsa, la presentación etc.
    """

    @property #nos genera los getter y setter de los de abajo
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def tipo_masa(self) -> None:
        pass
    
    @abstractmethod
    def salsa_base(self) -> None:
        pass
    
    @abstractmethod
    def ingr_principales(self) -> None: #ingredientes principales
        pass
    
    @abstractmethod
    def tec_coccion(self) -> None: #técnica de cocción
        pass
    
    @abstractmethod
    def presentacion(self) -> None:
        pass
    
    @abstractmethod
    def maridajes(self)-> None: #maridajes recomendados
        pass
    
    @abstractmethod
    def extras(self) -> None:
        pass
    
class ConcreteBuilder1(Builder): #Es un tipo de pizza, donde personaliza los métodos de la clase Builder
    '''
    Le preguntamos al cliente que tipo de pizza quiere y vamos construyendo la pizza según los 
    métodos que nos pida. 
    Más adelante debemos de dale sugerencias en base a su historial, etc. 
    '''

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Product1() #pizza final

    @property
    def pizza(self) -> Product1:
        pizza = self._pizza
        #self.reset()
        return pizza

    def tipo_masa(self, masa) -> None:
        self._pizza.add(masa)
    
    def salsa_base(self, salsa) -> None:
        self._pizza.add(salsa)
    
    def ingr_principales(self, ingrediente) -> None:
        self._pizza.add(ingrediente)
    
    def tec_coccion(self, coccion) -> None:
        self._pizza.add(coccion)
    
    def presentacion(self, presentacion) -> None:
        self._pizza.add(presentacion)
    
    def maridajes(self, maridaje) -> None:
        self._pizza.add(maridaje)
        
    
    def extras(self, extra) -> None:
        self._pizza.add(extra)
        
    


class Product1(): #Pizza agrupada
    '''
    Unimos cada parte de la pizza y lo almacenamos en una lista.
    '''

    def __init__(self) -> None:
        self.parts = []
        
    def get_parts(self) -> list:
        return self.parts

    def add(self, part: Any) :
        self.parts.append(part)

    def list_parts(self):
        print(f"Partes de la pizza: {', '.join(self.parts)}", end="")

class Director: #Chef
    '''
    Nos prepara todo para poder contruir la pizza según los ingredientes del cliente y 
    también marcamos el orden de los pasos a seguir.
    '''

    def __init__(self) -> None:
        self._builder = None 

    @property
    def builder(self) -> Builder: #getter del builder
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None: #setter del builder
        self._builder = builder

    #Construimos el producto según el tipo de pizza que queramos
    def build_pizza(self, masa, salsa, ingrediente, coccion, presentacion, maridaje, extra) -> None:
        self.builder.tipo_masa(masa)
        self.builder.salsa_base(salsa)
        self.builder.ingr_principales(ingrediente)
        self.builder.tec_coccion(coccion)
        self.builder.presentacion(presentacion)
        self.builder.maridajes(maridaje)
        self.builder.extras(extra)
        