# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import cv2
import numpy as np

# Cargar una imagen de ejemplo en escala de grises
imagen = cv2.imread('naranja.jpg', cv2.IMREAD_GRAYSCALE)

# Mostrar la imagen original
cv2.imshow('Imagen Original', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Calcular la media y la desviación estándar de los valores de píxeles
media = np.mean(imagen)
desviacion_estandar = np.std(imagen)

print(f"Media de los píxeles: {media}")
print(f"Desviación estándar de los píxeles: {desviacion_estandar}")
