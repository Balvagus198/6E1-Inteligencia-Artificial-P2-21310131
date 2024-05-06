# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np

# Definir la distribución de probabilidad condicional de una variable (ejemplo simplificado)
def p(x):
    return np.sin(x) ** 2

# Definir la distribución auxiliar (uniforme en este caso)
def q(x):
    return 1.0 / np.pi

# Función de muestreo por rechazo
def rejection_sampling(num_samples):
    samples = []
    for _ in range(num_samples):
        x = np.random.uniform(0, np.pi)  # Generar una muestra de la distribución auxiliar
        u = np.random.uniform(0, 1)  # Generar un número aleatorio entre 0 y 1
        if u < p(x) / q(x):
            samples.append(x)  # Aceptar la muestra con cierta probabilidad
    return samples

# Realizar muestreo por rechazo para aproximar la distribución de p(x)
num_samples = 10000
samples = rejection_sampling(num_samples)

# Calcular la probabilidad aproximada de un evento A (por ejemplo, x > pi/2)
probabilidad_aproximada = len([x for x in samples if x > np.pi / 2]) / num_samples
print("Probabilidad aproximada de x > pi/2:", probabilidad_aproximada)
