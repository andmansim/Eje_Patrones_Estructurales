import csv


def usuario_valido(usuario, contrasenia):
    try:
        with open("usuarios.csv", mode='r') as file:
            leer = csv.reader(file)
            for row in leer:
                if row['usuario'] == usuario and row['contrasenia'] == contrasenia:
                    return True
        return False
    except FileNotFoundError:
        pass

def usuario_existe(usuario):
    print("hola")
    with open("usuarios.csv", mode='r') as file:
        
        leer = csv.reader(file)
        for row in leer:
            if row['usuario'] == usuario:
                return True
    return False


def registrar_usuario(usuario, contrasenia, correo, telefono, direccion):
    with open("usuarios.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        # Agrega al nuevo usuario
        writer.writerow([usuario, contrasenia, correo, telefono, direccion])
