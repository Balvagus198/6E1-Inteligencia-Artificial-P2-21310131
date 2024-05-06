# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Crear una Red Bayesiana
modelo_bayesiano = BayesianModel([('D', 'G'), ('I', 'G'), ('G', 'L'), ('I', 'S')])

# Definir las Tablas de Probabilidad Condicional (CPDs)
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6, 0.4]])
cpd_i = TabularCPD(variable='I', variable_card=2, values=[[0.7, 0.3]])
cpd_g = TabularCPD(variable='G', variable_card=3, 
                   values=[[0.3, 0.05, 0.9,  0.5],
                           [0.4, 0.25, 0.08, 0.3],
                           [0.3, 0.7,  0.02, 0.2]],
                   evidence=['D', 'I'], evidence_card=[2, 2])
cpd_l = TabularCPD(variable='L', variable_card=2, 
                   values=[[0.1, 0.4, 0.99],
                           [0.9, 0.6, 0.01]],
                   evidence=['G'], evidence_card=[3])
cpd_s = TabularCPD(variable='S', variable_card=2, 
                   values=[[0.95, 0.2],
                           [0.05, 0.8]],
                   evidence=['I'], evidence_card=[2])

# Asignar las Tablas de CPD al modelo Bayesiano
modelo_bayesiano.add_cpds(cpd_d, cpd_i, cpd_g, cpd_l, cpd_s)

# Verificar si el modelo es válido y consistente
print("El modelo es válido y consistente?", modelo_bayesiano.check_model())

# Realizar inferencia utilizando VariableElimination
inferencia = VariableElimination(modelo_bayesiano)

# Calcular la probabilidad condicional P(L | D=1, I=0)
resultado = inferencia.query(variables=['L'], evidence={'D': 1, 'I': 0})
print("Probabilidad P(L | D=1, I=0):")
print(resultado)
