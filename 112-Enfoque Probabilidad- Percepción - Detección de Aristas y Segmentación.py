# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread('naranja.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el detector de bordes (Canny)
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Realizar la segmentación mediante umbralización
ret, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Mostrar las imágenes
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(edges, cmap='gray')
plt.title('Detección de Bordes (Canny)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(thresholded, cmap='gray')
plt.title('Segmentación por Umbralización')
plt.axis('off')

plt.tight_layout()
plt.show()
