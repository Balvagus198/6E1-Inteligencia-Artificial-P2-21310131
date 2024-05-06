# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ruta de la imagen
image_path = 'naranja.jpg'

# Intentar cargar la imagen
try:
    # Cargar la imagen
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Verificar si la imagen se cargó correctamente
    if image is None:
        raise FileNotFoundError('No se pudo cargar la imagen')

    # Convertir la imagen a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calcular el histograma de la imagen en escala de grises
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Calcular el histograma acumulado normalizado
    cdf = histogram.cumsum()
    cdf_normalized = cdf / cdf.max()

    # Crear la función de ecualización de histograma
    equalized_image = cv2.equalizeHist(gray_image)

    # Mostrar las imágenes y sus histogramas
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Imagen en Escala de Grises')
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.plot(histogram)
    plt.title('Histograma de la Imagen en Escala de Grises')

    plt.subplot(2, 3, 4)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Imagen Ecualizada')
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.plot(cdf_normalized, color='b')
    plt.title('Histograma Acumulado Normalizado')

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f'Error: {e}')
