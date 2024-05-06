# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definir las probabilidades de los eventos A, B y C
probabilidad_A = 0.4
probabilidad_B = 0.3
probabilidad_C = 0.5

# Definir las probabilidades condicionales P(A|C) y P(B|C)
probabilidad_A_dado_C = 0.6
probabilidad_B_dado_C = 0.4

# Calcular la probabilidad conjunta P(A ∩ B | C)
probabilidad_conjunta_A_y_B_dado_C = probabilidad_A_dado_C * probabilidad_B_dado_C

# Calcular P(A|C) * P(B|C)
probabilidad_A_dado_C_multiplicado_B_dado_C = probabilidad_A_dado_C * probabilidad_B_dado_C

# Verificar si se cumple la igualdad para la independencia condicional
es_independiente_condicionalmente = probabilidad_conjunta_A_y_B_dado_C == probabilidad_A_dado_C_multiplicado_B_dado_C

# Mostrar el resultado
print(f"¿A y B son independientes condicionalmente a C? {es_independiente_condicionalmente}")
