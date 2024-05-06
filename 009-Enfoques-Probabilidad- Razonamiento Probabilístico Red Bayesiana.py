
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Crear la estructura de la Red Bayesiana
modelo = BayesianModel([('Alarma', 'Robo'), ('Terremoto', 'Robo')])

# Definir las distribuciones condicionales de probabilidad (CPDs)
cpd_terremoto = TabularCPD(variable='Terremoto', variable_card=2,
                           values=[[0.99], [0.01]])
cpd_alarma = TabularCPD(variable='Alarma', variable_card=2,
                         values=[[0.95, 0.01], [0.05, 0.99]],
                         evidence=['Terremoto'], evidence_card=[2])
cpd_robo = TabularCPD(variable='Robo', variable_card=2,
                       values=[[0.999, 0.06, 0.71, 0.05],
                               [0.001, 0.94, 0.29, 0.95]],
                       evidence=['Alarma', 'Terremoto'], evidence_card=[2, 2])

# Asociar las CPDs con el modelo
modelo.add_cpds(cpd_terremoto, cpd_alarma, cpd_robo)

# Comprobar si la Red Bayesiana es válida
if modelo.check_model():
    print("La Red Bayesiana es válida.")

    # Crear el motor de inferencia
    inferencia = VariableElimination(modelo)

    # Calcular la probabilidad de que haya un robo dado que suena la alarma y hay un terremoto
    resultado = inferencia.query(variables=['Robo'], evidence={'Alarma': 1, 'Terremoto': 1})
    print("Probabilidad de robo dado alarma y terremoto:", resultado.values[1])
else:
    print("La Red Bayesiana no es válida.")
