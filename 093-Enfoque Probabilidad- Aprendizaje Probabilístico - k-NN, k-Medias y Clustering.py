# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Generar datos de ejemplo con 3 clusters
X, y = make_blobs(n_samples=300, centers=3, random_state=42)

# Inicializar y ajustar el modelo k-NN con k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Graficar los datos y las regiones de decisión del modelo
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolors='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('k-Nearest Neighbors (k-NN)')
plt.colorbar(label='Cluster')
plt.show()
