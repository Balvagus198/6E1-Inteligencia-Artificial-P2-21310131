# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definir la clase Categoria como base para la taxonomía
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

# Definir subclases de Categoria para diferentes tipos de categorías
class Fruta(Categoria):
    def __init__(self, nombre):
        super().__init__(nombre)

class Animal(Categoria):
    def __init__(self, nombre):
        super().__init__(nombre)

# Crear instancias de categorías y objetos asociados
frutas = Fruta("Frutas")
manzana = "Manzana"
platano = "Plátano"
frutas.agregar_objeto(manzana)
frutas.agregar_objeto(platano)

animales = Animal("Animales")
perro = "Perro"
gato = "Gato"
animales.agregar_objeto(perro)
animales.agregar_objeto(gato)

# Mostrar la información de las categorías y sus objetos asociados
print(f"Categoría: {frutas.nombre}, Objetos: {', '.join(frutas.objetos)}")
print(f"Categoría: {animales.nombre}, Objetos: {', '.join(animales.objetos)}")
