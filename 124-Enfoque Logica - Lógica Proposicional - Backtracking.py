# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones

    def verificar_restricciones(self, variable, valor, asignacion_actual):
        for restriccion in self.restricciones.get(variable, []):
            if not restriccion(variable, valor, asignacion_actual):
                return False
        return True

    def backtrack(self, asignacion_actual={}):
        if len(asignacion_actual) == len(self.variables):
            return asignacion_actual

        variable_no_asignada = next(
            variable for variable in self.variables if variable not in asignacion_actual
        )

        for valor in self.dominios[variable_no_asignada]:
            if self.verificar_restricciones(variable_no_asignada, valor, asignacion_actual):
                asignacion_actual[variable_no_asignada] = valor
                resultado = self.backtrack(asignacion_actual)
                if resultado is not None:
                    return resultado
                del asignacion_actual[variable_no_asignada]

        return None


# Ejemplo de uso
variables = ['A', 'B', 'C']
dominios = {
    'A': [1, 2],
    'B': [3, 4],
    'C': [5, 6]
}
restricciones = {
    'A': [lambda A, B, _: A != B],  # Restricción: A y B no pueden tener el mismo valor
    'B': [lambda A, B, _: A != B]   # Restricción: A y B no pueden tener el mismo valor
}

problema_csp = CSP(variables, dominios, restricciones)
solucion = problema_csp.backtrack()

if solucion is not None:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución para el problema CSP.")
