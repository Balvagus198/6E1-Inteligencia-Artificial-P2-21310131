# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk
from nltk.translate import IBMModel1
from nltk.tokenize import word_tokenize

# Texto en inglés
texto_en = "The cat is on the mat"

# Texto en español (traducción aproximada)
texto_es = "El gato está en la alfombra"

# Tokenización de textos
palabras_en = word_tokenize(texto_en.lower())
palabras_es = word_tokenize(texto_es.lower())

# Entrenamiento del modelo de traducción
ibm_model = IBMModel1(list(zip(palabras_en, palabras_es)), 5)

# Traducción de texto en inglés a español
traduccion_es = [ibm_model.best_translation(word) for word in palabras_en]

# Imprimir texto traducido
print("Texto original en inglés:", texto_en)
print("Texto traducido al español:", ' '.join(traduccion_es))
