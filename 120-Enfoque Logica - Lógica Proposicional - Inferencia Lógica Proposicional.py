# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class InferenciaProposicional:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def modus_ponens(self, premisa, conclusion):
        if self.base_conocimiento.verificar_hecho(premisa):
            self.base_conocimiento.agregar_hecho(conclusion)
            return True
        else:
            return False

# Crear una base de conocimiento
base_conocimiento = BaseConocimiento()

# Agregar hechos a la base de conocimiento
base_conocimiento.agregar_hecho("p")
base_conocimiento.agregar_hecho("p -> q")

# Crear un objeto de inferencia lógica proposicional
inferencia = InferenciaProposicional(base_conocimiento)

# Aplicar modus ponens para inferir una nueva conclusión
resultado = inferencia.modus_ponens("p", "q")
print(resultado)  # True si se pudo inferir la conclusión, False si no
print(base_conocimiento.verificar_hecho("q"))  # True si "q" está en la base de conocimiento
