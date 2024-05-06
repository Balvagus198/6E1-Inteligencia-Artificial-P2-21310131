import numpy as np

# Generar una distribución de probabilidad aleatoria
def generar_distribucion_probabilidad(tamano):
    distribucion = np.random.rand(tamano)
    return distribucion / np.sum(distribucion)

# Calcular la entropía de una distribución de probabilidad
def calcular_entropia(distribucion):
    entropia = -np.sum(distribucion * np.log2(distribucion + 1e-9))
    return entropia

# Ejemplo de uso
if __name__ == "__main__":
    tamano_distribucion = 5
    distribucion = generar_distribucion_probabilidad(tamano_distribucion)
    entropia = calcular_entropia(distribucion)

    print("Distribución de probabilidad generada:")
    print(distribucion)
    print("Entropía de la distribución:", entropia)
