# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
import pandas as pd
import numpy as np
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator

# Datos de ejemplo para clasificación binaria
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 1, 1, 0])

# Convertir los datos en un dataframe de pandas
data_df = pd.DataFrame({'Feature 1': X_train[:, 0], 'Feature 2': X_train[:, 1], 'Class': y_train})

# Crear una red bayesiana para modelar la relación entre las características y la clase
model_bayesiano = BayesianModel([('Feature 1', 'Class'), ('Feature 2', 'Class')])

# Entrenar la red bayesiana con los datos
model_bayesiano.fit(data_df, estimator=MaximumLikelihoodEstimator)

# Verificar si el modelo es válido y consistente
print("El modelo es válido y consistente?", model_bayesiano.check_model())
