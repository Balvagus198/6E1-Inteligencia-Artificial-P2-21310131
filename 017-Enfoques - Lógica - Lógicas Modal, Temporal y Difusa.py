#Gustavo Balvaneda Peredo   21310131
from sympy import symbols
from sympy.logic.boolalg import Implies, Not

# Definir variables
p, q = symbols('p q')

# Simulación de lógica modal: Necesidad y Posibilidad
def box(p):
    return Not(Not(p))

def diamond(p):
    return Not(Not(p))

# Lógica modal simulada
expresion_modal = Implies(box(p), diamond(q))  # ◻p → ◇q
print("Expresión de lógica modal simulada:")
print(expresion_modal)
