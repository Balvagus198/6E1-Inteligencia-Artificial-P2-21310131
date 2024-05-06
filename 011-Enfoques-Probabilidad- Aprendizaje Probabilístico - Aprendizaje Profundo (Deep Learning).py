import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Cargar y preparar el conjunto de datos Fashion MNIST
(x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = keras.datasets.fashion_mnist.load_data()
x_entrenamiento = x_entrenamiento.astype("float32") / 255.0
x_prueba = x_prueba.astype("float32") / 255.0

# Crear el modelo de red neuronal convolucional (CNN)
modelo = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dropout(0.5),
    layers.Dense(10, activation="softmax"),
])

# Compilar el modelo
modelo.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Entrenar el modelo
modelo.fit(x_entrenamiento.reshape(-1, 28, 28, 1), y_entrenamiento, batch_size=128, epochs=5, validation_split=0.1)

# Evaluar el modelo en el conjunto de prueba
puntuacion = modelo.evaluate(x_prueba.reshape(-1, 28, 28, 1), y_prueba)
print("Pérdida en el conjunto de prueba:", puntuacion[0])
print("Precisión en el conjunto de prueba:", puntuacion[1])
