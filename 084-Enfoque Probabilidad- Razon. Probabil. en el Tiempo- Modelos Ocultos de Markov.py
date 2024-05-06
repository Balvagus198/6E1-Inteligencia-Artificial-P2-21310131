# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from hmmlearn import hmm

# Definir el modelo HMM
model = hmm.MultinomialHMM(n_components=2)

# Definir la matriz de transición
model.transmat_ = [[0.7, 0.3],
                   [0.4, 0.6]]

# Definir la matriz de emisión
model.emissionprob_ = [[0.1, 0.4, 0.5],
                       [0.6, 0.3, 0.1]]

# Definir la distribución inicial
model.startprob_ = [0.8, 0.2]

# Definir el número de ensayos (n_trials)
n_trials = 100

# Generar secuencia de observaciones y estados ocultos
import numpy as np
np.random.seed(42)
X, Z = model.sample(n_trials)

# Ajustar el modelo a los datos observados
model.fit(X)

# Predecir la secuencia de estados ocultos
predicted_states = model.predict(X)

# Imprimir la secuencia de estados ocultos
print("Secuencia de estados ocultos predicha:")
print(predicted_states)
