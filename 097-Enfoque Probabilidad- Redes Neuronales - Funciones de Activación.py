# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import tensorflow as tf
from tensorflow.keras.layers import Dense, Activation

# Definir una capa densa
layer = Dense(64)

# Llamar a la capa para tener una salida definida
inputs = tf.keras.Input(shape=(10,))
x = layer(inputs)

# Definir una capa de activación
activation_layer = Activation('relu')(x)

# Crear el modelo
model = tf.keras.Model(inputs=inputs, outputs=activation_layer)

# Mostrar la estructura del modelo
model.summary()
