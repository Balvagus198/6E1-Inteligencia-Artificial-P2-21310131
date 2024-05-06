import heapq  # Importamos el módulo heapq para usar la cola de prioridad.
import math  # Importamos el módulo math para operaciones matemáticas.

class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializamos el grafo como un diccionario vacío.

    def agregar_conexion(self, nodo1, nodo2, peso):
        if nodo1 in self.grafo:
            self.grafo[nodo1][nodo2] = peso  # Agregamos una conexión con su respectivo peso.
        else:
            self.grafo[nodo1] = {nodo2: peso}  # Si el nodo no está en el grafo, lo creamos con su conexión.

    def a_estrella(self, inicio, objetivo):
        cola_prioridad = []  # Creamos una cola de prioridad usando heapq.
        heapq.heappush(cola_prioridad, (0, inicio))  # Agregamos el nodo de inicio con costo cero a la cola.
        padres = {}  # Diccionario para almacenar los padres de cada nodo en el camino.
        costos = {nodo: math.inf for nodo in self.grafo}  # Inicializamos los costos como infinito.
        costos[inicio] = 0  # El costo del nodo de inicio es cero.

        while cola_prioridad:
            costo_actual, actual = heapq.heappop(cola_prioridad)  # Obtenemos el nodo actual y su costo actual de la cola.

            if actual == objetivo:  # Si el nodo actual es el objetivo, reconstruimos el camino y lo devolvemos.
                camino = [actual]
                while actual in padres:
                    actual = padres[actual]
                    camino.append(actual)
                return camino[::-1]  # Invertimos el camino para que vaya desde el inicio hasta el objetivo.

            if actual not in self.grafo:
                continue  # Si el nodo actual no tiene vecinos, pasamos al siguiente nodo en la cola.

            for vecino, peso in self.grafo[actual].items():  # Exploramos los vecinos del nodo actual.
                costo_nuevo = costos[actual] + peso  # Calculamos el nuevo costo desde el nodo de inicio hasta el vecino.
                if costo_nuevo < costos.get(vecino, math.inf):  # Si el nuevo costo es menor que el costo anterior,
                    costos[vecino] = costo_nuevo  # actualizamos el costo del vecino.
                    padres[vecino] = actual  # Actualizamos el padre del vecino en el camino.
                    heuristica = self.distancia_euclidiana(vecino, objetivo)  # Calculamos la heurística del vecino.
                    heapq.heappush(cola_prioridad, (costo_nuevo + heuristica, vecino))  # Agregamos el vecino a la cola de prioridad.

        return None  # Si no se encuentra un camino, devolvemos None.

    def distancia_euclidiana(self, nodo1, nodo2):
        x1, y1 = nodo1  # Obtenemos las coordenadas del nodo1.
        x2, y2 = nodo2  # Obtenemos las coordenadas del nodo2.
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Calculamos la distancia euclidiana entre los nodos.

# Ejemplo de uso
if __name__ == "__main__":
    grafo = Grafo()
    # Creamos un grafo de ejemplo con nodos y conexiones.
    # Los nodos están representados como tuplas de coordenadas (x, y).
    grafo.agregar_conexion((0, 0), (0, 1), 1)
    grafo.agregar_conexion((0, 0), (1, 0), 1)
    grafo.agregar_conexion((0, 1), (1, 1), 1)
    grafo.agregar_conexion((1, 0), (1, 1), 1)
    grafo.agregar_conexion((1, 0), (2, 0), 1)
    grafo.agregar_conexion((1, 1), (1, 2), 1)
    grafo.agregar_conexion((2, 0), (2, 1), 1)
    grafo.agregar_conexion((2, 1), (2, 2), 1)

    inicio = (0, 0)  # Nodo de inicio.
    objetivo = (2, 2)  # Nodo objetivo.
    camino = grafo.a_estrella(inicio, objetivo)  # Aplicamos A* para encontrar el camino más corto.

    if camino:
        print(f"Camino más corto desde {inicio} hasta {objetivo}: {camino}")  # Imprimimos el camino más corto.
    else:
        print(f"No se encontró un camino desde {inicio} hasta {objetivo}")  # Imprimimos un mensaje si no se encuentra un camino.
