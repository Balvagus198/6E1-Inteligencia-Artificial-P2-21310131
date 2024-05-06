import numpy as np
import tensorflow as tf
from tensorflow import keras

# Cargar y preparar el conjunto de datos Fashion MNIST
(x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = keras.datasets.fashion_mnist.load_data()
x_entrenamiento = x_entrenamiento.reshape((x_entrenamiento.shape[0], -1)) / 255.0
x_prueba = x_prueba.reshape((x_prueba.shape[0], -1)) / 255.0

# Crear el modelo de red neuronal multicapa (MLP)
modelo = keras.Sequential([
    keras.layers.Input(shape=(784,)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])

# Compilar el modelo
modelo.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(x_entrenamiento, y_entrenamiento, epochs=5, batch_size=128, validation_split=0.1)

# Evaluar el modelo en el conjunto de prueba
puntuacion = modelo.evaluate(x_prueba, y_prueba)
print("Pérdida en el conjunto de prueba:", puntuacion[0])
print("Precisión en el conjunto de prueba:", puntuacion[1])
