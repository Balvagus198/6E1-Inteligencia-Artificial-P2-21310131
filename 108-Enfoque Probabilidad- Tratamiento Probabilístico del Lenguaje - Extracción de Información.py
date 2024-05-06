# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Ejemplo de texto
texto = """
La Inteligencia Artificial (IA) es la simulación de procesos inteligentes por parte de máquinas, 
especialmente sistemas informáticos. Estos procesos incluyen el aprendizaje (la adquisición de información 
y reglas para usarla), el razonamiento (usar reglas para llegar a conclusiones aproximadas o definitivas) 
y la autocorrección.
"""

# Tokenización de oraciones y palabras
oraciones = sent_tokenize(texto)
palabras = [word_tokenize(oracion) for oracion in oraciones]

# Etiquetado gramatical (POS tagging)
oraciones_etiquetadas = [pos_tag(palabra) for palabra in palabras]

# Identificación de entidades con nombre (NER)
oraciones_ner = [ne_chunk(oracion) for oracion in oraciones_etiquetadas]

# Imprimir entidades con nombre
for oracion in oraciones_ner:
    for chunk in oracion:
        if hasattr(chunk, 'label'):
            print(chunk.label(), ' '.join(c[0] for c in chunk))
