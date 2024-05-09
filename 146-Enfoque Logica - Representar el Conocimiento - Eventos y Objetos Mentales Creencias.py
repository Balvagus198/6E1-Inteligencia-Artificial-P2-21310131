# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definir la clase Evento para representar eventos
class Evento:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha

    def mostrar(self):
        print(f"El evento {self.nombre} ocurrió en la fecha {self.fecha}")

# Definir la clase Creencia para representar creencias
class Creencia:
    def __init__(self, sujeto, evento, opinion):
        self.sujeto = sujeto
        self.evento = evento
        self.opinion = opinion

    def expresar(self):
        print(f"{self.sujeto} cree que el evento {self.evento.nombre} fue {self.opinion}")

# Crear instancias de eventos y creencias
cumpleaños = Evento("Fiesta de Cumpleaños", "15 de mayo")
juan = "Juan"
creencia_juan = Creencia(juan, cumpleaños, "divertido")

# Mostrar el evento y la creencia expresada
cumpleaños.mostrar()
creencia_juan.expresar()
