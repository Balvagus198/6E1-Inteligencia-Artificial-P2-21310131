# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import cv2
import pytesseract

# Path de la imagen
image_path = 'IA.jpg'

# Cargar la imagen
image = cv2.imread(image_path)

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Utilizar Tesseract OCR para reconocer texto en la imagen
custom_config = r'--oem 3 --psm 6'  # Configuración personalizada para Tesseract OCR
text = pytesseract.image_to_string(gray, config=custom_config)

# Mostrar el texto reconocido
print("Texto reconocido:")
print(text)
