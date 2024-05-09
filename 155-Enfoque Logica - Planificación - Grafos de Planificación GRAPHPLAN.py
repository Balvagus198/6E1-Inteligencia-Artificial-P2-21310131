# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido acíclico para representar el grafo de planificación
grafo_planificacion = nx.DiGraph()

# Agregar nodos (acciones y estados) al grafo de planificación
grafo_planificacion.add_nodes_from([
    "Inicio", "Objetivo", 
    "Accion1", "Accion2", "Accion3", 
    "Estado1", "Estado2", "Estado3"
])

# Agregar aristas que representan las dependencias entre acciones y estados
grafo_planificacion.add_edges_from([
    ("Inicio", "Accion1"), ("Inicio", "Accion2"), ("Inicio", "Accion3"),
    ("Accion1", "Estado1"), ("Accion2", "Estado2"), ("Accion3", "Estado3"),
    ("Estado1", "Accion2"), ("Estado2", "Accion3"),
    ("Accion1", "Objetivo"), ("Accion2", "Objetivo"), ("Accion3", "Objetivo")
])

# Visualizar el grafo de planificación
posiciones = nx.planar_layout(grafo_planificacion)  # Calcular las posiciones para el layout
nx.draw(grafo_planificacion, pos=posiciones, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold')
plt.show()
