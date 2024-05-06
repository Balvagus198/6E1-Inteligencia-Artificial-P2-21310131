# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generar datos de un proceso ARMA estacionario
np.random.seed(0)
n = 100  # Número de puntos de datos
phi = [0.5, -0.2]  # Coeficientes autorregresivos (AR)
theta = [0.3, -0.4]  # Coeficientes de medias móviles (MA)
mu = 0  # Media del proceso
sigma = 1  # Desviación estándar del proceso
arma_process = sm.tsa.ArmaProcess(phi, theta)  # Crear proceso ARMA
datos = arma_process.generate_sample(nsample=n)  # Generar datos del proceso

# Graficar la serie temporal generada
plt.figure(figsize=(10, 4))
plt.plot(datos)
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Proceso ARMA Estacionario')
plt.grid(True)
plt.show()

# Analizar el proceso ARMA
acf = sm.tsa.acf(datos, nlags=10)  # Función de autocorrelación
pacf = sm.tsa.pacf(datos, nlags=10)  # Función de autocorrelación parcial

# Graficar la función de autocorrelación y autocorrelación parcial
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.stem(acf)
plt.xlabel('Lag')
plt.ylabel('ACF')
plt.title('Función de Autocorrelación')
plt.grid(True)

plt.subplot(122)
plt.stem(pacf)
plt.xlabel('Lag')
plt.ylabel('PACF')
plt.title('Función de Autocorrelación Parcial')
plt.grid(True)

plt.tight_layout()
plt.show()
