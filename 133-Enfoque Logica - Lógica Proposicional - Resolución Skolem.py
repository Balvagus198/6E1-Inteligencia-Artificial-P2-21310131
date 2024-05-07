# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sympy import symbols, Function, Or, And, Not, simplify

# Definir variables
x, y = symbols('x y')
P = Function('P')
Q = Function('Q')

# Definir la fórmula en lógica de primer orden
formula = Or(And(P(x), Q(y)), Not(And(P(x), Q(y))))

# Aplicar la resolución Skolem
skolemized = formula.skolemize()

# Simplificar la fórmula
simplified = simplify(skolemized)

# Imprimir el resultado
print("Fórmula original:", formula)
print("Fórmula Skolemizada:", skolemized)
print("Fórmula simplificada:", simplified)
