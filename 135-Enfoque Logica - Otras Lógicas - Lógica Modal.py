# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pymodal import World, Atom

# Creamos un mundo posible
w = World()

# Creamos algunos átomos
p = Atom("p")
q = Atom("q")

# Asignamos átomos a mundos posibles
w1 = World()
w1.assign(p, True)
w1.assign(q, False)

w2 = World()
w2.assign(p, False)
w2.assign(q, True)

# Agregamos mundos al modelo
w.add_child(w1)
w.add_child(w2)

# Imprimimos la verdad de una fórmula modal en un mundo dado
print("En w1, p es verdadero:", w1.satisfies(p))
print("En w1, q es verdadero:", w1.satisfies(q))

print("En w2, p es verdadero:", w2.satisfies(p))
print("En w2, q es verdadero:", w2.satisfies(q))

# Verificamos una fórmula modal
formula = "□(p → q)"  # Representa "siempre que p sea verdadero, q también lo es"
print("La fórmula", formula, "es verdadera en w:", w.satisfies(formula))
