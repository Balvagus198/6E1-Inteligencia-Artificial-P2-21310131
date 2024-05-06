# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Crear una señal de ejemplo (senoidal con ruido)
np.random.seed(0)
fs = 1000  # frecuencia de muestreo
t = np.arange(0, 1, 1/fs)  # vector de tiempo de 1 segundo
x = np.sin(2*np.pi*50*t) + 0.5*np.random.randn(len(t))

# Aplicar un filtro paso bajo (suavizado)
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

cutoff_frequency = 100  # frecuencia de corte del filtro (Hz)
filtered_signal = butter_lowpass_filter(x, cutoff_frequency, fs)

# Graficar la señal original y la señal filtrada
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Señal original')
plt.plot(t, filtered_signal, label='Señal filtrada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.title('Filtro Paso Bajo - Suavizado')
plt.legend()
plt.grid(True)
plt.show()
