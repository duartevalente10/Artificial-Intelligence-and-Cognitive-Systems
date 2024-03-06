from modelo_mundo_2d import ModeloMundo2D
from estado import Estado
from accao import Accao
from typing import List
from frente_onda import FrenteOnda
from typing import Dict

'''
Class que implementa os metodos que produzem um plano de acao conforme os estados passados e os objetivos 
ao calcular os valores correspondentes a cada accao
'''

class PlanFrenteOnda(FrenteOnda):

    # construtor da class 
    def __init__(self, modelo: ModeloMundo2D, gama: float = 0.98, valor_max: float = 1):
        self.modelo = modelo
        self.gama = gama
        self.valor_max = valor_max

    # retorna os valores da propagação dos estados
    def V(self) -> Dict[Estado, float]:
        return self._V
 
    # produz um plano de estrategia global
    # dado um estado indica qual a ação
    def planear(self, objetivos: List[Estado]) -> dict[Estado, Accao]:
        # propagar os estados atravez da função propagar da class Frente Onda
        self._V = super().propagar_valor(self.modelo, objetivos)
        # defenir a plotica com base nos estados que maximizam
        print("AQUIiiiii",self.modelo._A)
        politica = {estado: max(self.modelo._A,
                                key= lambda accao: self.valor_accao(estado, accao))
                                for estado in self.modelo._S
                                if estado not in objetivos}
        return politica, self._V

    # calcular o valor de uma acao num determinado estado
    def valor_accao(self, estado: Estado, accao: Accao) -> float: 
        # utiliza a função T do modelo para calcular o proximo estado do modelo2D 
        novo_estado = self.modelo.T(estado, accao)
        # retorna esse estado
        return self._V.get(novo_estado, float('-inf'))