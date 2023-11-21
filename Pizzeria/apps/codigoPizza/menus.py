from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any #tipado dinámigo 


class BuilderMenu(ABC):
    """
    Definimos la interfaz abstracta de los menus o combos.
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
    
    
class ConcreteBuilderMenu1(BuilderMenu): 
    '''
    Aquí vamos a construir el menu o combo según los métodos que nos pida.
    Este será el personalizado y el genérico, dado que su estructura base es la misma.
    '''

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._menu = ProductMenu1()

    @property
    def menu(self) -> ProductMenu1:
        menu = self._menu
        return menu
    
    def id_menu(self, id):
        self._menu.add(id)
        
    def nombre_menu(self, nombre):
        self._menu.add(nombre)
    
    def precio_menu(self, precio):
        # es el precio total de todos los productos
        self._menu.add(precio)
    
    def bebida_menu(self, bebida):
        self._menu.add(bebida)
    
    def postre_menu(self, postre):
        self._menu.add(postre)
    
    def pizza_menu(self, pizza):
        self._menu.add(pizza)
    
    
class ProductMenu1():
    '''
    Se encarga de juntarlo todo
    '''

    def __init__(self) -> None:
        self.parts = []
        
    def get_parts(self) -> list:
        return self.parts

    def add(self, part: Any) :
        self.parts.append(part)

    def list_parts(self):
        print(f"Partes del menu: {', '.join(map(str, filter(None, self.parts)))}", end="")

class Director:
    '''
    Nos contruye el menu
    '''

    def __init__(self) -> None:
        self._buildermenu = None 

    @property
    def buildermenu(self) -> BuilderMenu: #getter del builder
        return self._buildermenu

    @buildermenu.setter
    def builder(self, buildermenu: BuilderMenu) -> None: #setter del builder
        self._buildermenu = buildermenu

    #Construimos el producto según el tipo de pizza que queramos
    def build_menu(self, id, nombre, bebida, postre, pizza, precio) -> None:
        self.buildermenu.id_menu(id)
        self.buildermenu.nombre_menu(nombre)
        self.buildermenu.bebida_menu(bebida)
        self.buildermenu.postre_menu(postre)
        self.buildermenu.pizza_menu(pizza)
        self.buildermenu.precio_menu(precio)    

