import os
import csv

def guardar_pedido_pizza(id_cliente, datos_pedido):
    # Define la ruta del archivo CSV basada en el ID del cliente
    archivo_csv = "pedidos_pizza.csv"

    # Comprueba si el archivo ya existe
    nuevo_archivo = not os.path.exists(archivo_csv)

    # Agrega el nuevo pedido al archivo CSV
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Si es un nuevo archivo, escribe el encabezado
        if nuevo_archivo:
            writer.writerow(["id_cliente", "Masa", "Salsa", "Ingredientes", "Cocción", "Presentación", "Bebida", "Postre"])

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

