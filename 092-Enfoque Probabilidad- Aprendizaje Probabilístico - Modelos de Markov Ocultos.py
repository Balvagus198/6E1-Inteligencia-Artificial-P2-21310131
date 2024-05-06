# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from hmmlearn import hmm
import numpy as np

# Definir el modelo HMM
model = hmm.MultinomialHMM(n_components=3)  # Número de estados ocultos

# Definir las probabilidades de transición entre estados ocultos
model.transmat_ = np.array([[0.7, 0.2, 0.1],
                             [0.3, 0.5, 0.2],
                             [0.1, 0.3, 0.6]])

# Definir las probabilidades de emisión de los estados ocultos
model.emissionprob_ = np.array([[0.6, 0.4],
                                 [0.3, 0.7],
                                 [0.8, 0.2]])

# Definir la secuencia de observaciones
X = np.array([[0, 1, 0, 1, 0, 0]]).T

# Ajustar el modelo a la secuencia de observaciones
model.fit(X)

# Predecir la secuencia de estados ocultos más probable
predicted_states = model.predict(X)

print("Secuencia de observaciones:", X.flatten())
print("Secuencia de estados ocultos predicha:", predicted_states)
