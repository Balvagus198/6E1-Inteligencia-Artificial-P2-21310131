# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""

from sympy import symbols, Not, And, Implies

# Definir variables
Trabajar, Descansar, Listo, Estresado = symbols('Trabajar Descansar Listo Estresado')

# Reglas de planificación
reglas = [
    Implies(And(Trabajar, Not(Descansar)), Listo),  # Si trabajamos y no descansamos, estaremos listos
    Implies(Estresado, Not(Trabajar)),  # Si estamos estresados, no podemos trabajar
    Implies(Estresado, Descansar)  # Si estamos estresados, debemos descansar
]

# Ejemplo de situación
situacion = {
    Estresado: True,
    Listo: False
}

# Inferencia de acciones a tomar
def planificacion(reglas, situacion):
    acciones = []
    for regla in reglas:
        condicion = all(situacion.get(s, False) for s in regla.free_symbols)
        if condicion and regla.subs(situacion) == True:
            acciones.extend(regla.free_symbols - set(situacion.keys()))
            reglas.remove(regla)
    return acciones

# Obtener acciones a tomar
acciones_a_tomar = planificacion(reglas, situacion)
print("Acciones a tomar:")
print(acciones_a_tomar)
