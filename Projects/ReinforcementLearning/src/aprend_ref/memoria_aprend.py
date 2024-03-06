from agente.estado import Estado
from agente.accao import Accao

'''
Classe abstrata para ser implementada pela memoria esparsa
Define as funções atualizar e q, nao implementadas, pois seram implementadas nas classe memoria esparsa
'''

class MemoriaAprend:
    def atualizar(self, s: Estado, a: Accao, q: float) -> float:
        raise NotImplementedError

    def q(self, s: Estado, a: Accao) -> float:
        raise NotImplementedError