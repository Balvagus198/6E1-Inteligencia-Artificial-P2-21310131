# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, binom

# Parámetros del prior Beta
alpha_prior = 1
beta_prior = 1

# Datos del experimento binomial (éxitos y fracasos)
num_observaciones = 100
num_exitos = 60

# Actualización del prior utilizando el teorema de Bayes
alpha_posterior = alpha_prior + num_exitos
beta_posterior = beta_prior + num_observaciones - num_exitos

# Crear distribuciones Beta para el prior y posterior
prior = beta(alpha_prior, beta_prior)
posterior = beta(alpha_posterior, beta_posterior)

# Generar datos para graficar las distribuciones
x = np.linspace(0, 1, 1000)
prior_pdf = prior.pdf(x)
posterior_pdf = posterior.pdf(x)

# Graficar las distribuciones
plt.figure(figsize=(10, 6))
plt.plot(x, prior_pdf, label='Prior Beta({}, {})'.format(alpha_prior, beta_prior))
plt.plot(x, posterior_pdf, label='Posterior Beta({}, {})'.format(alpha_posterior, beta_posterior))
plt.xlabel('Probabilidad de Éxito')
plt.ylabel('Densidad de Probabilidad')
plt.title('Aprendizaje Bayesiano: Prior y Posterior')
plt.legend()
plt.show()
