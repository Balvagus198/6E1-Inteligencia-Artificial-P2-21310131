# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import random
import time

class Agente:
    def __init__(self, nombre, objetivo):
        self.nombre = nombre
        self.objetivo = objetivo

    def tomar_decision(self, estado_actual):
        print(f"{self.nombre}: Tomando decisión en el estado {estado_actual}")
        if random.random() < 0.8:  # Simulación de una acción exitosa en un 80% de los casos
            print(f"{self.nombre}: Realizando acción para avanzar hacia el objetivo {self.objetivo}")
        else:
            print(f"{self.nombre}: Fallo en la acción, replanificando...")
            self.replanificar()

    def replanificar(self):
        print(f"{self.nombre}: Generando un nuevo plan de acción...")
        # Aquí iría el proceso de replanificación en un escenario real

# Crear agentes
agente1 = Agente("Agente 1", "Objetivo A")
agente2 = Agente("Agente 2", "Objetivo B")
agente3 = Agente("Agente 3", "Objetivo C")

# Simular planificación continua y multiagente
while True:
    # Obtener información del entorno
    estado_actual = random.choice(["Estado 1", "Estado 2", "Estado 3"])
    
    # Tomar decisiones de los agentes
    agente1.tomar_decision(estado_actual)
    agente2.tomar_decision(estado_actual)
    agente3.tomar_decision(estado_actual)

    # Esperar un intervalo de tiempo antes de la siguiente iteración (simulando el tiempo continuo)
    time.sleep(1)
