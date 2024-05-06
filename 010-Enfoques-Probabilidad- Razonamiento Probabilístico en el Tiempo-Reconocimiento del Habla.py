from hmmlearn import hmm
import numpy as np

# Definir las palabras clave y sus índices
palabras = ['hola', 'adios']
indice_palabras = {indice: palabra for indice, palabra in enumerate(palabras)}

# Crear un modelo de HMM
modelo_hmm = hmm.MultinomialHMM(n_components=len(palabras))

# Entrenar el modelo con algunas secuencias de observaciones
secuencias_entrenamiento = [
    [0, 1, 0, 0],  # 'hola adios hola hola'
    [1, 0, 1]      # 'adios hola adios'
]
longitudes_secuencias = [len(seq) for seq in secuencias_entrenamiento]
observaciones = np.concatenate(secuencias_entrenamiento)
modelo_hmm.fit(np.atleast_2d(observaciones).T, longitudes_secuencias)

# Generar una secuencia de observaciones simulada
secuencia_estados_ocultos = modelo_hmm.predict(np.atleast_2d(observaciones).T)

# Traducir la secuencia de estados ocultos a palabras
palabras_simuladas = [indice_palabras[indice] for indice in secuencia_estados_ocultos]

# Imprimir resultados
print("Secuencia de estados ocultos simulada:", secuencia_estados_ocultos)
print("Palabras simuladas:", palabras_simuladas)
