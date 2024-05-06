# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
from sklearn.mixture import GaussianMixture

# Generar datos de ejemplo con dos componentes gaussianas
np.random.seed(42)
n_samples = 1000
X = np.concatenate([np.random.normal(0, 1, int(0.7 * n_samples)),
                    np.random.normal(5, 1, int(0.3 * n_samples))]).reshape(-1, 1)

# Inicializar y ajustar el modelo Gaussian Mixture con dos componentes
model = GaussianMixture(n_components=2, random_state=42)
model.fit(X)

# Imprimir los parámetros estimados del modelo
print("Media de cada componente:", model.means_)
print("Covarianza de cada componente:", model.covariances_)
print("Peso de cada componente:", model.weights_)

# Predecir las etiquetas de las muestras
predicted_labels = model.predict(X)
