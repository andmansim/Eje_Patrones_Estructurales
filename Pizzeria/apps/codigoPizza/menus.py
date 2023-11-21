from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any #tipado dinámigo 
from composite import Component, Leaf, Composite
from abc import ABC, abstractmethod

class Producto(ABC):
    '''
    Encargado de definir la estructura común de los productos
    '''
    @abstractmethod
    def construir(self):
        pass

class ElementoMenu(Producto):
    '''
    Son los elementos inidviduales que puede elegir el cliente, es decir, 
    la bebida o postre que quiera personalizar al pedir su combo personalizado
    '''
    def __init__(self, nombre):
        self.nombre = nombre

    def construir(self):
        return Composite(self.nombre)

class Pizza(ElementoMenu):
    '''
    Subclase de ElementoMenu, donde se define la pizza, aunque 
    no se si ponerla como las distintas que hay o crearla sin más
    '''
    def __init__(self, nombre, ingredientes):
        super().__init__(nombre)
        self.ingredientes = ingredientes
    def construir(self):
        return Composite(self.nombre)

class MenuCompuesto(Producto):
    '''
    Son los combos ya creados, donde se selecciona el pack. 
    '''
    def __init__(self, codigo, nombre):
        self.codigo = codigo #identificador del menú
        self.nombre = nombre
        self.elementos = [] #contendrá las pizzas, bebidas y postres

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def construir(self):
        menu = Composite(self.codigo, self.nombre)
        for elemento in self.elementos:
            menu.agregar_elemento(elemento.construir())
        return menu
class Builder(ABC): 
    '''
    Clase abstracta builder que se encarga de construir y obtener el menú
    '''
    @abstractmethod
    def construir_menu(self):
        pass

    @abstractmethod
    def obtener_menu(self):
        pass

class MenuGenericoBuilder(Builder):
    '''
    El el concrete builder 1, donde define el menú genérico
    '''
    def __init__(self):
        self.menu = MenuCompuesto("MG", "Menú Genérico")

    def construir_menu(self):
        pizza_margarita = Pizza("Margarita", ["tomate", "queso", "albahaca"])
        bebida = ElementoMenu("Bebida Genérica")
        postre = ElementoMenu("Postre Genérico")

        self.menu.agregar_elemento(pizza_margarita)
        self.menu.agregar_elemento(bebida)
        self.menu.agregar_elemento(postre)

    def obtener_menu(self):
        return self.menu

class MenuPersonalizableBuilder(Builder):
    '''
    Concretebuilder2, define el menú personalizable
    '''
    def __init__(self):
        self.menu = MenuCompuesto("MP", "Menú Personalizable")

    def construir_menu(self, pizza, bebida, postre):
        self.menu.agregar_elemento(pizza)
        self.menu.agregar_elemento(bebida)
        self.menu.agregar_elemento(postre)

    def obtener_menu(self):
        return self.menu

class RestauranteDirector:
    '''
    Es el director, que se encarga de construir el menú
    '''

    def __init__(self, builder):
        self.builder = builder

    def construir_menu(self):
        self.builder.construir_menu()

    def obtener_menu(self):
        return self.builder.obtener_menu()

