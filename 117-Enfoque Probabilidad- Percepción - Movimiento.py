# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import cv2

# Capturar video desde la cámara (0 para la cámara predeterminada)
cap = cv2.VideoCapture(0)

# Capturar el primer frame para establecer el fondo
ret, background = cap.read()

# Convertir el fondo a escala de grises
background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

while True:
    # Capturar un frame
    ret, frame = cap.read()
    
    # Convertir el frame actual a escala de grises
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calcular la diferencia entre el frame actual y el fondo
    diff = cv2.absdiff(frame_gray, background_gray)
    
    # Aplicar un umbral para resaltar las diferencias significativas
    threshold = 30
    _, thresholded_diff = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    
    # Encontrar contornos de las diferencias
    contours, _ = cv2.findContours(thresholded_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Dibujar los contornos sobre el frame original
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    
    # Mostrar el frame con las diferencias destacadas
    cv2.imshow('Detección de Movimiento', frame)
    
    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
