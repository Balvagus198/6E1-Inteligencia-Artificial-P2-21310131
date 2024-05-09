# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pystrips import run_optimize, create_state, create_action, Plan

# Definir acciones
accion_ir_biblioteca = create_action('Ir_Biblioteca', preconditions=['En_Casa'], effects=['En_Biblioteca'])
accion_estudiar = create_action('Estudiar', preconditions=['En_Biblioteca', 'Tener_Libros'], effects=['Saber_Materia'])
accion_ir_casa = create_action('Ir_Casa', preconditions=['En_Biblioteca'], effects=['En_Casa'])

# Definir estado inicial y estado objetivo
estado_inicial = create_state({'En_Casa'})
estado_objetivo = create_state({'Saber_Materia'})

# Definir el planificador y resolver el problema
planificador = run_optimize(estado_inicial, estado_objetivo, [accion_ir_biblioteca, accion_estudiar, accion_ir_casa])

# Mostrar el plan resultante
if planificador:
    print("Plan encontrado:")
    for accion in planificador.actions:
        print(f"- {accion.name}")
else:
    print("No se pudo encontrar un plan para alcanzar el estado objetivo.")
