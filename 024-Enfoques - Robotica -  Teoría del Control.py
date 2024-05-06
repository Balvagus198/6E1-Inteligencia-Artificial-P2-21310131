# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que representa el modelo dinámico del sistema (robot)
def modelo_dinamico(y, t):
    Kp = 2  # Ganancia proporcional
    Ki = 1  # Ganancia integral
    Kd = 1  # Ganancia derivativa
    setpoint = 1  # Valor deseado de posición
    
    # Calcular el error y sus componentes
    error = setpoint - y[0]
    integral = y[1] + error * t
    derivativa = error - y[2]
    
    # Calcular la señal de control (controlador PID)
    u = Kp * error + Ki * integral + Kd * derivativa
    
    # Modelo dinámico del sistema (ecuación diferencial)
    dydt = y[1], u, error
    return dydt

# Condiciones iniciales
y0 = [0, 0, 0]  # Posición inicial, velocidad inicial, error inicial

# Tiempo de simulación
t = np.linspace(0, 10, 1000)

# Resolver la ecuación diferencial con odeint
sol = odeint(modelo_dinamico, y0, t)

# Graficar la respuesta del sistema
plt.figure(figsize=(10, 6))
plt.plot(t, sol[:, 0], label='Posición')
plt.plot(t, sol[:, 1], label='Velocidad')
plt.plot(t, sol[:, 2], label='Error')
plt.title('Respuesta del sistema controlado con PID')
plt.xlabel('Tiempo (s)')
plt.ylabel('Magnitud')
plt.legend()
plt.grid(True)
plt.show()
