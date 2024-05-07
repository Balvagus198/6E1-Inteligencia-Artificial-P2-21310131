# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import random

def generar_asignacion_inicial(variables):
    return {variable: random.choice([True, False]) for variable in variables}

def evaluar_funcion_objetivo(asignacion_actual, funcion_objetivo):
    return funcion_objetivo(asignacion_actual)

def hill_climbing(variables, funcion_objetivo, max_iter=1000):
    asignacion_actual = generar_asignacion_inicial(variables)
    valor_actual = evaluar_funcion_objetivo(asignacion_actual, funcion_objetivo)

    for _ in range(max_iter):
        vecino = generar_vecino(asignacion_actual)
        valor_vecino = evaluar_funcion_objetivo(vecino, funcion_objetivo)

        if valor_vecino > valor_actual:
            asignacion_actual = vecino
            valor_actual = valor_vecino

    return asignacion_actual, valor_actual

# Ejemplo de uso
def funcion_objetivo(asignacion):
    # Función objetivo simple: contar la cantidad de variables verdaderas
    return sum(1 for valor in asignacion.values() if valor)

def generar_vecino(asignacion_actual):
    vecino = asignacion_actual.copy()
    variable_a_cambiar = random.choice(list(asignacion_actual.keys()))
    vecino[variable_a_cambiar] = not vecino[variable_a_cambiar]
    return vecino

variables = ['A', 'B', 'C']
solucion, valor_optimo = hill_climbing(variables, funcion_objetivo)

print("Solución encontrada:")
print(solucion)
print("Valor óptimo de la función objetivo:", valor_optimo)
