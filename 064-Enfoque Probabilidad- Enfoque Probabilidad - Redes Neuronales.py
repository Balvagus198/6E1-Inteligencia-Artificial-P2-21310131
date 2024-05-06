# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pymc3 as pm

# Generar datos de ejemplo
np.random.seed(0)
X_train = np.random.randn(100, 2)
y_train = np.random.randint(0, 2, size=100)

# Crear una red neuronal simple
model = Sequential([
    Dense(32, input_shape=(2,), activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar la red neuronal
model.fit(X_train, y_train, epochs=50, verbose=0)

# Crear un modelo probabilístico con PyMC3
with pm.Model() as bayesian_model:
    # Parámetros del modelo
    weights = pm.Normal('weights', mu=0, sd=1, shape=(2, 1))
    bias = pm.Normal('bias', mu=0, sd=1)

    # Función logística
    logits = pm.math.dot(X_train, weights) + bias
    probability = pm.Deterministic('probability', pm.math.sigmoid(logits))

    # Likelihood
    y_observed = pm.Bernoulli('y_observed', p=probability, observed=y_train)

    # Muestreo de la posterior
    trace = pm.sample(1000, tune=1000, chains=1)

# Obtener las medias de los parámetros de la red neuronal
nn_weights = model.layers[0].get_weights()[0]
nn_bias = model.layers[0].get_weights()[1]

# Obtener las medias de los parámetros del modelo bayesiano
bayesian_weights = trace['weights'].mean(axis=0)
bayesian_bias = trace['bias'].mean()

# Comparar los resultados
print("Parámetros de la red neuronal:")
print("Pesos:", nn_weights)
print("Bias:", nn_bias)
print("\nParámetros del modelo bayesiano:")
print("Pesos:", bayesian_weights)
print("Bias:", bayesian_bias)
