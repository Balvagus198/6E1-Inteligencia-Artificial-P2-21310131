# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class State:
    def __init__(self, name):
        self.name = name
        self.transitions = []

    def add_transition(self, transition):
        self.transitions.append(transition)

class Transition:
    def __init__(self, source, target, condition):
        self.source = source
        self.target = target
        self.condition = condition

class TemporalModel:
    def __init__(self):
        self.states = {}

    def add_state(self, name):
        if name not in self.states:
            self.states[name] = State(name)

    def add_transition(self, source, target, condition):
        transition = Transition(source, target, condition)
        self.states[source].add_transition(transition)

    def check(self, formula):
        # Aquí implementarías la lógica para verificar la fórmula en el modelo temporal
        # Por ejemplo, podrías recorrer los estados y transiciones según la fórmula
        # y verificar si se cumple o no

        # Por simplicidad, devolvemos siempre True
        return True

# Ejemplo de uso
model = TemporalModel()
model.add_state("s0")
model.add_state("s1")
model.add_transition("s0", "s1", "p")

formula = "G(p -> Fq)"
result = model.check(formula)
print("La fórmula", formula, "es", result)
