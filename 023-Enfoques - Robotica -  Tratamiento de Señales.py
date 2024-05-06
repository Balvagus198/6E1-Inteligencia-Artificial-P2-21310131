# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:02:44 2024

@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

# Generar una señal sinusoidal
tiempo = np.linspace(0, 1, 1000)  # Tiempo de 0 a 1 segundo, 1000 puntos
frecuencia = 5  # Frecuencia de la señal en Hz
amplitud = 1  # Amplitud de la señal
senal = amplitud * np.sin(2 * np.pi * frecuencia * tiempo)  # Señal sinusoidal

# Agregar ruido a la señal
ruido = np.random.normal(0, 0.1, tiempo.shape)  # Ruido gaussiano
senal_con_ruido = senal + ruido

# Graficar la señal original y la señal con ruido
plt.figure(figsize=(10, 6))
plt.plot(tiempo, senal, label='Señal original')
plt.plot(tiempo, senal_con_ruido, label='Señal con ruido')
plt.title('Señal sinusoidal con ruido')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()
