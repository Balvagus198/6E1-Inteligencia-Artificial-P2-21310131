# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import sympy as sp

# Definir las variables proposicionales
p = sp.Symbol('p')
q = sp.Symbol('q')

# Crear las expresiones lógicas
expresion_1 = sp.Eq(p | q, q)
expresion_2 = sp.Eq(p & q, p)

# Verificar equivalencia
equivalencia = sp.simplify(expresion_1.equals(expresion_2))
print(f"Las expresiones son equivalentes: {equivalencia}")

# Verificar validez (tanto por tabla de verdad como por el método de tautología)
tabla_validez = sp.ask(sp.Q.all_true, expresion_1)
tautologia_validez = sp.is_Tautology(expresion_1)
print(f"Es válida por tabla de verdad: {tabla_validez}")
print(f"Es una tautología: {tautologia_validez}")

# Verificar satisfacibilidad
satisfacibilidad = sp.ask(sp.Q.satisfiable, expresion_1)
print(f"Es satisfacible: {satisfacibilidad}")
