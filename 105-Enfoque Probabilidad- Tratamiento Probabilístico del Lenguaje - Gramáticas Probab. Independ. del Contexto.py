# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk
from nltk import PCFG, ViterbiParser
from nltk.corpus import treebank

# Descargar el corpus de entrenamiento (en este caso, usaremos el corpus Penn Treebank)
nltk.download('treebank')

# Obtener oraciones etiquetadas del corpus Treebank
sentences = treebank.parsed_sents()

# Entrenar un modelo PCFG con las oraciones etiquetadas
pcfg = PCFG.from_train(sentences)

# Definir una oración de ejemplo para analizar con el modelo
example_sentence = "The dog barks loudly"

# Crear un analizador Viterbi con el modelo PCFG entrenado
parser = ViterbiParser(pcfg)

# Analizar la oración de ejemplo y obtener el árbol de análisis más probable
parsed_tree = list(parser.parse(example_sentence.split()))[0]

# Imprimir el árbol de análisis
print(parsed_tree)
