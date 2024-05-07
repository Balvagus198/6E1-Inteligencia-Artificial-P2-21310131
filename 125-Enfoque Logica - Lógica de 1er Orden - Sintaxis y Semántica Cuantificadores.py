# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sympy import symbols, forall, exists

# Definir variables
x, y = symbols('x y')

# Ejemplo de cuantificador universal (para todo)
expresion_universal = forall(x, x > 0)

# Ejemplo de cuantificador existencial (existe al menos uno)
expresion_existencial = exists(y, y < 0)

# Evaluar las expresiones
print("Para la expresión universal, ¿es cierto para todo x que x > 0?")
print(expresion_universal)

print("Para la expresión existencial, ¿existe algún y tal que y < 0?")
print(expresion_existencial)
