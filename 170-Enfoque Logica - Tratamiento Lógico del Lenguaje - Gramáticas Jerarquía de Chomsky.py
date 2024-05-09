# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk
from nltk import CFG

# Definir una gramática CFG
gramatica = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'el' | 'la'
    N -> 'perro' | 'gato' | 'pelota'
    V -> 'persigue' | 'salta'
    P -> 'sobre' | 'en'
""")

# Crear un analizador sintáctico
analizador = nltk.ChartParser(gramatica)

# Oración de entrada
oracion = "el perro persigue la pelota en el jardín"

# Tokenizar la oración
tokens = oracion.split()

# Analizar la oración sintácticamente
for arbol in analizador.parse(tokens):
    print(arbol)
    arbol.pretty_print()
