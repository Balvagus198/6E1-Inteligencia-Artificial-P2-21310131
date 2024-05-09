# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
from prologpy import Prolog

# Inicializar el intérprete de Prolog
prolog = Prolog()

# Definir ejemplos positivos y negativos
ejemplos_positivos = [
    ("hombre(socrates)", True),
    ("mortal(socrates)", True),
    ("hombre(platon)", True),
    ("hombre(aristoteles)", True),
]

ejemplos_negativos = [
    ("hombre(platon)", False),
    ("hombre(aristoteles)", False),
    ("mortal(aristoteles)", False),
]

# Cargar ejemplos positivos y negativos en Prolog
for ejemplo, es_positivo in ejemplos_positivos:
    prolog.assertz(f"{ejemplo} :- {es_positivo}.")

for ejemplo, es_negativo in ejemplos_negativos:
    prolog.assertz(f"not {ejemplo} :- {es_negativo}.")

# Ejecutar el algoritmo FOIL para aprender reglas
reglas_aprendidas = prolog.query("foil.")

# Mostrar las reglas aprendidas
print("Reglas Aprendidas:")
for regla in reglas_aprendidas:
    print(regla)

