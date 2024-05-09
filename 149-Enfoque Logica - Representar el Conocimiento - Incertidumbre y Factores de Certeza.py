# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear las variables de entrada y salida difusas
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
velocidad_ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad_ventilador')

# Definir funciones de membresía para las variables difusas
temperatura['fría'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['cálida'] = fuzz.trimf(temperatura.universe, [0, 50, 100])

humedad['seca'] = fuzz.trimf(humedad.universe, [0, 0, 50])
humedad['húmeda'] = fuzz.trimf(humedad.universe, [0, 50, 100])

velocidad_ventilador['baja'] = fuzz.trimf(velocidad_ventilador.universe, [0, 0, 50])
velocidad_ventilador['alta'] = fuzz.trimf(velocidad_ventilador.universe, [0, 50, 100])

# Visualizar las funciones de membresía
temperatura.view()
humedad.view()
velocidad_ventilador.view()

# Crear reglas difusas
regla1 = ctrl.Rule(temperatura['fría'] | humedad['seca'], velocidad_ventilador['baja'])
regla2 = ctrl.Rule(temperatura['cálida'] & humedad['húmeda'], velocidad_ventilador['alta'])

# Crear el sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2])
sistema = ctrl.ControlSystemSimulation(sistema_control)

# Establecer entradas
sistema.input['temperatura'] = 25
sistema.input['humedad'] = 75

# Realizar la evaluación del sistema
sistema.compute()

# Mostrar el resultado de la salida
print("Velocidad del ventilador:", sistema.output['velocidad_ventilador'])
velocidad_ventilador.view(sim=sistema)
