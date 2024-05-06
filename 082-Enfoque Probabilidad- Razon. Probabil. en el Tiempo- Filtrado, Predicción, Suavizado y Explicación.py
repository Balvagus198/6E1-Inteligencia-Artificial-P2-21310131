# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter

# Simular datos de un sistema dinámico (ejemplo: movimiento lineal)
np.random.seed(0)
n = 50  # Número de pasos de tiempo
dt = 1  # Intervalo de tiempo
velocidad_real = 2  # Velocidad real del sistema
ruido_medida = 1  # Desviación estándar del ruido de medición

# Generar datos simulados con ruido
tiempo = np.arange(n)
posicion_real = velocidad_real * tiempo + np.random.normal(0, ruido_medida, n)

# Configurar el filtro de Kalman para el sistema de movimiento lineal
kf = KalmanFilter(dim_x=2, dim_z=1)
kf.F = np.array([[1, dt],
                 [0, 1]])  # Matriz de transición de estado
kf.H = np.array([[1, 0]])  # Matriz de observación
kf.P *= 1000  # Covarianza inicial del estado
kf.R = ruido_medida**2  # Covarianza del ruido de medición

# Filtrado y predicción usando el filtro de Kalman
predicciones = []
for medida in posicion_real:
    kf.predict()  # Predicción del siguiente estado
    kf.update(medida)  # Actualización del estado basada en la medida
    predicciones.append(kf.x[0])  # Estado estimado (posición) después de la actualización

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(tiempo, posicion_real, label='Mediciones')
plt.plot(tiempo, predicciones, label='Predicciones (Filtrado)', linestyle='--')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtrado y Predicción con Filtro de Kalman')
plt.legend()
plt.grid(True)
plt.show()
