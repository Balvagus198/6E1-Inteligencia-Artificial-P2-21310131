# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class BaseConocimiento:
    def __init__(self):
        self.hechos = set()  # Conjunto para almacenar los hechos conocidos

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def verificar_hecho(self, hecho):
        return hecho in self.hechos

# Ejemplo de uso
base = BaseConocimiento()

# Agregar hechos a la base de conocimiento
base.agregar_hecho("p")
base.agregar_hecho("q")
base.agregar_hecho("r")

# Verificar si un hecho está en la base de conocimiento
print(base.verificar_hecho("p"))  # True
print(base.verificar_hecho("s"))  # False
