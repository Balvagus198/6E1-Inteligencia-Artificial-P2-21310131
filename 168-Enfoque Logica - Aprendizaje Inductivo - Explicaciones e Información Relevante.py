# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Cargar el conjunto de datos de iris
iris = load_iris()
X = iris.data  # Características de las flores
y = iris.target  # Etiquetas de las clases de las flores

# Entrenar un clasificador de árbol de decisión
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Mostrar las características más importantes
importancias = clf.feature_importances_
caracteristicas = iris.feature_names

print("Características más importantes:")
for i, (caracteristica, importancia) in enumerate(zip(caracteristicas, importancias)):
    print(f"{i+1}. {caracteristica}: {importancia:.4f}")

# Mostrar el árbol de decisión
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()
