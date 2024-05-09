# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk
from nltk import CFG

# Definir una gramática CFG para estructuras causales simples
gramatica_causal = CFG.fromstring("""
    S -> Causa VP
    Causa -> 'debido a' | 'por causa de' | 'a causa de'
    VP -> V S | V NP
    V -> 'provocó' | 'ocasionó' | 'generó'
    NP -> Det N | Det N PP
    Det -> 'el' | 'la'
    N -> 'accidente' | 'incidente' | 'problema'
    PP -> P NP
    P -> 'en' | 'con'
""")

# Crear un analizador sintáctico para la gramática causal
analizador_causal = nltk.ChartParser(gramatica_causal)

# Oración de ejemplo
oracion_causal = "El accidente provocó problemas en el tráfico."

# Tokenizar la oración
tokens_causal = nltk.word_tokenize(oracion_causal)

# Realizar análisis sintáctico causal
for arbol_causal in analizador_causal.parse(tokens_causal):
    print(arbol_causal)
    arbol_causal.pretty_print()
