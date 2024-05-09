# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables lingüísticas y universos de discurso
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
velocidad = ctrl.Antecedent(np.arange(0, 101, 1), 'velocidad')
apertura_valvula = ctrl.Consequent(np.arange(0, 101, 1), 'apertura_valvula')

# Definir funciones de membresía
temperatura['baja'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['media'] = fuzz.trimf(temperatura.universe, [0, 50, 100])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

velocidad['baja'] = fuzz.trimf(velocidad.universe, [0, 0, 50])
velocidad['media'] = fuzz.trimf(velocidad.universe, [0, 50, 100])
velocidad['alta'] = fuzz.trimf(velocidad.universe, [50, 100, 100])

apertura_valvula['pequeña'] = fuzz.trimf(apertura_valvula.universe, [0, 0, 50])
apertura_valvula['mediana'] = fuzz.trimf(apertura_valvula.universe, [0, 50, 100])
apertura_valvula['grande'] = fuzz.trimf(apertura_valvula.universe, [50, 100, 100])

# Reglas difusas
rule1 = ctrl.Rule(temperatura['baja'] & velocidad['baja'], apertura_valvula['grande'])
rule2 = ctrl.Rule(temperatura['media'] & velocidad['media'], apertura_valvula['mediana'])
rule3 = ctrl.Rule(temperatura['alta'] & velocidad['alta'], apertura_valvula['pequeña'])

# Sistema de control
sistema_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Entradas al sistema
sistema.input['temperatura'] = 75
sistema.input['velocidad'] = 30

# Computar el resultado
sistema.compute()

# Obtener la salida
print("Apertura de la válvula:", sistema.output['apertura_valvula'])
apertura_valvula.view(sim=sistema)
