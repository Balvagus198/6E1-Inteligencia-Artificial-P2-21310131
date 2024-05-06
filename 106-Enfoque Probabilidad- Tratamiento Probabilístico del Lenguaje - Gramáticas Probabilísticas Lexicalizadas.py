# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk
from nltk import CFG
from nltk.parse import ViterbiParser
from nltk.tokenize import word_tokenize

# Definir una gramática probabilística lexicalizada
grammar = CFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | V [0.3]
    NP -> Det N [0.5] | NP PP [0.3] | 'John' [0.1] | 'Mary' [0.1]
    PP -> P NP [1.0]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'man' [0.5] | 'dog' [0.3] | 'cat' [0.2]
    V -> 'chased' [0.8] | 'saw' [0.2]
    P -> 'in' [0.6] | 'on' [0.4]
""")

# Crear un analizador Viterbi con la gramática probabilística lexicalizada
parser = ViterbiParser(grammar)

# Definir una oración de ejemplo para analizar
example_sentence = "the man saw a dog in the park"

# Tokenizar la oración
tokens = word_tokenize(example_sentence)

# Analizar la oración tokenizada y obtener el árbol de análisis más probable
parsed_tree = list(parser.parse(tokens))[0]

# Imprimir el árbol de análisis
print(parsed_tree)
