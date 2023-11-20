import csv

class GestorUsuarios:

    def usuario_valido(self, usuario, contrasenia):
        try:
            with open("usuarios.csv", mode='r') as file:
                leer = csv.reader(file)
                for row in leer:
                    if row['usuario'] == usuario and row['contrasenia'] == contrasenia:
                        return True
            return False
        except FileNotFoundError:
            pass

    def usuario_existe(self, usuario):
        try:
            with open("usuarios.csv", mode='r') as file:
                leer = csv.reader(file)
                for row in leer:
                    if row['usuario'] == usuario:
                        return True
            return False
        except FileNotFoundError:
            pass
        

    def registrar_usuario(self, id_usuario, usuario, contrasenia, correo, telefono, direccion):
        with open("usuarios.csv", mode='a', newline='') as file:
            writer = csv.writer(file)

            # Si el archivo está vacío, escribe el encabezado
            if file.tell() == 0:
                writer.writerow(["id_usuario", "usuario", "contrasenia", "correo", "telefono", "direccion"])

            # Agrega al nuevo usuario
            writer.writerow([id_usuario, usuario, contrasenia, correo, telefono, direccion])
    