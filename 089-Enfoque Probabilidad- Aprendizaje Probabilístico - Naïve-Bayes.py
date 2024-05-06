# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# Cargar el conjunto de datos de noticias 20newsgroups
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
train_data = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
test_data = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)

# Crear un modelo Naïve Bayes utilizando un pipeline con CountVectorizer y MultinomialNB
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Entrenar el modelo con los datos de entrenamiento
model.fit(train_data.data, train_data.target)

# Predecir las etiquetas de las noticias de prueba
predicted_labels = model.predict(test_data.data)

# Calcular la precisión del modelo
accuracy = accuracy_score(test_data.target, predicted_labels)
print("Precisión del modelo Naïve Bayes:", accuracy)

# Mostrar un informe de clasificación detallado
print("\nInforme de Clasificación:")
print(classification_report(test_data.target, predicted_labels, target_names=test_data.target_names))
