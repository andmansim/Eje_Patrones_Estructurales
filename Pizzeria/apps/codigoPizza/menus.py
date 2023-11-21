from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any #tipado dinámigo 


class Builder(ABC):
    """
    
    """

    @property #nos genera los getter y setter de los de abajo
    @abstractmethod
    def menu(self) -> None:
        pass

    @abstractmethod
    def id_menu(self) -> None:
        pass
    
    @abstractmethod
    def nombre_menu(self) -> None:
        pass
    
    @abstractmethod
    def precio_menu(self) -> None:
        pass
    
    @abstractmethod
    def bebida_menu(self) -> None:
        pass   
    
    @abstractmethod
    def postre_menu(self) -> None:
        pass
    
    @abstractmethod
    def pizza_menu(self) -> None:
        pass
    
    
class ConcreteBuilder1(Builder): 
    '''
    Menu general, el a creado
    '''

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._menu = Product1()

    @property
    def menu(self) -> Product1:
        menu = self._menu
        return menu
    
    def id_menu(self, id):
        self._menu.add(id)
        
    def nombre_menu(self, nombre):
        self._menu.add(nombre)
    
    def precio_menu(self, precio):
        self._menu.add(precio)
    
    def bebida_menu(self, bebida):
        self._menu.add(bebida)
    
    def postre_menu(self, postre):
        self._menu.add(postre)
    
    def pizza_menu(self, pizza):
        self._menu.add(pizza)
    
    
class Product1(): #Pizza agrupada
    '''
    
    '''

    def __init__(self) -> None:
        self.parts = []
        
    def get_parts(self) -> list:
        return self.parts

    def add(self, part: Any) :
        self.parts.append(part)

    def list_parts(self):
        print(f"Partes del menu: {', '.join(map(str, filter(None, self.parts)))}", end="")

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
    def build_menu(self, id, nombre, bebida, postre, pizza, precio) -> None:
        self.builder.id_menu(id)
        self.builder.nombre_menu(nombre)
        self.builder.bebida_menu(bebida)
        self.builder.postre_menu(postre)
        self.builder.pizza_menu(pizza)
        self.builder.precio_menu(precio)    

