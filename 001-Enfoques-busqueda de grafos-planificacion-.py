# Importamos el defaultdict y deque de collections para usarlos en la implementación del grafo y BFS.
from collections import defaultdict, deque

# Definimos una clase Grafo para manejar las operaciones relacionadas con el grafo.
class Grafo:

    # Constructor de la clase que inicializa el grafo como un defaultdict de listas.
    def __init__(self):
        self.grafo = defaultdict(list)

    # Método para agregar una conexión entre dos nodos al grafo.
    def agregar_conexion(self, nodo1, nodo2):
        self.grafo[nodo1].append(nodo2)
        self.grafo[nodo2].append(nodo1)

    # Implementación del algoritmo BFS para encontrar el camino más corto entre dos nodos en el grafo.
    def bfs(self, inicio, objetivo):
        cola = deque()  # Creamos una cola para almacenar los nodos a visitar.
        visitado = set()  # Conjunto para mantener registro de los nodos visitados.
        padres = {}  # Diccionario para almacenar los padres de cada nodo en el camino.
        cola.append(inicio)  # Agregamos el nodo de inicio a la cola.
        visitado.add(inicio)  # Marcamos el nodo de inicio como visitado.
        encontrado = False  # Variable para indicar si se ha encontrado el nodo objetivo.

        # Bucle principal de búsqueda en anchura.
        while cola:
            actual = cola.popleft()  # Tomamos el nodo actual de la cola.
            if actual == objetivo:  # Si el nodo actual es el objetivo, terminamos la búsqueda.
                encontrado = True
                break

            # Exploramos los nodos vecinos del nodo actual.
            for vecino in self.grafo[actual]:
                if vecino not in visitado:
                    visitado.add(vecino)  # Marcamos el vecino como visitado.
                    cola.append(vecino)  # Agregamos el vecino a la cola para explorarlo más tarde.
                    padres[vecino] = actual  # Almacenamos el nodo actual como padre del vecino.

        # Reconstruimos el camino más corto desde el nodo objetivo hasta el nodo de inicio.
        if encontrado:
            camino = [objetivo]
            while objetivo != inicio:
                objetivo = padres[objetivo]
                camino.append(objetivo)
            return camino[::-1]  # Invertimos el camino para que vaya desde el inicio hasta el objetivo.
        else:
            return None  # Si no se encuentra un camino, devolvemos None.

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos un grafo de ejemplo y agregamos conexiones entre nodos.
    grafo = Grafo()
    grafo.agregar_conexion(1, 2)
    grafo.agregar_conexion(1, 3)
    grafo.agregar_conexion(2, 4)
    grafo.agregar_conexion(3, 5)
    grafo.agregar_conexion(4, 5)

    inicio = 1
    objetivo = 5
    camino = grafo.bfs(inicio, objetivo)  # Aplicamos BFS para encontrar el camino más corto.

    # Imprimimos el resultado del camino encontrado o un mensaje si no se encontró un camino.
    if camino:
        print(f"Camino más corto desde {inicio} hasta {objetivo}: {camino}")
    else:
        print(f"No se encontró un camino desde {inicio} hasta {objetivo}")
