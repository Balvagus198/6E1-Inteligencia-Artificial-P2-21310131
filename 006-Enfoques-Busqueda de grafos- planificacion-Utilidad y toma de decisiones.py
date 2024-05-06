import heapq

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
        self.distancias = {}

    def agregar_nodo(self, valor):
        self.nodos.add(valor)

    def agregar_arista(self, desde, hacia, distancia):
        self.aristas.setdefault(desde, []).append(hacia)
        self.aristas.setdefault(hacia, []).append(desde)
        self.distancias[(desde, hacia)] = distancia
        self.distancias[(hacia, desde)] = distancia

    def dijkstra(self, inicio):
        cola_prioridad = [(0, inicio)]
        distancias = {nodo: float('infinity') for nodo in self.nodos}
        distancias[inicio] = 0

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if distancia_actual > distancias[nodo_actual]:
                continue

            for vecino in self.aristas[nodo_actual]:
                nueva_distancia = distancias[nodo_actual] + self.distancias[(nodo_actual, vecino)]
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return distancias

# Ejemplo de uso
if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_nodo("A")
    grafo.agregar_nodo("B")
    grafo.agregar_nodo("C")
    grafo.agregar_nodo("D")
    grafo.agregar_nodo("E")

    grafo.agregar_arista("A", "B", 4)
    grafo.agregar_arista("A", "C", 2)
    grafo.agregar_arista("B", "C", 5)
    grafo.agregar_arista("B", "D", 10)
    grafo.agregar_arista("C", "D", 3)
    grafo.agregar_arista("C", "E", 8)
    grafo.agregar_arista("D", "E", 6)

    inicio = "A"
    distancias_desde_inicio = grafo.dijkstra(inicio)

    print("Distancias desde el nodo inicial:")
    for nodo, distancia in distancias_desde_inicio.items():
        print(f"Distancia desde {inicio} a {nodo}: {distancia}")
