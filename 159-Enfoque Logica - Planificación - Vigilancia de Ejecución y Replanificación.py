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

# Función para ejecutar una acción
def ejecutar_accion(accion, estado_actual):
    if all(precondicion in estado_actual for precondicion in accion.precondiciones):
        estado_actual += accion.efectos
        print(f"Ejecutando acción: {accion.nombre}")
    else:
        print(f"No se pueden ejecutar {accion.nombre}, precondiciones no cumplidas")

# Definir acciones
accion_ir_biblioteca = Accion("Ir_Biblioteca", ["En_Casa"], ["En_Biblioteca"])
accion_estudiar = Accion("Estudiar", ["En_Biblioteca", "Tener_Libros"], ["Saber_Materia"])
accion_ir_casa = Accion("Ir_Casa", ["En_Biblioteca"], ["En_Casa"])

# Estado inicial y estado objetivo
estado_inicial = ["En_Casa", "Tener_Libros"]
estado_objetivo = ["Saber_Materia"]

# Plan original
plan_original = [accion_ir_biblioteca, accion_estudiar, accion_ir_casa]

# Ejecutar el plan original
estado_actual = estado_inicial.copy()
for accion in plan_original:
    ejecutar_accion(accion, estado_actual)

# Simular una desviación o problema
estado_actual.remove("Tener_Libros")

# Vigilancia de ejecución y replanificación
if estado_actual != estado_objetivo:
    print("Desviación detectada, iniciando replanificación...")
    # Aquí iría el proceso de replanificación para generar un nuevo plan
    # Por simplicidad, simularemos la replanificación con un nuevo plan estático
    nuevo_plan = [accion_ir_biblioteca, accion_ir_casa]
    print("Nuevo plan generado:")
    for accion in nuevo_plan:
        ejecutar_accion(accion, estado_actual)
else:
    print("Plan ejecutado con éxito, objetivo alcanzado.")
