# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Definir las variables de la Red Bayesiana
variables = ['A', 'B']

# Definir la estructura de la Red Bayesiana (grafo)
estructura = [('A', 'B')]

# Crear el objeto de la Red Bayesiana
red_bayesiana = BayesianModel(estructura)

# Definir las distribuciones de probabilidad condicional (CPDs) de cada nodo
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.2, 0.7], [0.8, 0.3]], evidence=['A'], evidence_card=[2])

# Añadir los CPDs a la Red Bayesiana
red_bayesiana.add_cpds(cpd_A, cpd_B)

# Verificar si la Red Bayesiana es válida
es_valida = red_bayesiana.check_model()
print("¿Es la Red Bayesiana válida?", es_valida)

# Mostrar la estructura de la Red Bayesiana
print("Estructura de la Red Bayesiana:")
print(red_bayesiana.edges())
