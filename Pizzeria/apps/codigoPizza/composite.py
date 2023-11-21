from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    '''
    Definimos la interfaz de los objetos que formarán la estructura de árbol.
    En otras palabras, el método para coger el precio de los menus.
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


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    laptop = Leaf(1000.0)
    print("Client: I've got a laptop:")
    client_code(laptop)
    print("\n")

    # ...as well as the complex composites.
    cart = Composite()

    smartphone = Leaf(500.0)
    tablet = Leaf(300.0)

    cart.add(laptop)
    cart.add(smartphone)
    cart.add(tablet)

    print("Client: Now I've got a shopping cart:")
    print(client_code(cart))
    print("\n")
