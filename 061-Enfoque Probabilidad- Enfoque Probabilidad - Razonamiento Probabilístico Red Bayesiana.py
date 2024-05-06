# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Crear una Red Bayesiana
modelo_bayesiano = BayesianModel([('Lluvia', 'Cesped'), ('Riego', 'Cesped')])

# Definir las Tablas de Probabilidad Condicional (CPDs)
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, values=[[0.2], [0.8]])
cpd_riego = TabularCPD(variable='Riego', variable_card=2, values=[[0.4], [0.6]])
cpd_cesped = TabularCPD(variable='Cesped', variable_card=2, 
                         values=[[0.9, 0.6, 0.7, 0.1],
                                 [0.1, 0.4, 0.3, 0.9]],
                         evidence=['Lluvia', 'Riego'], evidence_card=[2, 2])

# Asignar las Tablas de CPD al modelo Bayesiano
modelo_bayesiano.add_cpds(cpd_lluvia, cpd_riego, cpd_cesped)

# Verificar si el modelo es válido y consistente
print("El modelo es válido y consistente?", modelo_bayesiano.check_model())

# Realizar inferencia utilizando VariableElimination
inferencia = VariableElimination(modelo_bayesiano)

# Calcular la probabilidad condicional P(Césped | Lluvia=1, Riego=0)
resultado = inferencia.query(variables=['Cesped'], evidence={'Lluvia': 1, 'Riego': 0})
print("Probabilidad P(Césped | Lluvia=1, Riego=0):")
print(resultado)
