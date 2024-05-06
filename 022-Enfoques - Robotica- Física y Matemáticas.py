# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:00:56 2024

@author: Gustavo
"""

import math

class ObjetoMovil:
    def __init__(self, x, y, velocidad, angulo):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.angulo = angulo
    
    def mover(self, tiempo):
        # Convertir el ángulo de grados a radianes
        angulo_rad = math.radians(self.angulo)
        
        # Calcular el desplazamiento en las coordenadas x e y
        desplazamiento_x = self.velocidad * tiempo * math.cos(angulo_rad)
        desplazamiento_y = self.velocidad * tiempo * math.sin(angulo_rad)
        
        # Actualizar las coordenadas del objeto
        self.x += desplazamiento_x
        self.y += desplazamiento_y

# Crear un objeto móvil en posición (0, 0) con velocidad 5 y ángulo 45 grados
objeto = ObjetoMovil(0, 0, 5, 45)

# Simular el movimiento del objeto durante 2 segundos
objeto.mover(2)

# Imprimir las nuevas coordenadas del objeto
print("Nuevas coordenadas del objeto:")
print(f"Posición X: {objeto.x}")
print(f"Posición Y: {objeto.y}")
