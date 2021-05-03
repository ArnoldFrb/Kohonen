import random as rn

class Funtions:

    #CONSTRUCTOR
    def __init__(self):
        print()
    
    #METODO PARA GENERAR PESOS
    def Generar_pesos(self, row, col):
        Matriz = []
        for N in range(row):
            Fila = []
            for M in range(col):
                Fila.append(round(rn.uniform(-1, 1), 2))
            Matriz.append(Fila)
        return Matriz
        
    # NORMALIZAR ENTRADAS 
    def NormalizarEntradas(self, entrada):
        entradas = []
        for i in range(len(entrada[0])):
            aux = []
            for j in range(len(entrada)):
                aux.append(entrada[j][i])
            entradas.append(aux)
        return entradas

    def DistanciaEuclidiana(self, entradas, pesos):
        dis = []
        for i in range(len(pesos[0])):
            _dis = 0
            for j in range(len(pesos)):
                _dis += pow((entradas[j] - pesos[j][i]), 2)
            dis.append(pow(_dis, 0.5))
        return dis

    def Blanda(self, distanciaEuclidiana, distanciaTotal):
        estado = []
        for dis in distanciaEuclidiana:
            if dis <= distanciaTotal:
                estado.append(True)
            else:
                estado.append(False)
        return estado

    def Dura(self, distanciaEuclidiana, vencedora):
        estado = []
        for dis in distanciaEuclidiana:
            if dis == vencedora:
                estado.append(True)
            else:
                estado.append(False)
        return estado

    def ActualizarPesos(self, pesos, rata, nerona, estado):
        for i in range(len(pesos[0])):
            for j in range(len(pesos)):
                if estado[i]:
                    pesos[j][i] = pesos[j][i] + (rata * nerona)
        return pesos
