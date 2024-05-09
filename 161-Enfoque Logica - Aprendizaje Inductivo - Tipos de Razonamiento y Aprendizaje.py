# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos de flores iris
iris = load_iris()
X = iris.data  # Características de las flores
y = iris.target  # Etiquetas de las clases de las flores

# Dividir el conjunto de datos en datos de entrenamiento y datos de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear un clasificador KNN (vecinos más cercanos) con k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenar el clasificador con los datos de entrenamiento
knn.fit(X_train, y_train)

# Realizar predicciones en los datos de prueba
y_pred = knn.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Visualizar el razonamiento inductivo mediante un gráfico de dispersión
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='viridis')
plt.xlabel('Longitud del sépalo')
plt.ylabel('Anchura del sépalo')
plt.title('Clasificación de flores iris por KNN')
plt.colorbar(label='Clase')
plt.show()
