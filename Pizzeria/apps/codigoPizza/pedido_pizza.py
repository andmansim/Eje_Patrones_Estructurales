import os
import csv
def guardar_pedido_en_csv(id_cliente, datos_pedido):
    # Define la ruta del archivo CSV basada en el ID del cliente
    archivo_csv = f"pedidos_cliente_{id_cliente}.csv"

    # Comprueba si el archivo ya existe
    if not os.path.exists(archivo_csv):
        # Si no existe, crea un nuevo archivo CSV y escribe el encabezado
        with open(archivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Masa", "Salsa", "Ingredientes", "Cocción", "Presentación", "Bebida", "Postre"])

    # Agrega el nuevo pedido al archivo CSV
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(datos_pedido)
