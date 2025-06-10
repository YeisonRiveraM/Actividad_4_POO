import math

class Notas:
    def __init__(self):
        self.listaNotas = [0, 0, 0, 0, 0]

    def calcularPromedio(self):
        sumaAcumulada = 0
        for i in range(0, 5):
            sumaAcumulada += self.listaNotas[i]
        return sumaAcumulada/5
    
    def calcularDesviacion(self):
        promedio = self.calcularPromedio()
        suma_cuadrados_dif = 0
        for i in range(5):
            suma_cuadrados_dif += (self.listaNotas[i] - promedio)**2
        return math.sqrt(suma_cuadrados_dif / 4)
    
    def calcularMenor(self):
        return min(self.listaNotas)
    
    def calcularMayor(self):
        return max(self.listaNotas)
    
