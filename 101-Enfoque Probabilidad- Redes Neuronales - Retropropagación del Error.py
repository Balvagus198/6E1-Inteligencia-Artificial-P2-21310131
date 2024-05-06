# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np

# Función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Derivada de la función de activación ReLU
def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Función de activación Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función de activación Sigmoid
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Inicialización de pesos y sesgos
input_size = 3
hidden_size = 4
output_size = 2

weights_input_hidden = np.random.randn(input_size, hidden_size)
bias_hidden = np.zeros((1, hidden_size))
weights_hidden_output = np.random.randn(hidden_size, output_size)
bias_output = np.zeros((1, output_size))

# Datos de entrada y salida de ejemplo
X = np.array([[0.1, 0.2, 0.3]])
y = np.array([[0.4, 0.5]])

# Forward pass
hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
hidden_layer_output = relu(hidden_layer_input)
output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
output_layer_output = sigmoid(output_layer_input)

# Cálculo de la pérdida (error)
loss = np.sum((output_layer_output - y) ** 2) / 2
print(f"Pérdida inicial: {loss}")

# Backpropagation
output_error = output_layer_output - y
output_delta = output_error * sigmoid_derivative(output_layer_input)
hidden_error = np.dot(output_delta, weights_hidden_output.T)
hidden_delta = hidden_error * relu_derivative(hidden_layer_input)

# Actualización de pesos y sesgos
learning_rate = 0.1
weights_hidden_output -= np.dot(hidden_layer_output.T, output_delta) * learning_rate
bias_output -= np.sum(output_delta, axis=0, keepdims=True) * learning_rate
weights_input_hidden -= np.dot(X.T, hidden_delta) * learning_rate
bias_hidden -= np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

# Nuevo forward pass para verificar la reducción de la pérdida
hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
hidden_layer_output = relu(hidden_layer_input)
output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
output_layer_output = sigmoid(output_layer_input)

new_loss = np.sum((output_layer_output - y) ** 2) / 2
print(f"Nueva pérdida: {new_loss}")
