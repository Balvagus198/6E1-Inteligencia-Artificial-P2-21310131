# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definir las relaciones lógicas como diccionarios
padres = {
    'Pedro': 'Juan',
    'Pablo': 'Pedro',
    'Carlos': 'Pablo'
}

# Funciones para inferir relaciones lógicas
def es_padre(padres, hijo, padre):
    return padres.get(hijo) == padre

def es_abuelo(padres, nieto, abuelo):
    padre = padres.get(nieto)
    return padre and padres.get(padre) == abuelo

def es_ancestro(padres, descendiente, ancestro):
    if descendiente == ancestro:
        return True
    padre = padres.get(descendiente)
    return padre and (padre == ancestro or es_ancestro(padres, padre, ancestro))

# Consultar y mostrar las relaciones lógicas inferidas
print("Padres:")
for hijo, padre in padres.items():
    print(f"{padre} es padre de {hijo}")

print("\nAbuelos:")
for nieto in padres:
    for abuelo in padres.values():
        if es_abuelo(padres, nieto, abuelo):
            print(f"{abuelo} es abuelo de {nieto}")

print("\nAncestros:")
for descendiente in padres:
    for ancestro in padres.values():
        if es_ancestro(padres, descendiente, ancestro):
            print(f"{ancestro} es ancestro de {descendiente}")

# Crear una red semántica utilizando networkx
import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido para la red semántica
red_semantica = nx.DiGraph()

# Agregar nodos y arcos al grafo
aristas = [('Juan', 'Pedro'), ('Pedro', 'Pablo'), ('Pablo', 'Carlos')]
red_semantica.add_edges_from(aristas)

# Dibujar la red semántica
nx.draw(red_semantica, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold')
plt.show()
