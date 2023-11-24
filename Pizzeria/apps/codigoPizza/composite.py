from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    '''
    Definimos la interfaz de los objetos que formarán la estructura de árbol.
    En otras palabras, el método para coger el precio de los menús.
    '''
    @abstractmethod
    def coger_precio(self) -> float:
        pass


class Leaf(Component):
    '''
    Definimos la clase de los objetos hoja.
    En nuestro caso, los objetos hoja son los distinto precios que componen el total
    '''
    def __init__(self, precio: float) -> None:
        self._precio = precio

    def coger_precio(self) -> float:
        return self._precio


class Composite(Component):
    '''
    Nos recore cada hoja y nos calcula el precio total
    '''
    def __init__(self) -> None:
        self._hijo: List[Component] = []

    def add(self, component: Component) -> None:
        self._hijo.append(component)

    def remove(self, component: Component) -> None:
        self._hijo.remove(component)

    def coger_precio(self) -> float:
        precio_total = 0.0
        for hijo in self._hijo:
            precio_total += hijo.coger_precio()
        return precio_total


def client_code(component: Component):
    return component.coger_precio()



