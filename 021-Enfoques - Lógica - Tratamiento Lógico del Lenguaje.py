# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""
import nltk

# Configurar NLTK y descargar recursos necesarios
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Definir la oración de entrada
sentence = "Si es un gato entonces es un mamífero y si es un perro entonces es un mamífero"

# Tokenizar la oración y etiquetar partes del discurso
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

# Crear una expresión lógica a partir de la oración
def build_logic_expression(tagged_sentence):
    logic_expr = None
    for word, tag in tagged_sentence:
        if tag.startswith('N'):
            logic_expr = word
        elif tag.startswith('V'):
            if word == 'es':
                continue
            elif logic_expr:
                logic_expr = f"({logic_expr} -> {word})"
        elif tag.startswith('J'):
            if word == 'un':
                continue
            elif logic_expr:
                logic_expr = f"({logic_expr} & {word})"
    return logic_expr

logic_expression = build_logic_expression(tagged)
print("Expresión lógica resultante:")
print(logic_expression)
