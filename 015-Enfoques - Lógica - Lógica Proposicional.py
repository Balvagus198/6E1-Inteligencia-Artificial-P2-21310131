class LogicaProposicional:
    def __init__(self, variables, expresion):
        self.variables = variables
        self.expresion = expresion

    def evaluar(self, asignacion):
        for variable in asignacion.keys():
            if variable not in self.variables:
                raise ValueError(f"Variable '{variable}' no está presente en la lista de variables")
        try:
            return eval(self.expresion, asignacion)
        except Exception as e:
            raise ValueError(f"Error al evaluar la expresión: {e}")

# Ejemplo de uso
variables = ['p', 'q', 'r']
expresion = "(p and q) or (not p and r)"

logica = LogicaProposicional(variables, expresion)

asignacion_1 = {'p': True, 'q': True, 'r': False}
resultado_1 = logica.evaluar(asignacion_1)
print(f"Resultado con asignación 1: {resultado_1}")

asignacion_2 = {'p': False, 'q': True, 'r': True}
resultado_2 = logica.evaluar(asignacion_2)
print(f"Resultado con asignación 2: {resultado_2}")
