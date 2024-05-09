# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
class Tarea:
    def __init__(self, nombre, nivel, subtareas=None):
        self.nombre = nombre
        self.nivel = nivel
        self.subtareas = subtareas if subtareas is not None else []

    def __repr__(self):
        return f"Tarea({self.nombre}, Nivel {self.nivel}, Subtareas: {self.subtareas})"

# Crear tareas y organizarlas en una red jerárquica
tarea1 = Tarea("Tarea 1", 1)
tarea2 = Tarea("Tarea 2", 1)
tarea3 = Tarea("Tarea 3", 1)
tarea4 = Tarea("Tarea 4", 2, [tarea1, tarea2])
tarea5 = Tarea("Tarea 5", 2, [tarea3])
tarea6 = Tarea("Tarea 6", 3, [tarea4, tarea5])

# Mostrar la red jerárquica de tareas
print(tarea6)
