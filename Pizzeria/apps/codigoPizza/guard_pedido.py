import os
import csv

def guardar_pedido(id_cliente, datos_pedido, dato):
    # Define la ruta del archivo CSV basada en el ID del cliente
    archivo_csv = "pedidos_pizza.csv"
    archivo_csv2 = "pedidos_combo.csv"

    # Comprueba si el archivo ya existe
    nuevo_archivo = not os.path.exists(archivo_csv)
    nuevo_archivo2 = not os.path.exists(archivo_csv2)

    if dato == 'pizza':
        archivo = archivo_csv
        nuevo_arch= nuevo_archivo
        columnas = ["id_cliente", "Masa", "Salsa", "Ingredientes", "Cocción", "Presentación", "Bebida", "Postre"]
    else:
        archivo = archivo_csv2
        nuevo_arch = nuevo_archivo2
        columnas = ["id_cliente", "nombre", "bebida", "postre", "pizza", "precio"]
    # Agrega el nuevo pedido al archivo CSV
    with open(archivo, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Si es un nuevo archivo, escribe el encabezado
        if nuevo_arch:
            writer.writerow(columnas)

        # Agrega el nuevo pedido con el id_cliente
        writer.writerow([id_cliente] + datos_pedido)


def guardar_pedido_combo(id_cliente, datos_pedido):
    # Define la ruta del archivo CSV basada en el ID del cliente
    archivo_csv = "pedidos_combo.csv"

    # Comprueba si el archivo ya existe
    nuevo_archivo = not os.path.exists(archivo_csv)

    # Agrega el nuevo pedido al archivo CSV
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Si es un nuevo archivo, escribe el encabezado
        if nuevo_archivo:
            writer.writerow(["id_cliente", 'nombre', 'bebida', 'postre', 'pizza', 'precio'])

        # Agrega el nuevo pedido con el id_cliente
        writer.writerow([id_cliente] + datos_pedido)

