# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definir la lista de frutas con sus características
frutas = [
    {'nombre': 'Manzana', 'color': 'Rojo', 'tamaño': 'Pequeño', 'textura': 'Suave'},
    {'nombre': 'Naranja', 'color': 'Naranja', 'tamaño': 'Mediano', 'textura': 'Rugoso'},
    {'nombre': 'Plátano', 'color': 'Amarillo', 'tamaño': 'Grande', 'textura': 'Suave'},
    {'nombre': 'Limón', 'color': 'Amarillo', 'tamaño': 'Pequeño', 'textura': 'Rugoso'},
]

# Función de aprendizaje (K-DL) para crear reglas heurísticas
def aprender_reglas(frutas):
    reglas = []
    for fruta in frutas:
        if fruta['color'] == 'Rojo' and fruta['tamaño'] == 'Pequeño':
            reglas.append((fruta['nombre'], 'Manzana'))
        elif fruta['color'] == 'Amarillo':
            reglas.append((fruta['nombre'], 'Plátano o Limón'))
        else:
            reglas.append((fruta['nombre'], 'Desconocido'))
    return reglas

# Función de prueba (K-DT) para evaluar el modelo con pruebas específicas
def probar_modelo(modelo, pruebas):
    resultados = []
    for prueba in pruebas:
        for regla in modelo:
            if regla[0] == prueba['nombre']:
                if regla[1] == prueba['etiqueta']:
                    resultados.append((prueba['nombre'], 'Clasificación correcta'))
                else:
                    resultados.append((prueba['nombre'], 'Clasificación incorrecta'))
                break
        else:
            resultados.append((prueba['nombre'], 'No se encontró regla'))
    return resultados

# Crear modelo de reglas heurísticas (K-DL)
modelo = aprender_reglas(frutas)

# Definir pruebas específicas (K-DT)
pruebas = [
    {'nombre': 'Manzana', 'etiqueta': 'Manzana'},
    {'nombre': 'Naranja', 'etiqueta': 'Naranja'},
    {'nombre': 'Plátano', 'etiqueta': 'Plátano'},
    {'nombre': 'Limón', 'etiqueta': 'Limón'},
    {'nombre': 'Durazno', 'etiqueta': 'Manzana'},  # Prueba incorrecta para evaluar K-DT
]

# Evaluar modelo con pruebas (K-DT)
resultados = probar_modelo(modelo, pruebas)

# Mostrar resultados
for resultado in resultados:
    print(f"{resultado[0]}: {resultado[1]}")
