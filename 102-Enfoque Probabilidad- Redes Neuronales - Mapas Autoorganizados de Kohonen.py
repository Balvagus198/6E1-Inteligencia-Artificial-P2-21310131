# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

class SOM:
    def __init__(self, input_size, output_size, learning_rate=0.1, sigma=1.0):
        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.sigma = sigma
        self.weights = np.random.rand(output_size, input_size)

    def update_weights(self, input_vector):
        # Encuentra el nodo ganador (neurona con el peso más cercano al vector de entrada)
        winner_index = np.argmin(np.linalg.norm(self.weights - input_vector, axis=1))
        # Actualiza los pesos de los nodos vecinos
        for i in range(self.output_size):
            distance = np.abs(i - winner_index)
            influence = np.exp(-distance**2 / (2*self.sigma**2))
            self.weights[i] += self.learning_rate * influence * (input_vector - self.weights[i])

    def train(self, data, epochs):
        for epoch in range(epochs):
            for input_vector in data:
                self.update_weights(input_vector)

    def predict(self, input_vector):
        return np.argmin(np.linalg.norm(self.weights - input_vector, axis=1))

# Genera datos de ejemplo
np.random.seed(0)
data = np.random.rand(100, 2)  # 100 muestras de 2 dimensiones

# Crea y entrena el SOM
input_size = data.shape[1]
output_size = 5  # Tamaño de la cuadrícula del SOM (5x5)
som = SOM(input_size, output_size)
epochs = 100
som.train(data, epochs)

# Muestra el resultado
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c='b', label='Datos de entrada')
for i in range(output_size):
    plt.scatter(som.weights[i, 0], som.weights[i, 1], c='r', marker='x', label='Neurona')
plt.legend()
plt.title('Mapa Autoorganizado de Kohonen')
plt.show()
