import csv
import os

class Usuario:
    def __init__(self, nombre, direccion, telefono, correo, contrasenia):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.contrasenia = contrasenia
        self.ordenes = []
        
    def usuario_valido(self):
        file_exists = os.path.isfile("usuarios.csv")
        if file_exists: #Por si no existe el csv escribe el encabezado
            with open("usuarios.csv", mode='r', newline='') as file:
                leer = csv.DictReader(file)
                for row in leer:
                    if row['nombre'] == self.nombre and row['contrasenia'] == self.contrasenia:
                        return True
        return False
        
    def usuario_existe(self):
        file_exists = os.path.isfile("usuarios.csv")
        if file_exists:
            with open("usuarios.csv", mode='r', newline='') as file:
                
                leer = csv.DictReader(file)
                for row in leer:
                    if row['nombre'] == self.nombre:
                        return True
        return False


    def registrar_usuario(self):
        file_exists = os.path.isfile("usuarios.csv")
        with open("usuarios.csv", mode='a', newline='') as file:
            fieldnames = ['nombre', 'direccion', 'telefono', 'correo', 'contrasenia']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists: #Por si no existe el csv escribe el encabezado
                writer.writeheader()
            # Agrega al nuevo usuario
            writer.writerow({'nombre': self.nombre, 'direccion': self.direccion, 'telefono': self.telefono, 'correo': self.correo, 'contrasenia': self.contrasenia})
