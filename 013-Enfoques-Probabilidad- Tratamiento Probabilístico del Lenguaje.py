import nltk
import random

# Descargar el conjunto de datos de prueba
nltk.download('gutenberg')
nltk.download('punkt')

# Importar el corpus Gutenberg y tokenizar el texto
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize

# Obtener el texto del libro "Moby Dick"
texto = gutenberg.raw('melville-moby_dick.txt')

# Tokenizar el texto en palabras
palabras = word_tokenize(texto)

# Generar n-gramas a partir de las palabras tokenizadas
def generar_ngramas(tokens, n):
    ngramas = []
    for i in range(len(tokens) - n + 1):
        ngramas.append(tuple(tokens[i:i + n]))  # Convertir a tupla en lugar de lista
    return ngramas

# Crear n-gramas de 2 palabras (bigramas)
bigramas = generar_ngramas(palabras, 2)

# Contar la frecuencia de cada bigrama
frecuencia_bigramas = nltk.FreqDist(bigramas)

# Obtener la lista de bigramas únicos
bigramas_unicos = list(frecuencia_bigramas.keys())

# Imprimir algunos bigramas y palabras únicas para revisión
print("Algunos bigramas generados:")
print(bigramas[:10])  # Imprimir los primeros 10 bigramas
print("\nPalabras únicas en el corpus:")
print(set(palabras))  # Imprimir la lista de palabras únicas en el corpus

# Función para predecir la siguiente palabra dado un bigrama
def predecir_siguiente_palabra(bigram, bigramas_unicos):
    palabras_posibles = [bigrama[1] for bigrama in bigramas_unicos if bigrama[0] == bigram]
    if palabras_posibles:
        return random.choice(palabras_posibles)
    else:
        return None

# Ejemplo de uso: predecir la siguiente palabra después de "Call me"
bigrama_dado = ("Call", "me")  # Usar tupla en lugar de lista
siguiente_palabra = predecir_siguiente_palabra(bigrama_dado, bigramas_unicos)

if siguiente_palabra:
    print(f"\nSiguiente palabra después de '{bigrama_dado}': {siguiente_palabra}")
else:
    print(f"\nNo se encontraron palabras después de '{bigrama_dado}' en el corpus")
