# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido para la planificación de orden parcial
grafo = nx.DiGraph()

# Agregar tareas al grafo con restricciones de precedencia
grafo.add_node("Tarea 1")
grafo.add_node("Tarea 2")
grafo.add_node("Tarea 3")
grafo.add_node("Tarea 4")

# Agregar relaciones de precedencia entre las tareas
grafo.add_edge("Tarea 1", "Tarea 2")
grafo.add_edge("Tarea 1", "Tarea 3")
grafo.add_edge("Tarea 2", "Tarea 4")
grafo.add_edge("Tarea 3", "Tarea 4")

# Visualizar el grafo de planificación de orden parcial
nx.draw(grafo, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold')
plt.show()

# Calcular un orden parcial válido para las tareas
orden_parcial = list(nx.topological_sort(grafo))
print("Orden Parcial de Ejecución de Tareas:", orden_parcial)
