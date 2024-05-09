# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class Rule:
    def __init__(self, head, body):
        self.head = head
        self.body = body

    def __str__(self):
        return f"{self.head} :- {', '.join(self.body)}"

class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def infer(self, query):
        consequences = []
        for rule in self.rules:
            if query in rule.body:
                consequences.append(rule.head)
        return consequences

# Ejemplo de uso
kb = KnowledgeBase()

# Reglas
rule1 = Rule("bird(X)", ["flies(X)"])
rule2 = Rule("bird(X)", ["lays_eggs(X)"])
rule3 = Rule("flies(X)", ["bird(X)"])
rule4 = Rule("bird(X)", ["penguin(X)"])

# Agregar reglas a la base de conocimiento
kb.add_rule(rule1)
kb.add_rule(rule2)
kb.add_rule(rule3)
kb.add_rule(rule4)

# Consulta
query = "flies(Tweety)"
consequences = kb.infer(query)

print("Consecuencias de la consulta:", consequences)
