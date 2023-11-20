import os
import csv

def guardar_pedido_en_csv(id_cliente, datos_pedido):
    # Define la ruta del archivo CSV basada en el ID del cliente
    archivo_csv = f"pedidos_clientes.csv"

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

