# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np

# Definir un espacio muestral para lanzar una moneda (0: cara, 1: cruz)
espacio_muestral = np.array([0, 1])

# Calcular la probabilidad de cada evento en el espacio muestral
probabilidad_cara = 0.5
probabilidad_cruz = 0.5

# Generar una muestra aleatoria de lanzamientos de moneda
num_lanzamientos = 1000
lanzamientos = np.random.choice(espacio_muestral, size=num_lanzamientos, p=[probabilidad_cara, probabilidad_cruz])

# Contar la frecuencia de cada resultado
frecuencia_cara = np.sum(lanzamientos == 0)
frecuencia_cruz = np.sum(lanzamientos == 1)

# Calcular la frecuencia relativa (proporción) de cada resultado
frecuencia_relativa_cara = frecuencia_cara / num_lanzamientos
frecuencia_relativa_cruz = frecuencia_cruz / num_lanzamientos

print(f"Frecuencia relativa de cara: {frecuencia_relativa_cara}")
print(f"Frecuencia relativa de cruz: {frecuencia_relativa_cruz}")
