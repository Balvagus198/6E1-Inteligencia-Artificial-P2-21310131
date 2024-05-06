# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from hmmlearn import hmm

# Definir las observaciones (ejemplo simplificado)
observaciones = [[0], [1], [0], [1], [0], [1]]

# Definir el modelo HMM
modelo_hmm = hmm.GaussianHMM(n_components=2, covariance_type="full")

# Entrenar el modelo con las observaciones
modelo_hmm.fit(observaciones)

# Predecir la secuencia de estados ocultos
secuencia_estados, _ = modelo_hmm.decode(observaciones)

# Mostrar la secuencia de estados predicha
print("Secuencia de estados predicha:", secuencia_estados)
