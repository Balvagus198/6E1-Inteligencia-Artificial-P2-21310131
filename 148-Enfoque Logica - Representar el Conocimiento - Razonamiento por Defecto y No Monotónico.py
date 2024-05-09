# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pyknow import *

# Definir un hecho por defecto
@DefFacts()
def default_facts():
    yield Fact(alarm=True)

# Definir una regla con razonamiento no monotónico
class MiSistemaExperto(KnowledgeEngine):
    @Rule(Fact(alarm=True))
    def activar_alarma(self):
        print("Alarma activada")

    @Rule(AND(Fact(alarm=True), NOT(Fact(burglar_detected=True))))
    def falso_positivo(self):
        print("Falso positivo: La alarma se activó sin detectar un intruso")

    @Rule(Fact(alarm=True), Fact(burglar_detected=True))
    def intruso_detectado(self):
        print("¡Intruso detectado!")

# Crear una instancia del sistema experto y ejecutar el razonamiento
experto = MiSistemaExperto()
experto.reset()
experto.declare(Fact(burglar_detected=True))
experto.run()
