import csv
import os
import secrets
from flask import flash, redirect, render_template, request

class GestorUsuarios:
    def __init__(self, archivo_usuarios="usuarios.csv"):
        self.archivo_usuarios = archivo_usuarios

    def usuario_valido(self, usuario, contrasenia):
        with open(self.archivo_usuarios, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['usuario'] == usuario and row['contrasenia'] == contrasenia:
                    return True
        return False

    def usuario_existe(self, usuario):
        with open(self.archivo_usuarios, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['usuario'] == usuario:
                    return True
        return False

    def registrar_usuario(self, id_usuario, usuario, contrasenia, correo, telefono, direccion):
        with open(self.archivo_usuarios, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Si es un nuevo archivo, escribe el encabezado
            if file.tell() == 0:
                writer.writerow(["id_usuario", "usuario", "contrasenia", "correo", "telefono", "direccion"])

            # Agrega al nuevo usuario
            writer.writerow([id_usuario, usuario, contrasenia, correo, telefono, direccion])

   

    