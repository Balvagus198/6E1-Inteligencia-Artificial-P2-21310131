# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import pycosat

# Definir variables proposicionales para el problema de planificación
variables = {
    'A': 1,  # Acción A
    'B': 2,  # Acción B
    'C': 3,  # Acción C
    'S': 4,  # Estado Inicial
    'G': 5   # Estado Objetivo
}

# Definir cláusulas en lógica proposicional para el problema de planificación
clausulas = [
    [-variables['A'], -variables['S']],  # No(A) o No(S)
    [-variables['B'], variables['S']],   # No(B) o S
    [-variables['C'], variables['S']],   # No(C) o S
    [variables['A'], variables['G']],    # A o G
    [variables['B'], -variables['G']],   # B o No(G)
    [variables['C'], variables['G']]     # C o G
]

# Resolver el problema de satisfacibilidad (SAT) utilizando SATPLAN
resultado = pycosat.solve(clausulas)

# Mostrar el resultado
if resultado != "UNSAT":
    print("Plan encontrado:")
    for variable in resultado:
        if variable > 0:
            print(f"- {list(variables.keys())[list(variables.values()).index(variable)]}")
else:
    print("No se pudo encontrar un plan para satisfacer las cláusulas.")
