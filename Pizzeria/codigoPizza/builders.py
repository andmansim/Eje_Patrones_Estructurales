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

    def tipo_masa(self) -> None:
        masa = input("¿Qué tipo de masa quieres? (Por ejemplo: fina, normal, gruesa): ")
        self._pizza.add(masa)
    
    def salsa_base(self) -> None:
        salsa = input("¿Qué salsa quieres? (Por ejemplo: tomate, barbacoa, carbonara): ")
        self._pizza.add(salsa)
    
    def ingr_principales(self) -> None:
        while True:
            ingrediente = input("¿Qué ingrediente quieres? (Si no quieres ninguno pulsa 0 para salir): ")
            if ingrediente == "0":
                break
            else:
                self._pizza.add(ingrediente)
    
    def tec_coccion(self) -> None:
        coccion = input("¿Qué técnica de cocción quieres? (Por ejemplo: horno de leña, horno eléctrico, horno de gas): ")
        self._pizza.add(coccion)
    
    def presentacion(self) -> None:
        presentacion = input("¿Cómo quieres que se presente? (Por ejemplo: en caja de cartón, en plato de barro): ")
        self._pizza.add(presentacion)
    
    def maridajes(self) -> None:
        while True:
            maridaje = input("¿Qué maridaje quieres? (Por ejemplo: vino tinto, cerveza, etc.)(Si no quieres ninguno pulsa 0 para salir): ")
            if maridaje == "0":
                break
            else:
                self._pizza.add(maridaje)
        
    
    def extras(self) -> None:
        while True:
            extra = input("¿Qué extra quieres? (Por ejemplo: bordes especiales, ingrediente extra, etc.)(Si no quieres ninguno pulsa 0 para salir): ")
            if extra == "0":
                break
            else:
                self._pizza.add(extra)
        
    


class Product1(): #Pizza agrupada
    '''
    Unimos cada parte de la pizza y lo almacenamos en una lista.
    '''

    def __init__(self) -> None:
        self.parts = []
        
    def get_parts(self) -> list:
        return self.parts

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
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
    def build_pizza(self) -> None:
        self.builder.tipo_masa()
        self.builder.salsa_base()
        self.builder.ingr_principales()
        self.builder.tec_coccion()
        self.builder.presentacion()
        self.builder.maridajes()
        self.builder.extras()
        