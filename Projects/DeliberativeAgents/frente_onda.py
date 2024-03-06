from typing import List, Dict
from modelo_mundo import ModeloMundo
from modelo_mundo_2d import ModeloMundo2D
from estado import Estado

'''
A classe FrenteOnda realiza a propagação de valores ou custos associados aos estados do modelo do mundo. 
Implementa a função propagar_valor que tem o objetivo de atualizar os valores associados aos estados do modelo do mundo.
'''

class FrenteOnda:

    # construtor ca classe
    def __init__(self, gama: float, valor_max: float):
        # fator de desconto
        self.gama = gama
        # valor maximo de cada estado
        self.valor_max = valor_max

    #  função para propagar os valores pelo modelo do mundo
    def propagar_valor(self, modelo: ModeloMundo2D, objetivos: List[Estado]) -> Dict[Estado, float]:
        # inicializar o campo de valores
        V = {}
        # inicializar os estados 
        frente_de_onda = []

        # adicionar os estados possiveis do modelo do mundo á lista e coloca os valores V de cada estado no valor maximo 
        for s in objetivos:
            V[s] = self.valor_max
            frente_de_onda.append(s)

        # enquanto existirem estados na frente de onda
        while frente_de_onda:
            s = frente_de_onda.pop(0)

            # precorre os estados adjacentes a cada possicao
            for s_adjacente in self.adjacentes(modelo, s):
                # atenuar o valor
                v = V[s] * self.gama * modelo.distancia(s, s_adjacente)

                # se o estado adjacente tiver um valor inferior adiciona à frente de onda
                if v > V.get(s_adjacente, float('-inf')):
                    V[s_adjacente] = v
                    frente_de_onda.append(s_adjacente)
        return V

    # estados que são adjacentes a um determinado estado
    def adjacentes(self, modelo: ModeloMundo2D, estado: Estado) -> List[Estado]:

        # lista de estados adjacentes
        estados_adjacentes = []

        #print("Todas as Accoes: ",modelo.A)
        # varrer todas as açoes
        for acao in modelo.A():
            # para cada ação calcular o adjacente desse estado e guardar numa lista
            print("Acao: ", acao)
            estado_adjacente = modelo.T(estado, acao)
            print("Estado adjacente: ", estado_adjacente)
            estados_adjacentes.append(estado_adjacente)

        print("Estados adjacentes: ", estados_adjacentes)
        # retornar a lista de estados adjacentes
        return estados_adjacentes
