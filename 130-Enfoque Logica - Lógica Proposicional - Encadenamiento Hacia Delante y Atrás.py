# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pyknow import *

class Ejemplo(Fact):
    pass

class MotorDeInferencia(KnowledgeEngine):
    @Rule(Fact())
    def hecho_inicial(self):
        print("Hecho inicial")
        self.declare(Ejemplo(propiedad='A'))

    @Rule(Ejemplo(propiedad='A'))
    def regla_1(self):
        print("Se cumple la regla 1")
        self.declare(Ejemplo(propiedad='B'))

    @Rule(Ejemplo(propiedad='B'))
    def regla_2(self):
        print("Se cumple la regla 2")
        self.declare(Ejemplo(propiedad='C'))

engine = MotorDeInferencia()
engine.reset()
engine.declare(Fact())
engine.run()

