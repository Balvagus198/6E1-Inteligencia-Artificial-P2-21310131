# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Crear el modelo bayesiano
modelo = BayesianModel([('A', 'B'), ('C', 'B')])

# Definir las probabilidades condicionales
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.8], [0.2]])
cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.7], [0.3]])
cpd_b = TabularCPD(variable='B', variable_card=2, 
                   values=[[0.9, 0.6, 0.7, 0.1], 
                           [0.1, 0.4, 0.3, 0.9]],
                   evidence=['A', 'C'], evidence_card=[2, 2])

# Agregar las probabilidades condicionales al modelo
modelo.add_cpds(cpd_a, cpd_c, cpd_b)

# Verificar la consistencia del modelo
print("¿El modelo es consistente?", modelo.check_model())

# Obtener la distribución de probabilidad conjunta
joint_prob = cpd_a * cpd_c * cpd_b
print("Distribución de probabilidad conjunta:")
print(joint_prob)

# Calcular la probabilidad condicional P(B | A=1, C=0)
inferencia = modelo.infer_query(variables=['B'], evidence={'A': 1, 'C': 0})
print("P(B | A=1, C=0) =", inferencia['B'])

# Calcular la probabilidad conjunta P(A=1, B=0, C=1)
prob_conjunta = joint_prob.values[1, 0, 1]
print("P(A=1, B=0, C=1) =", prob_conjunta)
