from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any #tipado dinámigo 

from abc import ABC, abstractmethod

class Producto(ABC):
    '''
    Encargado de definir la estructura común de los productos
    '''
    @abstractmethod
    def obtener_precio(self):
        pass

class ElementoMenu(Producto):
    '''
    Son los elementos inidviduales que puede elegir el cliente, es decir, 
    la bebida o postre que quiera personalizar al pedir su combo personalizado
    '''
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

class Pizza(ElementoMenu):
    '''
    Subclase de ElementoMenu, donde se define la pizza, aunque 
    no se si ponerla como las distintas que hay o crearla sin más
    '''
    def __init__(self, nombre, ingredientes, precio):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes

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

    def obtener_precio(self):
        return sum(elemento.obtener_precio() for elemento in self.elementos)

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
        pizza_margarita = Pizza("Margarita", ["tomate", "queso", "albahaca"], 12.0)
        bebida = ElementoMenu("Bebida Genérica", 3.0)
        postre = ElementoMenu("Postre Genérico", 4.0)

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

# Ejemplo de uso:
restaurante = RestauranteDirector(MenuGeneridoBuilder())
restaurante.construir_menu()
menu_generico = restaurante.obtener_menu()

restaurante = RestauranteDirector(MenuPersonalizableBuilder())
pizza_personalizable = Pizza("Personalizada", ["tomate", "queso"], 15.0)
bebida_personalizable = ElementoMenu("Bebida Personalizable", 4.0)
postre_personalizable = ElementoMenu("Postre Personalizable", 5.0)
restaurante.builder.construir_menu(pizza_personalizable, bebida_personalizable, postre_personalizable)
menu_personalizable = restaurante.obtener_menu()

# Agregar menús al menú principal
restaurante.menu_principal = MenuCompuesto("MP", "Menú Principal")
restaurante.menu_principal.agregar_elemento(menu_generico)
restaurante.menu_principal.agregar_elemento(menu_personalizable)

# Calcular el precio de un menú por su código
codigo_menu_buscar = "MP"
precio_menu = restaurante.menu_principal.obtener_precio()

if precio_menu is not None:
    print(f"El precio del menú {codigo_menu_buscar} es: ${precio_menu}")
else:
    print(f"No se encontró el menú con el código {codigo_menu_buscar}")
