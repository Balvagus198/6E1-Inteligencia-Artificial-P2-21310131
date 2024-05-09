# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class Rule:
    def __init__(self, head, body):
        self.head = head
        self.body = body

class DefaultLogic:
    def __init__(self):
        self.default_rules = []
        self.non_default_rules = []

    def add_default_rule(self, rule):
        self.default_rules.append(rule)

    def add_non_default_rule(self, rule):
        self.non_default_rules.append(rule)

    def infer(self, query):
        conclusions = []
        for rule in self.default_rules:
            if query in rule.head:
                conclusions.append(rule.body)
        for rule in self.non_default_rules:
            if query in rule.head:
                conclusions.append(rule.body)
        return conclusions

# Ejemplo de uso
dl = DefaultLogic()

# Reglas por defecto
default_rule1 = Rule("bird(X)", "flies(X)")
default_rule2 = Rule("bird(X)", "lays_eggs(X)")

# Reglas no por defecto
non_default_rule1 = Rule("bird(Tweety)", "flies(Tweety)")

# Agregar reglas a la lógica por defecto
dl.add_default_rule(default_rule1)
dl.add_default_rule(default_rule2)
dl.add_non_default_rule(non_default_rule1)

# Consulta
query = "flies(Tweety)"
conclusions = dl.infer(query)

print("Conclusión de la consulta:", conclusions)
