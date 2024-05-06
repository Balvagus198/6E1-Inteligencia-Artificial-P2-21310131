# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de transición del Proceso de Markov
# En este ejemplo, tenemos un Proceso de Markov de dos estados (0 y 1)
# La matriz de transición representa las probabilidades de transición entre estados
# Ejemplo de matriz de transición: [[0.7, 0.3], [0.4, 0.6]]
transiciones = np.array([[0.7, 0.3], [0.4, 0.6]])

# Definir el estado inicial y el número de pasos de tiempo
estado_actual = 0  # Estado inicial
num_pasos = 1000  # Número de pasos de tiempo

# Simular el Proceso de Markov
estados_simulados = [estado_actual]
for _ in range(num_pasos):
    estado_siguiente = np.random.choice([0, 1], p=transiciones[estado_actual])
    estados_simulados.append(estado_siguiente)
    estado_actual = estado_siguiente

# Graficar la evolución de los estados en el tiempo
plt.figure(figsize=(10, 4))
plt.plot(estados_simulados)
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.title('Simulación de un Proceso de Markov')
plt.yticks([0, 1], ['Estado 0', 'Estado 1'])
plt.grid(True)
plt.show()
