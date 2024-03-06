from ambiente.ambiente import Ambiente
from agente.accao import Accao
from aprend_ref.mec_aprend_ref import MecAprendRef
from aprend_ref.agente_aprend_ref import AgenteAprendRef
from typing import List

'''
classe para inicializar o ambiente, as accoes, o agente atraves do mecanismo de apnredigem e executar os episodios
'''

class TesteAprendRef:

    def testar(self, num_ambiente, num_episodios, exp, valor_inicial: float): 
        ambiente = Ambiente(num_ambiente)
        #accoes = List[Accao]
        accoes = [Accao.NORTE, Accao.SUL, Accao.ESTE, Accao.OESTE]
        mec_aprend_ref = MecAprendRef(accoes, 0.2, 0.5, 0.9, exp, valor_inicial)
        agente = AgenteAprendRef(ambiente, mec_aprend_ref)
        num_passos_episodio = agente.executar(num_episodios)
        politica = mec_aprend_ref.obterPolitca()
        return num_passos_episodio, politica
    

