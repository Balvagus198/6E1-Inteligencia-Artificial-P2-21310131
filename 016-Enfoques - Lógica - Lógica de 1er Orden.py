from sympy import symbols, Or, And, Not

# Definir variables
x, y, z = symbols('x y z')

# Definir la expresión lógica de primer orden
expresion = Or(
    And(x > 0, y > 0),  # Para todo x, existe un y tal que x > 0 y y > 0
    And(Not(x < 0), Not(y < 0))  # Para todo x, y, no es cierto que x < 0 y y < 0
)

# Imprimir la expresión lógica
print("Expresión lógica:")
print(expresion)

# Evaluar la expresión con asignaciones específicas
asignaciones = {
    x: 1,
    y: 2,
    z: 3
}

resultado = expresion.subs(asignaciones)
print("\nResultado de la evaluación:")
print(resultado)
