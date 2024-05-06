# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize

# Descargar recursos necesarios de NLTK
nltk.download('punkt')

# Texto de ejemplo
texto = "El tratamiento probabilístico del lenguaje es importante para analizar textos."

# Tokenización del texto en palabras
palabras = word_tokenize(texto)

# Calcular la frecuencia de las palabras
frecuencia = FreqDist(palabras)

# Calcular la probabilidad de cada palabra
total_palabras = sum(frecuencia.values())
probabilidades = {palabra: frecuencia[palabra] / total_palabras for palabra in frecuencia}

# Mostrar las probabilidades de las palabras
for palabra, probabilidad in probabilidades.items():
    print(f"Palabra: {palabra}, Probabilidad: {probabilidad}")
