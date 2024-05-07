# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sympy import symbols, Implies
from sympy.logic.boolalg import to_cnf

# Definir las variables proposicionales
p, q, r = symbols('p q r')

# Definir algunas expresiones lógicas
expresion_1 = Implies(p, q)
expresion_2 = Implies(q, r)

# Convertir las expresiones lógicas a Forma Normal Conjuntiva (FNC)
fnc_expresion_1 = to_cnf(expresion_1)
fnc_expresion_2 = to_cnf(expresion_2)

print("Expresión 1 en FNC:", fnc_expresion_1)
print("Expresión 2 en FNC:", fnc_expresion_2)
