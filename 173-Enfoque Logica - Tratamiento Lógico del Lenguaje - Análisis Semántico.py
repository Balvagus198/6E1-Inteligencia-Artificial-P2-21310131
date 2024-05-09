# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import spacy

# Cargar el modelo de lenguaje en español
nlp = spacy.load("es_core_news_sm")

# Oración de entrada
oracion = "El gato persigue al ratón por el jardín."

# Procesar la oración con spaCy
doc = nlp(oracion)

# Mostrar las entidades nombradas en la oración
print("Entidades nombradas:")
for entidad in doc.ents:
    print(entidad.text, entidad.label_)

# Mostrar las dependencias sintácticas de las palabras
print("\nDependencias sintácticas:")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_)

# Mostrar el análisis semántico de las palabras
print("\nAnálisis semántico:")
for token in doc:
    print(token.text, token.pos_, token.tag_, token.lemma_)
