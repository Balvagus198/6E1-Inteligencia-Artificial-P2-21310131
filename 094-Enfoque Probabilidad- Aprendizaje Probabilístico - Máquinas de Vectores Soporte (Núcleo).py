# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo para clasificación
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y ajustar el modelo SVM con núcleo probabilístico
svm = SVC(kernel='rbf', probability=True, random_state=42)
svm.fit(X_train, y_train)

# Calcular las probabilidades de pertenencia a cada clase para los datos de prueba
probabilities = svm.predict_proba(X_test)

# Graficar los datos y las regiones de decisión del modelo
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolors='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('SVM con Núcleo Probabilístico')
plt.colorbar(label='Class')
plt.show()
