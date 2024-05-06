# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la Red Bayesiana
modelo = BayesianModel([('A', 'C'), ('B', 'C')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.8], [0.2]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(variable='C', variable_card=2,
                   values=[[0.9, 0.6, 0.7, 0.1], [0.1, 0.4, 0.3, 0.9]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Añadir los CPDs al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_c)

# Crear el objeto de eliminación de variables
eliminacion_variables = VariableElimination(modelo)

# Realizar inferencia
resultado = eliminacion_variables.query(variables=['C'], evidence={'A': 0})
print(resultado)
