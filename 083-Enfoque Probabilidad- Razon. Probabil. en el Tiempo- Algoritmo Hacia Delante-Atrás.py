# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# Definir la estructura de la red bayesiana dinámica
model = DBN()

# Definir los nodos y sus transiciones temporales
model.add_edges_from([
    (('Lluvia', 0), ('Lluvia', 1)),
    (('Lluvia', 0), ('Riego', 1)),
    (('Riego', 0), ('Riego', 1)),
    (('Lluvia', 1), ('Lluvia', 2)),
    (('Lluvia', 1), ('Riego', 2)),
    (('Riego', 1), ('Riego', 2))
])

# Definir las tablas de probabilidad condicional (CPDs)
cpd_lluvia_0 = TabularCPD(('Lluvia', 0), 2, [[0.5], [0.5]])
cpd_lluvia_1 = TabularCPD(('Lluvia', 1), 2, [[0.6, 0.3], [0.4, 0.7]], evidence=[('Lluvia', 0)], evidence_card=[2])
cpd_riego_0 = TabularCPD(('Riego', 0), 2, [[0.9], [0.1]])
cpd_riego_1 = TabularCPD(('Riego', 1), 2, [[0.7, 0.3], [0.3, 0.7]], evidence=[('Riego', 0)], evidence_card=[2])

# Añadir las CPDs al modelo
model.add_cpds(cpd_lluvia_0, cpd_lluvia_1, cpd_riego_0, cpd_riego_1)

# Crear un objeto de inferencia para el modelo
inference = DBNInference(model)

# Calcular la probabilidad hacia adelante y hacia atrás
forward_prob = inference.forward_backward([['Lluvia', 'Riego']], evidence={('Lluvia', 0): 0, ('Riego', 0): 1})

# Imprimir la probabilidad hacia adelante y hacia atrás
print("Probabilidad hacia adelante y hacia atrás:")
print(forward_prob)
