import random

class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables
        self.dominios = dominios  # Diccionario de dominios de las variables
        self.restricciones = restricciones  # Lista de restricciones

    def asignar_valor(self, variable, valor, asignacion):
        asignacion[variable] = valor  # Asigna un valor a una variable en la asignación

    def consistente(self, variable, valor, asignacion):
        for restriccion in self.restricciones:
            if not restriccion(variable, valor, asignacion):  # Verifica la consistencia con las restricciones
                return False  # La asignación no es consistente
        return True  # La asignación es consistente si todas las restricciones se cumplen

    def minimos_conflictos(self, asignacion, max_pasos=1000):
        for _ in range(max_pasos):
            conflictos = self.contar_conflictos(asignacion)  # Contamos los conflictos en la asignación actual
            if conflictos == 0:
                return asignacion  # Si no hay conflictos, hemos encontrado una solución
            variable = random.choice(list(asignacion.keys()))  # Seleccionamos una variable aleatoria
            mejor_valor = self.mejor_valor(variable, asignacion)  # Encontramos el mejor valor para la variable
            self.asignar_valor(variable, mejor_valor, asignacion)  # Asignamos el mejor valor a la variable
        return None  # Si alcanzamos el número máximo de pasos y no encontramos solución, devolvemos None

    def contar_conflictos(self, asignacion):
        conflictos = 0
        for restriccion in self.restricciones:
            for variable in self.variables:
                valor = asignacion[variable]
                if not restriccion(variable, valor, asignacion):  # Verifica la consistencia con las restricciones
                    conflictos += 1
        return conflictos

    def mejor_valor(self, variable, asignacion):
        dominio = self.dominios[variable]
        mejor_valor = None
        min_conflictos = float('inf')
        for valor in dominio:
            asignacion[variable] = valor  # Asignamos temporalmente un valor a la variable
            conflictos = self.contar_conflictos(asignacion)  # Contamos los conflictos con este valor
            if conflictos < min_conflictos:
                mejor_valor = valor
                min_conflictos = conflictos
        return mejor_valor

# Ejemplo de uso
if __name__ == "__main__":
    variables = ['A', 'B', 'C', 'D', 'E']
    dominios = {'A': ['Rojo', 'Verde', 'Azul'], 'B': ['Rojo', 'Verde'], 'C': ['Rojo', 'Azul'], 'D': ['Verde', 'Azul'], 'E': ['Rojo', 'Verde', 'Azul']}
    
    def restriccion_diferente(variable, valor, asignacion):
        vecinos = {'A': ['B', 'C', 'D'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D', 'E'], 'D': ['A', 'C', 'E'], 'E': ['C', 'D']}
        for vecino in vecinos[variable]:
            if vecino in asignacion and asignacion[vecino] == valor:
                return False  # Valor igual al de un vecino
        return True  # Valor diferente al de todos los vecinos

    restricciones = [restriccion_diferente]
    problema = CSP(variables, dominios, restricciones)
    asignacion_inicial = {'A': 'Rojo', 'B': 'Verde', 'C': 'Azul', 'D': 'Rojo', 'E': 'Verde'}
    solucion = problema.minimos_conflictos(asignacion_inicial)

    if solucion:
        print("Solución encontrada:")
        for variable, valor in solucion.items():
            print(f"{variable}: {valor}")
    else:
        print("No se encontró solución después de 1000 pasos")

