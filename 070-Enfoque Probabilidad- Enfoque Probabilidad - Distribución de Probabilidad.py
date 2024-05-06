# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución normal (media y desviación estándar)
media = 0
desviacion_estandar = 1

# Generar datos aleatorios a partir de una distribución normal
datos = np.random.normal(media, desviacion_estandar, 1000)

# Graficar el histograma de los datos para visualizar la distribución
plt.hist(datos, bins=30, density=True, alpha=0.6, color='g')

# Calcular la densidad de probabilidad de la distribución normal
x = np.linspace(-4, 4, 100)
densidad_probabilidad = (1 / (desviacion_estandar * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media) / desviacion_estandar) ** 2)

# Graficar la densidad de probabilidad
plt.plot(x, densidad_probabilidad, '--', color='b', linewidth=2)

# Mostrar la gráfica
plt.title('Distribución de Probabilidad Normal')
plt.xlabel('Valores')
plt.ylabel('Densidad de Probabilidad')
plt.legend(['Densidad de Probabilidad', 'Histograma de Datos'])
plt.show()
