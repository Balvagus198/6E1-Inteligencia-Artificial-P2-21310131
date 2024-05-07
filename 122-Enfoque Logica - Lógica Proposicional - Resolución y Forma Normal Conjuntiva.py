# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import sympy as sp

# Definir las variables proposicionales
p = sp.Symbol('p')
q = sp.Symbol('q')

# Crear la expresión lógica
expresion = (p | q) & (~p | q)  # Ejemplo de expresión lógica

# Aplicar resolución
resolucion = sp.ask(sp.Q.resolvent, expresion)

# Obtener la Forma Normal Conjuntiva (FNC)
fnc = sp.to_cnf(expresion)

# Imprimir los resultados
print(f"Expresión original: {expresion}")
print(f"Resolución aplicada: {resolucion}")
print(f"Forma Normal Conjuntiva (FNC): {fnc}")
