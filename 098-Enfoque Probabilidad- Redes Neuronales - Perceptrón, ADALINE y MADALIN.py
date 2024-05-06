# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data[:, :2]  # Usar solo las dos primeras características para simplificar
y = (iris.target != 0) * 1  # Convertir a un problema de clasificación binaria

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el Perceptrón
perceptron = Perceptron()
perceptron.fit(X_train, y_train)

# Predecir con el conjunto de prueba
y_pred = perceptron.predict(X_test)

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del Perceptrón: {accuracy}")
