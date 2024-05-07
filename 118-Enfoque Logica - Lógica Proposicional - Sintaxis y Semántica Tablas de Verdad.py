# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import itertools

class TablaVerdad:
    def __init__(self, variables, expresion):
        self.variables = variables  # Lista de variables en la expresión lógica
        self.expresion = expresion  # Expresión lógica en forma de cadena

    def generar_tabla(self):
        combinaciones = list(itertools.product([False, True], repeat=len(self.variables)))
        encabezado = self.variables + [self.expresion]
        tabla = [encabezado]

        for combinacion in combinaciones:
            valores = dict(zip(self.variables, combinacion))
            resultado = eval(self.expresion, valores)
            fila = list(combinacion) + [resultado]
            tabla.append(fila)

        return tabla

# Ejemplo de uso
variables = ["p", "q"]
expresion = "(p and q) or (not p)"
tabla_verdad = TablaVerdad(variables, expresion)
tabla = tabla_verdad.generar_tabla()

for fila in tabla:
    print(fila)
