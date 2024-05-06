#Gustavo Balvaneda Peredo   21310131
from sympy import symbols, Not, And, Implies, Or

# Definir variables
x, y, z = symbols('x y z')

# Definir predicados
Mortal = symbols('Mortal')
Hombre = symbols('Hombre')
Padre = symbols('Padre')
Hijo = symbols('Hijo')

# Reglas y hechos de la representación del conocimiento
reglas = [
    Implies(And(Mortal, Hombre), True),  # Todos los hombres son mortales
    Implies(And(Padre, Hijo), True),  # Si x es padre de y y y es hijo de z, entonces x es abuelo de z
    Or(Hombre, Not(Or(Hijo(x, y) for y in [symbols(f'y{i}') for i in range(1, 11)])))  # Existe un hombre que no tiene hijos
]

hechos = [
    Hombre,
    Padre,
    Hijo
]

# Inferencia de conocimiento
def inferir_conocimiento(reglas, hechos):
    conocimiento = hechos.copy()
    nueva_informacion = True

    while nueva_informacion:
        nueva_informacion = False
        for regla in reglas:
            if regla.subs(conocimiento) == True:
                nueva_informacion = True
                conocimiento.extend(regla.atoms())
                reglas.remove(regla)

    return conocimiento

# Ejemplo de uso
conocimiento_final = inferir_conocimiento(reglas, hechos)
print("Conocimiento inferido:")
print(conocimiento_final)
