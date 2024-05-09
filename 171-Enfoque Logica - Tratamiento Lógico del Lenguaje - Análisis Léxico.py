# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk

# Oración de entrada
oracion = "El gato persigue al ratón por el jardín."

# Tokenizar la oración
tokens = nltk.word_tokenize(oracion)

# Mostrar los tokens generados
print("Tokens:")
print(tokens)

# Obtener información léxica de los tokens
info_lexica = [(token, nltk.pos_tag([token])) for token in tokens]

# Mostrar la información léxica
print("\nInformación léxica:")
for token, info in info_lexica:
    print(f"{token}: {info}")
