from .sel_accao import SelAccao
from agente.accao import Accao
from agente.estado import Estado
from .memoria_aprend import MemoriaAprend
import random
from typing import List

"""
A classe EGreedy é uma implementação da estratégia epsilon-greedy,
Esta estrategia permite que o agente escolha entre explorar ações aleatoriamente e pode aproveitar a ação com maior probabilidade de recompensa com base em seu conhecimento atual.
"""

class EGreedy(SelAccao):

    # constrotor da classe
    def __init__(self, mem_aprend: MemoriaAprend, accoes: List[Accao], epsilon: float):
        self.mem_aprend = mem_aprend
        self.accoes = accoes
        self.epsilon = epsilon

    def seleccionar_accao(self, s: Estado) -> Accao:
        if random.random() > self.epsilon:
            return self.aproveitar(s)
        else:
            return self.explorar()
        
    def aproveitar(self, s: Estado) -> Accao:
        return self.accao_sofrega(s)
    
    def explorar(self) -> Accao:
        return random.choice(self.accoes)
    
    # seleciona uma determinada ação onde o valor de Q é maximo
    def accao_sofrega(self, s: Estado) -> Accao:
        random.shuffle(self.accoes)
        # encontrar a ação com o valor máximo
        q_values = {a: self.mem_aprend.q(s, a) for a in self.accoes}
        acao_maxima = max(q_values, key=q_values.get)
        return acao_maxima