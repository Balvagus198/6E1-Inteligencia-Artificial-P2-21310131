# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import cv2
import numpy as np

# Cargar la imagen y el clasificador preentrenado
image_path = 'naranja.jpg'
cascade_path = 'naranja.xml'  # Cambia esto por la ruta de tu clasificador

# Cargar el clasificador Haar cascade para detección de rostros
face_cascade = cv2.CascadeClassifier(cascade_path)

# Leer la imagen
image = cv2.imread(image_path)

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar rostros en la imagen
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibujar rectángulos alrededor de los rostros detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar la imagen con los rostros detectados
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
