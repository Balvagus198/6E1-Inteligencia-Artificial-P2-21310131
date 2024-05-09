# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sympy import symbols, Function, And, ForAll

# Definir variables y funciones de primer y segundo orden
x, y = symbols('x y')
P = Function('P')
Q = Function('Q')
R = Function('R')
S = Function('S')

# Expresar una fórmula de segundo orden
formula = ForAll(x, ForAll(y, And(P(x), Q(y), R(x, y), S(P, Q, R))))

# Imprimir la fórmula
print("Fórmula de segundo orden:", formula)
