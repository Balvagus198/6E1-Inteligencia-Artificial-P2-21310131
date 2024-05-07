# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sympy import symbols, Implies, And, Or, Not, ForAll, Exists

# Definir variables
paciente, sintoma, enfermedad = symbols('paciente sintoma enfermedad')

# Regla de diagnóstico: Si un paciente tiene ciertos síntomas, entonces tiene una enfermedad
regla_diagnostico = Implies(And(sintoma, Not(enfermedad)), paciente)

# Regla causal: Si un paciente tiene ciertos síntomas, entonces tiene una causa específica
regla_causal = Implies(And(sintoma, Not(enfermedad)), Exists(enfermedad))

# Expresar universalmente la regla causal
regla_causal_universal = ForAll(paciente, regla_causal)

# Ejemplo de aplicación de las reglas
sintoma_paciente = True
tiene_enfermedad = False

# Aplicar la regla de diagnóstico
diagnostico_paciente = regla_diagnostico.subs({sintoma: sintoma_paciente, enfermedad: tiene_enfermedad})

# Aplicar la regla causal
causa_paciente = regla_causal_universal.subs({sintoma: sintoma_paciente, enfermedad: tiene_enfermedad})

# Mostrar resultados
print("Diagnóstico del paciente:", diagnostico_paciente)
print("Causa del paciente:", causa_paciente)
