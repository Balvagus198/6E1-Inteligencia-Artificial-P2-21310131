# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definir la clase Animal como base para la ontología
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.caracteristicas = []

    def agregar_caracteristica(self, caracteristica):
        self.caracteristicas.append(caracteristica)

# Definir subclases de Animal para diferentes tipos de animales
class Mamifero(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

class Reptil(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

# Crear instancias de animales y agregar características
perro = Mamifero("Perro")
perro.agregar_caracteristica("Cuatro patas")
perro.agregar_caracteristica("Pelaje")

gato = Mamifero("Gato")
gato.agregar_caracteristica("Cuatro patas")
gato.agregar_caracteristica("Pelaje")

tortuga = Reptil("Tortuga")
tortuga.agregar_caracteristica("Caparazón")
tortuga.agregar_caracteristica("Reptil")

# Mostrar la información de los animales y sus características
print(f"Nombre: {perro.nombre}, Características: {', '.join(perro.caracteristicas)}")
print(f"Nombre: {gato.nombre}, Características: {', '.join(gato.caracteristicas)}")
print(f"Nombre: {tortuga.nombre}, Características: {', '.join(tortuga.caracteristicas)}")
