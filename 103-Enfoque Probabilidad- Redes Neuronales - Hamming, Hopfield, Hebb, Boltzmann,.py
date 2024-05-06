# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
import numpy as np

class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        num_patterns = len(patterns)
        for pattern in patterns:
            pattern = pattern.reshape((1, -1))
            self.weights += np.dot(pattern.T, pattern)
        np.fill_diagonal(self.weights, 0)
        self.weights /= num_patterns

    def recall(self, input_pattern, max_iter=100):
        input_pattern = input_pattern.reshape((1, -1))
        for _ in range(max_iter):
            old_pattern = input_pattern.copy()
            input_pattern = np.sign(np.dot(input_pattern, self.weights))
            if np.array_equal(input_pattern, old_pattern):
                break
        return input_pattern

# Crear y entrenar la red de Hopfield
patterns = np.array([[1, -1, 1, -1], [-1, 1, -1, 1], [1, 1, 1, 1]])
hopfield_net = HopfieldNetwork(num_neurons=patterns.shape[1])
hopfield_net.train(patterns)

# Recuperar un patrón almacenado
input_pattern = np.array([[1, -1, 1, -1]])
retrieved_pattern = hopfield_net.recall(input_pattern)

print("Patrón de entrada:")
print(input_pattern)
print("Patrón recuperado:")
print(retrieved_pattern)

