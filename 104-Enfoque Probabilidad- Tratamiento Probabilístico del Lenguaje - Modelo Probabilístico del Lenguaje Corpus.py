# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import LidstoneProbDist

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('gutenberg')

# Cargar el corpus de texto (usaremos el corpus de Gutenberg como ejemplo)
corpus = nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')

# Tokenizar el texto en palabras
words = word_tokenize(corpus)

# Crear un modelo de frecuencia de palabras usando Lidstone smoothing
vocab = set(words)
freq_dist = nltk.FreqDist(words)
total_words = len(words)
prob_dist = LidstoneProbDist(freq_dist, 0.1, bins=len(vocab))

# Función para calcular la probabilidad de una oración dada
def sentence_probability(sentence):
    sentence_words = word_tokenize(sentence)
    prob = 1
    for word in sentence_words:
        prob *= prob_dist.prob(word)
    return prob

# Ejemplo de uso
test_sentence = "To be or not to be"
probability = sentence_probability(test_sentence)
print(f"La probabilidad de la oración '{test_sentence}' es: {probability}")
