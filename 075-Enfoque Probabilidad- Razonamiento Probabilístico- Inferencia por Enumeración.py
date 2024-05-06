# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np

# Definir las variables del modelo probabilístico
variables = ['A', 'B', 'C']

# Definir las posibles combinaciones de valores para las variables
valores_posibles = {
    'A': [True, False],
    'B': [True, False],
    'C': [True, False]
}

# Definir la probabilidad conjunta P(A, B, C)
probabilidad_conjunta = np.array([0.2, 0.1, 0.3, 0.4])

# Definir la evidencia observada (por ejemplo, B=True)
evidencia = {'B': True}

# Función para calcular la probabilidad condicional de una variable dada la evidencia
def calcular_probabilidad_condicional(variable, evidencia):
    probabilidades_condicionales = []
    for valor in valores_posibles[variable]:
        nueva_evidencia = evidencia.copy()
        nueva_evidencia[variable] = valor
        probabilidad_conjunta_consistente = np.prod([probabilidad_conjunta[i] for i, val in enumerate(variables) if nueva_evidencia.get(val, None) == val])
        probabilidad_evidencia = np.prod([probabilidad_conjunta[i] for i, val in enumerate(variables) if nueva_evidencia.get(val, None) is not None])
        probabilidad_condicional = probabilidad_conjunta_consistente / probabilidad_evidencia
        probabilidades_condicionales.append(probabilidad_condicional)
    return probabilidades_condicionales

# Calcular la probabilidad condicional de A dado B=True
probabilidad_A_dado_B_verdadero = calcular_probabilidad_condicional('A', evidencia)
print("Probabilidad de A dado B=True:", probabilidad_A_dado_B_verdadero)
