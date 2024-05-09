# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pyknow import *

class Paciente(Fact):
    """Clase para representar un paciente con síntomas."""
    pass

class Diagnostico(KnowledgeEngine):
    @Rule(Paciente(fiebre=True, tos=True))
    def diagnostico_resfriado(self):
        print("El paciente tiene resfriado común.")

    @Rule(Paciente(fiebre=True, dolor_garganta=True))
    def diagnostico_gripe(self):
        print("El paciente tiene gripe.")

    @Rule(Paciente(dificultad_respiratoria=True))
    def diagnostico_neumonia(self):
        print("El paciente podría tener neumonía.")

    @Rule(Paciente(fiebre=True, tos=True, dolor_garganta=True, dificultad_respiratoria=True))
    def diagnostico_covid19(self):
        print("El paciente podría tener COVID-19. Se requiere prueba adicional.")

# Crear una instancia del sistema experto
experto = Diagnostico()

# Insertar hechos sobre el paciente
experto.declare(Paciente(fiebre=True, tos=True, dificultad_respiratoria=True))

# Ejecutar el sistema experto para obtener el diagnóstico
experto.run()
