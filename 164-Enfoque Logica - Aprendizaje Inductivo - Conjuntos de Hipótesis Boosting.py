# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Cargar el conjunto de datos de iris
iris = load_iris()
X = iris.data  # Características de las flores
y = iris.target  # Etiquetas de las clases de las flores

# Dividir el conjunto de datos en datos de entrenamiento y datos de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear un clasificador AdaBoost
boosting_clf = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=1), n_estimators=50, random_state=42)

# Entrenar el clasificador Boosting con los datos de entrenamiento
boosting_clf.fit(X_train, y_train)

# Realizar predicciones en los datos de prueba
y_pred = boosting_clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")
