# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import matplotlib.pyplot as plt

# Datos para el gráfico
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 11, 9]

# Crear el gráfico
plt.plot(x, y)

# Agregar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de ejemplo')

# Mostrar el gráfico
plt.show()
