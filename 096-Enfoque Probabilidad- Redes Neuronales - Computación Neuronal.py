# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Definir la arquitectura de la red neuronal
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),  # Capa oculta con 64 neuronas y activación ReLU
    Dense(1, activation='sigmoid')  # Capa de salida con 1 neurona y activación Sigmoide para problemas de clasificación binaria
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',  # Función de pérdida para clasificación binaria
              metrics=['accuracy'])  # Métrica a optimizar durante el entrenamiento

# Mostrar la estructura del modelo
model.summary()
