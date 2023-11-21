from abc import ABC, abstractmethod

class ComponenteMenu(ABC):
    @abstractmethod
    def obtener_precio(self):
        pass

class ElementoMenu(ComponenteMenu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

class MenuCompuesto(ComponenteMenu):
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def obtener_precio(self):
        return sum(elemento.obtener_precio() for elemento in self.elementos)

class Restaurante:
    def __init__(self):
        self.menu_principal = MenuCompuesto("MP", "Menú Principal")

    def agregar_elemento_a_menu(self, codigo_menu, elemento):
        for elemento_menu in self.menu_principal.elementos:
            if isinstance(elemento_menu, MenuCompuesto) and elemento_menu.codigo == codigo_menu:
                elemento_menu.agregar_elemento(elemento)
                return

    def obtener_precio_menu(self, codigo_menu):
        for elemento_menu in self.menu_principal.elementos:
            if isinstance(elemento_menu, MenuCompuesto) and elemento_menu.codigo == codigo_menu:
                return elemento_menu.obtener_precio()
        return None

# Ejemplo de uso:
restaurante = Restaurante()

# Crear elementos individuales
entrada = ElementoMenu("Entrada", 5.0)
bebida = ElementoMenu("Bebida", 3.0)
pizza_margarita = ElementoMenu("Margarita", 12.0)
postre = ElementoMenu("Postre", 4.0)

# Crear menús individuales
menu_individual_1 = MenuCompuesto("M1", "Menú Individual 1")
menu_individual_1.agregar_elemento(entrada)
menu_individual_1.agregar_elemento(pizza_margarita)
menu_individual_1.agregar_elemento(postre)

menu_individual_2 = MenuCompuesto("M2", "Menú Individual 2")
menu_individual_2.agregar_elemento(entrada)
menu_individual_2.agregar_elemento(bebida)
menu_individual_2.agregar_elemento(pizza_margarita)
menu_individual_2.agregar_elemento(postre)

# Agregar menús individuales al menú principal
restaurante.menu_principal.agregar_elemento(menu_individual_1)
restaurante.menu_principal.agregar_elemento(menu_individual_2)

# Crear menú compuesto (Combo Pareja)
combo_pareja = MenuCompuesto("CP", "Combo Pareja")
combo_pareja.agregar_elemento(menu_individual_1)
combo_pareja.agregar_elemento(menu_individual_2)

# Agregar menú compuesto al menú principal
restaurante.menu_principal.agregar_elemento(combo_pareja)

# Calcular el precio de un menú por su código
codigo_menu_buscar = "CP"
precio_menu = restaurante.obtener_precio_menu(codigo_menu_buscar)

if precio_menu is not None:
    print(f"El precio del menú {codigo_menu_buscar} es: ${precio_menu}")
else:
    print(f"No se encontró el menú con el código {codigo_menu_buscar}")
