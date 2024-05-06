# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np

# Definir la matriz de transición de la cadena de Markov
# En este ejemplo, la matriz representa una cadena con 3 estados
# La fila i y columna j representa la probabilidad de pasar del estado i al estado j
matriz_transicion = np.array([[0.8, 0.1, 0.1],
                               [0.2, 0.6, 0.2],
                               [0.3, 0.2, 0.5]])

# Definir el estado inicial de la cadena de Markov
estado_actual = 0  # Comenzamos en el estado 0

# Simular la cadena de Markov durante 10 pasos
num_pasos = 10
historial_estados = [estado_actual]

for _ in range(num_pasos):
    # Calcular el siguiente estado basado en la matriz de transición
    siguiente_estado = np.random.choice([0, 1, 2], p=matriz_transicion[estado_actual])
    
    # Guardar el siguiente estado en el historial
    historial_estados.append(siguiente_estado)
    
    # Actualizar el estado actual para el siguiente paso
    estado_actual = siguiente_estado

# Mostrar el historial de estados
print("Historial de estados de la cadena de Markov:")
print(historial_estados)
