# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class Estado:
    def __init__(self, nombre, atributos):
        self.nombre = nombre
        self.atributos = atributos  # Un diccionario que representa los atributos del estado

    def __repr__(self):
        return f"{self.nombre}: {self.atributos}"

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones  # Lista de precondiciones que deben cumplirse para ejecutar la acción
        self.efectos = efectos  # Lista de efectos que resultan de ejecutar la acción

    def __repr__(self):
        return f"{self.nombre} - Pre: {self.precondiciones}, Efecto: {self.efectos}"

# Definir estados
estado_inicial = Estado("Inicio", {"En_Casa": True, "Tener_Libros": True})
estado_objetivo = Estado("Objetivo", {"Saber_Materia": True})

# Definir acciones
accion_ir_biblioteca = Accion("Ir_Biblioteca", ["En_Casa"], ["En_Biblioteca"])
accion_estudiar = Accion("Estudiar", ["En_Biblioteca", "Tener_Libros"], ["Saber_Materia"])
accion_ir_casa = Accion("Ir_Casa", ["En_Biblioteca"], ["En_Casa"])

# Mostrar estados y acciones
print("Estado Inicial:", estado_inicial)
print("Estado Objetivo:", estado_objetivo)
print("Acciones:")
print(accion_ir_biblioteca)
print(accion_estudiar)
print(accion_ir_casa)
