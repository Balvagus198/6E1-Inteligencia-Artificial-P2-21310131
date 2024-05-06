# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar datos linealmente separables
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el Perceptrón
perceptron = Perceptron()
perceptron.fit(X_train, y_train)

# Predecir con el conjunto de prueba
y_pred = perceptron.predict(X_test)

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del Perceptrón en datos linealmente separables: {accuracy}")
