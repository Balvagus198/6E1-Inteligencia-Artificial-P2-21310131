# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np

# Probabilidad a priori de las hipótesis
prior_A = 0.3  # Hipótesis A: dado sesgado
prior_B = 0.7  # Hipótesis B: dado equilibrado

# Verosimilitud de la evidencia bajo cada hipótesis
likelihood_A = 0.5  # Hipótesis A: dado sesgado, verosimilitud de mostrar un número par
likelihood_B = 1/3  # Hipótesis B: dado equilibrado, verosimilitud de mostrar un número par

# Ponderación de verosimilitud
posterior_A = prior_A * likelihood_A
posterior_B = prior_B * likelihood_B

# Normalización (para que la suma de las probabilidades sea 1)
sum_posteriors = posterior_A + posterior_B
posterior_A_normalized = posterior_A / sum_posteriors
posterior_B_normalized = posterior_B / sum_posteriors

# Resultados
print("Probabilidad posterior de Hipótesis A (dado sesgado):", posterior_A_normalized)
print("Probabilidad posterior de Hipótesis B (dado equilibrado):", posterior_B_normalized)
