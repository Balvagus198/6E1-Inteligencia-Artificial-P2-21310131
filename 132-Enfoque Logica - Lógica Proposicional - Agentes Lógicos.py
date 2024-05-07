# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sympy import symbols, Function, Or, And, Implies

# Definir variables y funciones
x, y = symbols('x y')
P = Function('P')
Q = Function('Q')

# Conocimiento del agente: reglas lógicas
regla1 = Implies(And(P(x), Q(y)), Or(P(x), Q(y)))
regla2 = Implies(P(x), Or(P(x), Q(y)))

# Conocimiento adicional del agente
conocimiento_adicional = And(P(x), Q(y))

# Inferencia utilizando las reglas lógicas y el conocimiento adicional
inferencia1 = regla1.subs({P(x): conocimiento_adicional})
inferencia2 = regla2.subs({P(x): conocimiento_adicional})

# Imprimir resultados
print("Regla 1:", regla1)
print("Regla 2:", regla2)
print("Conocimiento adicional:", conocimiento_adicional)
print("Inferencia 1:", inferencia1)
print("Inferencia 2:", inferencia2)
