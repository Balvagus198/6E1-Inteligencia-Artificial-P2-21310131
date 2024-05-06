# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""

from sympy import symbols, And, Or, Not, Implies

# Definir variables y símbolos
A, B, C = symbols('A B C')
P, Q, R = symbols('P Q R')

# Definir predicados
Mortal = symbols('Mortal')
Humano = symbols('Humano')
Animal = symbols('Animal')
EsMamifero = symbols('EsMamifero')
EsCarnivoro = symbols('EsCarnivoro')

# Reglas de conocimiento
reglas = [
    Implies(And(Humano, Mortal), True),  # Todos los humanos son mortales
    Implies(And(Animal, EsMamifero), Not(EsCarnivoro)),  # Si un animal es mamífero, no es carnívoro
    Implies(Or(A, B), C)  # Si A o B es verdadero, entonces C es verdadero
]

# Ejemplos de situaciones conocidas
situaciones_conocidas = [
    {Humano: True, Mortal: True},  # Ejemplo de un humano que es mortal
    {Animal: True, EsMamifero: True},  # Ejemplo de un animal que es mamífero
    {A: True, B: True}  # Ejemplo de situación que cumple la tercera regla
]

# Función de aprendizaje
def aprendizaje(reglas, situaciones):
    nuevos_hechos = []
    for situacion in situaciones:
        for regla in reglas:
            if regla.subs(situacion) == True:
                nuevos_hechos.extend(regla.atoms() - set(situacion.keys()))
    return nuevos_hechos

# Obtener nuevos hechos aprendidos
nuevos_hechos_aprendidos = aprendizaje(reglas, situaciones_conocidas)
print("Nuevos hechos aprendidos:")
print(nuevos_hechos_aprendidos)
