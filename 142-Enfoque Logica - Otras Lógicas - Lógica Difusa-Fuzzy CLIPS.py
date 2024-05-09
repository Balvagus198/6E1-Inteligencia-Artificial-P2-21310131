# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import clips

# Inicializar el entorno CLIPS
env = clips.Environment()

# Cargar el módulo Fuzzy CLIPS
env.load('fuzzy.clp')

# Resetear el entorno
env.reset()

# Definir las variables difusas y sus funciones de membresía
env.assert_string('(defvar ?temperatura (fuzzy 0 100))')
env.assert_string('(deffuz-activation ramp)')
env.assert_string('(defuzzify ?temperatura (COG))')

# Insertar hechos
env.assert_string('(temperatura-cold (triangle 0 0 50))')
env.assert_string('(temperatura-warm (triangle 20 50 80))')
env.assert_string('(temperatura-hot (triangle 50 100 100))')

# Evaluar una regla fuzzy
env.assert_string('(temperatura (fuzzy-value 35 (temperatura-warm)))')
env.run()

# Obtener el resultado
result = env.eval('(fuzzy-value ?temperatura)')

# Mostrar el resultado
print(result)
