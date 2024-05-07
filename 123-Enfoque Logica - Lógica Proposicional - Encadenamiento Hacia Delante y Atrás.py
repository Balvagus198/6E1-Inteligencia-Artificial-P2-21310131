# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class Hecho:
    def __init__(self, nombre, valor=False):
        self.nombre = nombre
        self.valor = valor

    def __repr__(self):
        return f"{self.nombre}={self.valor}"


class Regla:
    def __init__(self, antecedentes, consecuente):
        self.antecedentes = antecedentes
        self.consecuente = consecuente

    def evaluar(self, hechos):
        for antecedente in self.antecedentes:
            if not any(hecho.nombre == antecedente.nombre and hecho.valor for hecho in hechos):
                return False
        return True

    def aplicar_consecuente(self, hechos):
        if self.evaluar(hechos):
            return self.consecuente
        return None


class MotorEncadenamientoAdelante:
    def __init__(self, reglas, hechos):
        self.reglas = reglas
        self.hechos = hechos

    def encadenamiento_adelante(self):
        cambios = True
        while cambios:
            cambios = False
            for regla in self.reglas:
                consecuente = regla.aplicar_consecuente(self.hechos)
                if consecuente and not any(hecho.nombre == consecuente.nombre for hecho in self.hechos):
                    self.hechos.append(consecuente)
                    cambios = True


class MotorEncadenamientoAtras:
    def __init__(self, reglas, hechos):
        self.reglas = reglas
        self.hechos = hechos

    def encadenamiento_atras(self, objetivo):
        if any(hecho.nombre == objetivo.nombre and not hecho.valor for hecho in self.hechos):
            return False

        for regla in self.reglas:
            if regla.consecuente.nombre == objetivo.nombre:
                antecedentes_satisfechos = True
                for antecedente in regla.antecedentes:
                    if not any(hecho.nombre == antecedente.nombre and hecho.valor for hecho in self.hechos):
                        antecedentes_satisfechos = False
                        break
                if antecedentes_satisfechos:
                    if objetivo.valor:
                        self.hechos.append(objetivo)
                    return True

        for regla in self.reglas:
            for antecedente in regla.antecedentes:
                if antecedente.nombre == objetivo.nombre:
                    if self.encadenamiento_atras(antecedente):
                        return True

        return False


# Crear hechos
p = Hecho("p", True)
q = Hecho("q", True)
r = Hecho("r", True)

# Crear reglas
regla1 = Regla([p, q], r)

# Ejemplo de encadenamiento hacia adelante
motor_adelante = MotorEncadenamientoAdelante([regla1], [p, q])
motor_adelante.encadenamiento_adelante()
print("Resultado encadenamiento hacia adelante:", motor_adelante.hechos)

# Ejemplo de encadenamiento hacia atrás
motor_atras = MotorEncadenamientoAtras([regla1], [r])
objetivo = Hecho("p", True)
resultado_atras = motor_atras.encadenamiento_atras(objetivo)
print("Resultado encadenamiento hacia atrás:", resultado_atras)
