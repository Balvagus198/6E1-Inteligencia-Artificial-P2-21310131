# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
from prologpy import Prolog

# Inicializar el intérprete de Prolog
prolog = Prolog()

# Definir hechos y reglas en Prolog
prolog.assertz("padre(juan, pedro)")
prolog.assertz("padre(pedro, maria)")
prolog.assertz("padre(pedro, ana)")

# Realizar consultas en Prolog desde Python
for solucion in prolog.query("padre(X, Y)"):
    print(f"{solucion['X']} es padre de {solucion['Y']}")

