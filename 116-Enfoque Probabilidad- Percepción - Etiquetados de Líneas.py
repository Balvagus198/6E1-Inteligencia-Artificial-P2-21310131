# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
import cv2
import numpy as np

# Path de la imagen
image_path = 'IA.jpg'

# Cargar la imagen
image = cv2.imread(image_path)

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes utilizando Canny
edges = cv2.Canny(gray, threshold1=50, threshold2=150, apertureSize=3)

# Encontrar líneas en la imagen utilizando la transformada de Hough
lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)

# Dibujar las líneas sobre la imagen original
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Mostrar la imagen con las líneas etiquetadas
cv2.imshow('Líneas Etiquetadas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

