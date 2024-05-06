# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import pymc3 as pm

# Definir el modelo bayesiano (ejemplo simplificado)
with pm.Model() as modelo:
    # Parámetro a estimar
    theta = pm.Beta('theta', alpha=2, beta=2)  # Distribución a priori Beta(2, 2)

    # Datos observados
    observaciones = pm.Bernoulli('observaciones', p=theta, observed=[1, 1, 0, 1, 0])

    # Realizar muestreo MCMC
    trace = pm.sample(1000, tune=1000)  # Generar 1000 muestras, con 1000 pasos de "tuning"

# Analizar resultados
pm.summary(trace)
