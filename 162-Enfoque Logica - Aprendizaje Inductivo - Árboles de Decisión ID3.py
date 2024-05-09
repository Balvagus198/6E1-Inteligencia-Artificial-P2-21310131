# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# Cargar el conjunto de datos de iris
iris = load_iris()
X = iris.data  # Características de las flores
y = iris.target  # Etiquetas de las clases de las flores

# Crear un clasificador de árbol de decisión utilizando el algoritmo ID3
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X, y)

# Mostrar la estructura del árbol de decisión generado por ID3
tree_rules = export_text(clf, feature_names=iris.feature_names)
print("Árbol de Decisión ID3:")
print(tree_rules)
