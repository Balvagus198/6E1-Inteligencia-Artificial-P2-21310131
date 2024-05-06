# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from filterpy.kalman import KalmanFilter
import numpy as np

# Crear el filtro de Kalman
kf = KalmanFilter(dim_x=2, dim_z=1)

# Definir las matrices de transición y observación
kf.F = np.array([[1, 1],
                 [0, 1]])  # Matriz de transición

kf.H = np.array([[1, 0]])  # Matriz de observación

# Definir las matrices de covarianza del proceso y observación
kf.Q = np.array([[0.01, 0],
                 [0, 0.01]])  # Covarianza del proceso

kf.R = np.array([[0.1]])  # Covarianza de la observación

# Definir la estimación inicial y la covarianza inicial
kf.x = np.array([0, 0])  # Estimación inicial
kf.P = np.eye(2)  # Covarianza inicial

# Generar datos de prueba
np.random.seed(0)
measurements = np.random.normal(loc=0, scale=0.1, size=(100, 1))

# Aplicar el filtro de Kalman a los datos de prueba
filtered_states = []
for measurement in measurements:
    kf.predict()
    kf.update(measurement)
    filtered_states.append(kf.x)

# Imprimir los estados filtrados
print("Estados filtrados:")
for state in filtered_states:
    print(state)
