import random as rn
import numpy as np
import pandas as pd
import os
from heapq import nsmallest

class Config:

    #CONSTRUCTOR
    def __init__(self):
        self.Entradas = []
    
    #METODO PARA GENERAR PESOS
    def Generar_pesos(self, row, col):
        Matriz = []
        for N in range(row):
            Fila = []
            for M in range(col):
                Fila.append(round(rn.uniform(-1, 1), 2))
            Matriz.append(Fila)
        return Matriz

    #METODO PARA GENERAR UMBRALES
    def Generar_Umbrales(self, row):
        Fila = []
        for N in range(row):
            Fila.append(round(rn.uniform(-1, 1), 2))
        return Fila

    # LLENAR MATRICES ENTRADAS Y SALIDAS
    def NormalizarDatos(self, ruta):
        Matriz = pd.read_csv(ruta, delimiter=' ')
        col = Matriz.columns
        column = Matriz.to_numpy()

        for i in range(len(col)):
            Fila = []
            for j in range(len(column)):
                Fila.append(column[j,i])
            self.Entradas.append(Fila)

    # INICIAR ENTRENAMIENTO
    def Entrenar(self, rataAprendizaje, errorMaximo, numeroIteraciones):
        self.Entradas = self.NormalizarEntradas(self.Entradas)
        print(np.array(self.Entradas))

    # LIMPIAR CAPAS
    def Limpiar(self):
        self.capas = []

    def NormalizarEntradas(self, entrada):
        entradas = []
        for i in range(len(entrada[0])):
            aux = []
            for j in range(len(entrada)):
                aux.append(entrada[j][i])
            entradas.append(aux)
        return entradas

if __name__ == '__main__':
    print("Hola")