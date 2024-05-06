# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# Cargar el conjunto de datos MNIST de dígitos escritos a mano
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalizar los datos
X_train, X_test = X_train / 255.0, X_test / 255.0

# Crear el modelo de red neuronal profunda
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Capa de aplanado para convertir imágenes 28x28 en vectores 1D
    Dense(128, activation='relu'),  # Capa densa con 128 neuronas y función de activación ReLU
    Dense(10, activation='softmax') # Capa densa de salida con 10 neuronas y función de activación Softmax para clasificación
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=5)

# Evaluar el modelo con los datos de prueba
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Accuracy: {test_acc}')
