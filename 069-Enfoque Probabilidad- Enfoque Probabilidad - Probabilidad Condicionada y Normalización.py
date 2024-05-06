# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definir probabilidades iniciales
probabilidad_A = 0.6
probabilidad_B = 0.4

# Calcular la probabilidad condicionada P(A|B) y P(B|A)
probabilidad_A_dado_B = 0.8
probabilidad_B_dado_A = 0.3

# Calcular la probabilidad conjunta P(A, B) utilizando la regla del producto
probabilidad_A_y_B = probabilidad_A_dado_B * probabilidad_B

# Calcular la probabilidad normalizada P(B|A) utilizando la regla de Bayes
probabilidad_B_dado_A_normalizada = (probabilidad_B_dado_A * probabilidad_A) / probabilidad_A_y_B

# Mostrar los resultados
print(f"Probabilidad condicionada P(A|B): {probabilidad_A_dado_B}")
print(f"Probabilidad condicionada P(B|A): {probabilidad_B_dado_A}")
print(f"Probabilidad normalizada P(B|A) después de normalización: {probabilidad_B_dado_A_normalizada}")
