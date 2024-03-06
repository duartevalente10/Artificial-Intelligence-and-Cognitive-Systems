from agente_delib import AgenteDelib
from modelo_mundo_2d import ModeloMundo2D
from plan_frente_onda import PlanFrenteOnda
from typing import List
from estado import Estado
from defamb import DEF_AMB
from vis_valor_pol import VisValorPol
from estado import Estado

'''
Class que implementa os metodos abstratos da class AgenteDelib e que obtem a prececao do ambiente,
atualiza as crencas do agente, gera uma lista de objetivos dos estados que o agente pretende atingir,
retornar um plano utilizando o planeador e executa o plano que encontrou
'''

# classe do agente que deriva da implementação dos métodos abstratos da class AgenteDelib
class AgenteFrenteOnda(AgenteDelib):

    ALVO = '+'
    OBSTACULO = '#'

    # construtor do agente
    def __init__(self, ambiente: int):
        self.num_ambiente = ambiente
        self.modelo = ModeloMundo2D()
        self.plan_frente_onda = PlanFrenteOnda(self.modelo)
        self.visualizar = VisValorPol
        self.elementos = None

    # implementar a class precepcionar
    def precepcionar(self):
        return DEF_AMB[self.num_ambiente]

    # implementar a class actualizar as crencas do agente
    def actualizar_crencas(self, precepcao):
        # atualizar o modelo do mundo
        self.modelo.atualizar(precepcao)
        self.elementos = precepcao 

    # gerar uma lista de objetivos dos estados que o agente pretende atingir
    def deliberar(self) -> List[Estado]: 
        # produzir uma lista das posicoes onde existem alvos
        # utiliza o metodo do modelo do mundo 2d para obter esta lista
        self._S = self.modelo.S()
        list_estados_alvo = ModeloMundo2D.obter_posicoes_alvo(self)
        return list_estados_alvo

    # retornar um plano utilizando o planeador
    def planear(self, objetivos: List[Estado]):
        objetivos = self.deliberar()
        plano, valores = self.plan_frente_onda.planear(objetivos)
        return plano, valores

    # visualizar o plano com a politica que o agente utiliza para se movimentar
    def executar_plano(self, plano, valores):
        self.visualizar.mostrar(self.modelo._x_max , self.modelo.y_max, valores ,plano)
