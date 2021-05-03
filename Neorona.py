import numpy as np
import pandas as pd
import os
from heapq import nsmallest
from Funtions import *

class Neorona:

    #CONSTRUCTOR
    def __init__(self):
        self.Entradas = []
        self.func = Funtions()
    

    # LLENAR MATRICES ENTRADAS Y SALIDAS
    def NormalizarDatos(self, ruta):
        self.Entradas = []
        Matriz = pd.read_csv(ruta, delimiter=' ')
        col = Matriz.columns
        column = Matriz.to_numpy()

        for i in range(len(col)):
            Fila = []
            for j in range(len(column)):
                Fila.append(column[j,i])
            self.Entradas.append(Fila)

    # INICIAR ENTRENAMIENTO
    def Entrenar(self, rataAprendizaje, coeficieteVecindad, neuronas, numeroIteraciones, competencia):
        self.Entradas = self.func.NormalizarEntradas(self.Entradas)
        print('ENTRADAS:')
        print(np.array(self.Entradas))
        print()
        
        # INICIALIZAR PESOS
        pesos = self.func.Generar_pesos(len(self.Entradas[0]), neuronas)
        print('PESOS:')
        print(np.array(pesos))
        print()

        print('COMPETANCIA:', competencia)
        print()

        Iteracion = 1

        while True:

            DistanciasGanadoras = []
            Error = 0

            for entrada in self.Entradas:
                print('PATRON:', entrada)
                print()

                DistanciaEuclidiana = self.func.DistanciaEuclidiana(entrada, pesos)
                print('DISTANCIA EUCLIDIANA:')
                print(np.array(DistanciaEuclidiana))
                print()

                NeuronaVencedora = np.array(DistanciaEuclidiana).flat[np.abs(np.array(DistanciaEuclidiana) - coeficieteVecindad).argmin()]
                DistanciasGanadoras.append(NeuronaVencedora)
                print('COEFICIENTE DE VECINDAD:', coeficieteVecindad)
                print('NEURONA VENCEDOR:', NeuronaVencedora)
                print()

                vecina = 0
                if(competencia == 'BLANDA'):
                    dt = coeficieteVecindad + NeuronaVencedora
                    vecina = self.func.Blanda(DistanciaEuclidiana, dt)
                    print('NEURONAS VECINAS:', vecina)
                    print()
                else:
                    vecina = self.func.Dura(DistanciaEuclidiana, NeuronaVencedora)
                    print('NEURONAS VECINAS:', vecina)
                    print()
                
                pesos = self.func.ActualizarPesos(pesos, rataAprendizaje, NeuronaVencedora, vecina)
                print('PESOS ACTUALIZADOS')
                print(np.array(pesos))
                print()

            rataAprendizaje /= Iteracion
            Error = sum(DistanciasGanadoras) / len(self.Entradas)
            Iteracion += 1

            print('RATA:', rataAprendizaje)
            print('DISTANCIAS GANADORAS:', DistanciasGanadoras)
            print('ERROR DEL PATRON:', Error)
            print()

            #CONDICIONES DE PARADA
            if((Iteracion > numeroIteraciones) or Error <= 0.0005):
                break

        print('ITERACIONES:', Iteracion-1)
        print('ERROR FINAL:', Error)

    # LIMPIAR CAPAS
    def Limpiar(self):
        self.capas = []  

if __name__ == '__main__':
    print("Hola")