# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definir las probabilidades a priori P(A) y P(B)
probabilidad_A = 0.3
probabilidad_B = 0.7

# Definir las probabilidades condicionales P(B|A) y P(A|B)
probabilidad_B_dado_A = 0.8
probabilidad_A_dado_B = 0.6

# Calcular la probabilidad conjunta P(B, A) utilizando la regla del producto
probabilidad_B_y_A = probabilidad_B_dado_A * probabilidad_A

# Aplicar la regla de Bayes para calcular P(A|B)
probabilidad_A_dado_B_actualizado = (probabilidad_B_dado_A * probabilidad_A) / probabilidad_B

# Mostrar los resultados
print(f"Probabilidad a priori de A: {probabilidad_A}")
print(f"Probabilidad a priori de B: {probabilidad_B}")
print(f"Probabilidad condicional de B dado A: {probabilidad_B_dado_A}")
print(f"Probabilidad condicional de A dado B: {probabilidad_A_dado_B}")
print(f"Probabilidad conjunta de B y A: {probabilidad_B_y_A}")
print(f"Probabilidad a posteriori de A dado B: {probabilidad_A_dado_B_actualizado}")
