import random  # Importamos el módulo random para generar números aleatorios.

# Función de aptitud: cuenta el número de bits "1" en la cadena
def aptitud(cadena):
    return sum(c == '1' for c in cadena)

# Función de selección de padres por torneo
def seleccion_torneo(poblacion, n_torneo):
    torneo = random.sample(poblacion, n_torneo)  # Seleccionamos aleatoriamente n_torneo individuos de la población.
    torneo.sort(key=lambda x: aptitud(x), reverse=True)  # Ordenamos el torneo por aptitud (mayor a menor).
    return torneo[0]  # Devolvemos el individuo con mayor aptitud.

# Función de cruce (crossover) de dos cadenas
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)  # Seleccionamos un punto de cruce aleatorio.
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]  # Creamos el primer hijo intercambiando las partes de los padres.
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]  # Creamos el segundo hijo intercambiando las partes de los padres.
    return hijo1, hijo2  # Devolvemos los dos hijos generados.

# Función de mutación de una cadena
def mutacion(cadena, prob_mutacion):
    nueva_cadena = ''  # Inicializamos una nueva cadena vacía.
    for bit in cadena:
        if random.random() < prob_mutacion:  # Probamos si se produce una mutación en el bit.
            nueva_cadena += '1' if bit == '0' else '0'  # Si hay mutación, invertimos el bit.
        else:
            nueva_cadena += bit  # Si no hay mutación, mantenemos el bit original.
    return nueva_cadena  # Devolvemos la cadena mutada o no.

# Algoritmo Genético
def algoritmo_genetico(tam_poblacion, tam_cadena, prob_mutacion, generaciones):
    # Inicializar población aleatoria
    poblacion = [''.join(random.choice('01') for _ in range(tam_cadena)) for _ in range(tam_poblacion)]
    # Generamos una población aleatoria de cadenas de bits de longitud tam_cadena.

    for generacion in range(generaciones):
        nueva_poblacion = []  # Inicializamos una nueva población vacía para la siguiente generación.
        for _ in range(tam_poblacion // 2):
            # Selección de padres
            padre1 = seleccion_torneo(poblacion, 3)  # Seleccionamos el primer padre por torneo.
            padre2 = seleccion_torneo(poblacion, 3)  # Seleccionamos el segundo padre por torneo.

            # Cruce
            hijo1, hijo2 = cruce(padre1, padre2)  # Cruzamos los padres para obtener dos hijos.

            # Mutación
            hijo1 = mutacion(hijo1, prob_mutacion)  # Mutamos al primer hijo.
            hijo2 = mutacion(hijo2, prob_mutacion)  # Mutamos al segundo hijo.

            nueva_poblacion.extend([hijo1, hijo2])  # Agregamos los hijos a la nueva población.

        poblacion = nueva_poblacion  # Reemplazamos la población anterior con la nueva población.

        # Calcular la mejor solución de la generación actual
        mejor_solucion = max(poblacion, key=lambda x: aptitud(x))  # Encontramos la cadena con mayor aptitud.

        print(f"Generación {generacion + 1}: Mejor solución -> {mejor_solucion} (Aptitud: {aptitud(mejor_solucion)})")
        # Imprimimos la mejor solución y su aptitud en la generación actual.

# Parámetros del algoritmo genético
tam_poblacion = 20  # Tamaño de la población.
tam_cadena = 10  # Longitud de la cadena de bits.
prob_mutacion = 0.1  # Probabilidad de mutación.
generaciones = 50  # Número de generaciones.

# Ejecutar el algoritmo genético
algoritmo_genetico(tam_poblacion, tam_cadena, prob_mutacion, generaciones)
# Llamamos a la función del algoritmo genético con los parámetros especificados.
