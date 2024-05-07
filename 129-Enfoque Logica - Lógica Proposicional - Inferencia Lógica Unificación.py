# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sympy import symbols, Eq, unify, Or

# Definir las variables y constantes
x, y = symbols('x y')
A = symbols('A', cls=Or)
B = symbols('B', cls=Or)

# Definir dos expresiones lógicas para unificar
expresion_1 = Eq(A, x)
expresion_2 = Eq(B, y)

# Realizar la unificación
unificacion = unify(expresion_1, expresion_2)

print("Unificación:", unificacion)
