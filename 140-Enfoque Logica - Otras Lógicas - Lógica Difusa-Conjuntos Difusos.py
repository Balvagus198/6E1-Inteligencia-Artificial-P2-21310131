# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


# Generar un universo de variables
x = np.arange(0, 11, 1)

# Generar conjuntos difusos
set_bajo = fuzz.trimf(x, [0, 0, 5])
set_medio = fuzz.trimf(x, [0, 5, 10])
set_alto = fuzz.trimf(x, [5, 10, 10])

# Visualizar conjuntos difusos
plt.figure()
plt.plot(x, set_bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(x, set_medio, 'g', linewidth=1.5, label='Medio')
plt.plot(x, set_alto, 'r', linewidth=1.5, label='Alto')
plt.title('Conjuntos Difusos')
plt.ylabel('Pertenencia')
plt.xlabel('Valor')
plt.legend()
plt.show()
