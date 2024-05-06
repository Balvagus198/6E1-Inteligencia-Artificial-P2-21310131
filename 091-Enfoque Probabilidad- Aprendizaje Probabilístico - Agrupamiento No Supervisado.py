# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generar datos de ejemplo con 3 clusters
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)

# Inicializar y ajustar el modelo Gaussian Mixture con 3 componentes
model = GaussianMixture(n_components=3, random_state=42)
model.fit(X)

# Obtener las etiquetas de los clusters asignadas por el modelo
predicted_labels = model.predict(X)

# Graficar los datos y los clusters asignados por el modelo
plt.scatter(X[:, 0], X[:, 1], c=predicted_labels, cmap='viridis', marker='o', edgecolors='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Agrupamiento No Supervisado con Gaussian Mixture Model')
plt.colorbar(label='Cluster')
plt.show()
