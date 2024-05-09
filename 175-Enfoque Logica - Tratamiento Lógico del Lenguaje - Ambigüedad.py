# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""

import nltk

# Definir una gramática CFG ambigua
gramatica_ambigua = nltk.CFG.fromstring("""
    S -> NP VP | VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'el' | 'la'
    N -> 'banco' | 'río'
    V -> 'salió' | 'corrió'
    P -> 'por'
""")

# Crear un analizador sintáctico para la gramática ambigua
analizador_ambiguo = nltk.ChartParser(gramatica_ambigua)

# Oración de ejemplo ambigua
oracion_ambigua = "El banco salió corriendo por el río."

# Tokenizar la oración
tokens_ambiguos = nltk.word_tokenize(oracion_ambigua)

# Realizar análisis sintáctico ambiguo
for arbol_ambiguo in analizador_ambiguo.parse(tokens_ambiguos):
    print(arbol_ambiguo)
    arbol_ambiguo.pretty_print()
