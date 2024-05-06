# Definimos una clase Grafo para manejar las operaciones relacionadas con el grafo.
class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializamos el grafo como un diccionario vacío.

    def agregar_conexion(self, nodo1, nodo2):
        if nodo1 in self.grafo:
            self.grafo[nodo1].append(nodo2)  # Agregamos una conexión desde nodo1 a nodo2.
        else:
            self.grafo[nodo1] = [nodo2]  # Si nodo1 no está en el grafo, creamos una lista de adyacencia para nodo1.

    def dfs(self, inicio, objetivo, visitado=None, camino=None):
        if visitado is None:
            visitado = set()  # Conjunto para mantener registro de nodos visitados.
        if camino is None:
            camino = []  # Lista para almacenar el camino actual desde el nodo de inicio.

        visitado.add(inicio)  # Marcamos el nodo de inicio como visitado.
        camino.append(inicio)  # Agregamos el nodo de inicio al camino actual.

        if inicio == objetivo:  # Si el nodo de inicio es el objetivo, devolvemos el camino.
            return camino

        if inicio not in self.grafo:  # Si el nodo de inicio no tiene vecinos, retornamos None.
            return None

        for vecino in self.grafo[inicio]:  # Exploramos los vecinos del nodo de inicio.
            if vecino not in visitado:  # Si el vecino no ha sido visitado, llamamos recursivamente a dfs.
                resultado = self.dfs(vecino, objetivo, visitado, camino)
                if resultado:  # Si se encuentra un camino, lo devolvemos.
                    return resultado

        camino.pop()  # Si no se encuentra un camino desde el nodo de inicio, retrocedemos y exploramos otro camino.
        return None

# Ejemplo de uso
if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_conexion('A', 'B')
    grafo.agregar_conexion('A', 'C')
    grafo.agregar_conexion('B', 'D')
    grafo.agregar_conexion('B', 'E')
    grafo.agregar_conexion('C', 'F')
    grafo.agregar_conexion('E', 'G')

    inicio = 'A'
    objetivo = 'G'
    camino = grafo.dfs(inicio, objetivo)  # Aplicamos DFS para encontrar el camino desde 'A' hasta 'G'.

    if camino:
        print(f"Camino encontrado desde {inicio} hasta {objetivo}: {camino}")
    else:
        print(f"No se encontró un camino desde {inicio} hasta {objetivo}")
