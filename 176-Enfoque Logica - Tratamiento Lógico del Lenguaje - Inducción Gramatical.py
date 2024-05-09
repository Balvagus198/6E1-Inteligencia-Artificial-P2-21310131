# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk
from nltk import Nonterminal
from nltk import induce_pcfg
from nltk.corpus import treebank

# Obtener oraciones etiquetadas del corpus Treebank
corpus = treebank.parsed_sents()

# Filtrar oraciones de longitud menor o igual a 10 palabras
oraciones = [oracion for oracion in corpus if len(oracion.leaves()) <= 10]

# Obtener la producción más frecuente de cada oración
producciones = [produccion for oracion in oraciones for produccion in oracion.productions()]

# Inducir la gramática probabilística a partir de las producciones
gramatica_pcfg = induce_pcfg(Nonterminal('S'), producciones)

# Mostrar las reglas gramaticales inducidas
for produccion in gramatica_pcfg.productions():
    print(produccion)
