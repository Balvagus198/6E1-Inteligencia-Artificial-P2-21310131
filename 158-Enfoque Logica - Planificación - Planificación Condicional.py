# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones  # Lista de precondiciones que deben cumplirse para ejecutar la acción
        self.efectos = efectos  # Lista de efectos que resultan de ejecutar la acción

    def __repr__(self):
        return f"{self.nombre} - Pre: {self.precondiciones}, Efecto: {self.efectos}"

# Definir acciones condicionales
accion_ir_biblioteca = Accion("Ir_Biblioteca", ["En_Casa"], ["En_Biblioteca"])
accion_estudiar = Accion("Estudiar", ["En_Biblioteca", "Tener_Libros"], ["Saber_Materia"])
accion_ir_casa = Accion("Ir_Casa", ["En_Biblioteca"], ["En_Casa"])
accion_aprender_python = Accion("Aprender_Python", ["Saber_Materia"], ["Python_Aprendido"])

# Estado inicial y estado objetivo
estado_inicial = ["En_Casa", "Tener_Libros"]
estado_objetivo = ["Python_Aprendido"]

# Ejecutar el planificador condicional
plan = []
estado_actual = estado_inicial.copy()

# Definir reglas condicionales para seleccionar acciones
while estado_actual != estado_objetivo:
    if "En_Casa" in estado_actual and "Tener_Libros" in estado_actual:
        plan.append(accion_ir_biblioteca)
        estado_actual += ["En_Biblioteca"]
    elif "En_Biblioteca" in estado_actual and "Tener_Libros" in estado_actual:
        plan.append(accion_estudiar)
        estado_actual += ["Saber_Materia"]
    elif "En_Biblioteca" in estado_actual:
        plan.append(accion_ir_casa)
        estado_actual.remove("En_Biblioteca")
    elif "Saber_Materia" in estado_actual:
        plan.append(accion_aprender_python)
        estado_actual.append("Python_Aprendido")

# Mostrar el plan resultante
print("Plan encontrado:")
for accion in plan:
    print(accion)
