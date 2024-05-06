# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from filterpy.monte_carlo import systematic_resample
import numpy as np

def predict(particles, u, std):
    """Función de predicción del filtro de partículas."""
    particles += u + (np.random.randn(len(particles)) * std)
    return particles

def update(particles, weights, z, R):
    """Función de actualización del filtro de partículas."""
    weights *= np.exp(-0.5 * ((particles - z) / R)**2)
    weights += 1.e-300  # para evitar la división por cero
    weights /= sum(weights)  # normalizar los pesos
    return weights

def estimate(particles, weights):
    """Estimar el estado basado en las partículas y sus pesos."""
    return np.sum(particles * weights)

# Definir parámetros
np.random.seed(0)
num_particles = 1000
std_movement = 2.0  # desviación estándar del movimiento
std_measurement = 1.0  # desviación estándar de la medición

# Generar partículas y pesos iniciales
particles = np.random.randn(num_particles)
weights = np.ones(num_particles) / num_particles

# Simular el movimiento y las mediciones
movements = np.random.normal(1, std_movement, size=100)
measurements = np.random.normal(0, std_measurement, size=100)

# Aplicar el filtro de partículas
for movement, measurement in zip(movements, measurements):
    particles = predict(particles, movement, std_movement)
    weights = update(particles, weights, measurement, std_measurement)
    particles = systematic_resample(particles, weights)  # Corregir aquí

# Estimar el estado final
estimated_state = estimate(particles, weights)
print("Estado estimado:", estimated_state)
