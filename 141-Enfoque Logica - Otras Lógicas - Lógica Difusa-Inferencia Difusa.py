# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear las variables difusas
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'ventilador')

# Definir funciones de membresía
temperatura['fría'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['normal'] = fuzz.trimf(temperatura.universe, [20, 50, 80])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

humedad['seca'] = fuzz.trimf(humedad.universe, [0, 0, 50])
humedad['normal'] = fuzz.trimf(humedad.universe, [20, 50, 80])
humedad['húmeda'] = fuzz.trimf(humedad.universe, [50, 100, 100])

ventilador['apagado'] = fuzz.trimf(ventilador.universe, [0, 0, 50])
ventilador['medio'] = fuzz.trimf(ventilador.universe, [20, 50, 80])
ventilador['encendido'] = fuzz.trimf(ventilador.universe, [50, 100, 100])

# Reglas difusas
regla1 = ctrl.Rule(temperatura['fría'] | humedad['seca'], ventilador['apagado'])
regla2 = ctrl.Rule(temperatura['normal'] & humedad['normal'], ventilador['medio'])
regla3 = ctrl.Rule(temperatura['caliente'] | humedad['húmeda'], ventilador['encendido'])

# Crear el sistema de control difuso
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Entradas al sistema
sistema.input['temperatura'] = 35
sistema.input['humedad'] = 75

# Computar el resultado
sistema.compute()

# Mostrar el resultado
print(sistema.output['ventilador'])
ventilador.view(sim=sistema)
