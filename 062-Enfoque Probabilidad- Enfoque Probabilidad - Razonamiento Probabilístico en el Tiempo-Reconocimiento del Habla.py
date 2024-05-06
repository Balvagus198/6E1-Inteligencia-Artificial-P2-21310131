# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from hmmlearn import hmm
import numpy as np

# Definir los estados ocultos del HMM (representando fonemas en este ejemplo)
estados_ocultos = ['Fonema1', 'Fonema2', 'Fonema3']
num_estados = len(estados_ocultos)

# Definir los observables (representando características del habla en este ejemplo)
observables = ['Caracteristica1', 'Caracteristica2', 'Caracteristica3']
num_observables = len(observables)

# Crear el modelo HMM
modelo_hmm = hmm.MultinomialHMM(n_components=num_estados)

# Definir las probabilidades de inicio
modelo_hmm.startprob_ = np.array([0.6, 0.3, 0.1])

# Definir las matrices de transición entre estados
modelo_hmm.transmat_ = np.array([[0.7, 0.2, 0.1],
                                  [0.3, 0.5, 0.2],
                                  [0.1, 0.3, 0.6]])

# Definir las probabilidades de emisión de observables para cada estado
probabilidades_emision = np.array([[0.6, 0.3, 0.1],
                                   [0.2, 0.5, 0.3],
                                   [0.1, 0.4, 0.5]])
modelo_hmm.emissionprob_ = probabilidades_emision

# Generar secuencia de observables simulada
longitud_secuencia = 10
secuencia_observables, secuencia_estados = modelo_hmm.sample(n_samples=longitud_secuencia)

# Imprimir la secuencia generada
print("Secuencia de Observables:")
print(secuencia_observables)
print("Secuencia de Estados:")
print(secuencia_estados)

# Ajustar el modelo HMM a datos reales (si los tienes disponibles)
# datos_entrenamiento = [[observaciones1], [observaciones2], ...]
# modelo_hmm.fit(datos_entrenamiento)

# Realizar inferencia para determinar la secuencia de estados más probable
# secuencia_mas_probable = modelo_hmm.predict(secuencia_observables)
# print("Secuencia de Estados Más Probable:")
# print(secuencia_mas_probable)
