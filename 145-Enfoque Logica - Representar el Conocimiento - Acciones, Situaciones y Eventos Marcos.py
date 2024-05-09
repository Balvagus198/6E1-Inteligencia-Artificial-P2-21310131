# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definir la clase Accion para representar acciones en un marco
class Accion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def ejecutar(self):
        print(f"Ejecutando la acción: {self.nombre}")

# Definir la clase Situacion para representar situaciones en un marco
class Situacion:
    def __init__(self, nombre, lugar):
        self.nombre = nombre
        self.lugar = lugar

    def describir(self):
        print(f"La situación {self.nombre} ocurre en {self.lugar}")

# Definir la clase Evento para representar eventos en un marco
class Evento:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha

    def mostrar(self):
        print(f"El evento {self.nombre} ocurre en la fecha {self.fecha}")

# Crear instancias de acciones, situaciones y eventos
comer = Accion("Comer", "30 minutos")
casa = Situacion("En casa", "La cocina")
fiesta = Evento("Fiesta de cumpleaños", "10 de mayo")

# Ejecutar la acción, describir la situación y mostrar el evento
comer.ejecutar()
casa.describir()
fiesta.mostrar()
