from agente.accao import Accao
from agente.estado import Estado
from typing import List
from .e_gredy import EGreedy
from .q_learning import QLearning
from .memoria_esparsa import MemoriaEsparsa
from .qme import QME

'''
Classe do mecanismo de aprendisagem por reforco
Obtem a memoria das acoes e estados já armasenada pela classe MemoriaEsparsa, 
Seleciona uma accao com base na memoria anterior,
Atualiza o conhecimento sobre as acoes e estados atraves da classe QLearning
Tem o objetivo de efetuar e aprender com as ações do agente e retornar qual a ação que se deve execurar de seguida
Assim, esta classe necessita de outras sublasses para puder efetuar entao a aprendisagem (AprendRef, SelAccao, Esparsa)
Atraves do metodo aprender, é possivel atualizar o conhecimento sobre o ambiente ao invocar os metodos da subclasse MemoriaAprend
Por fim a clasase tambem utiliza o metodo seleccionar_accao para, atraves da classe EGreedy obter a ação que este deve executar
'''

class MecAprendRef:
    # construtor da classe
    def __init__(self, accoes: List[Accao], epsilon = 0.2, alfa = 0.5, gama = 0.9, exp = bool, valor_inicial = int):
        # iniciar a memoria a um valor positivo para forcar todas as possibilidades
        self.epsilon = epsilon
        self.mem_aprend = MemoriaEsparsa(valor_inicial)
        self.sel_accao = EGreedy(self.mem_aprend,accoes, epsilon)
        if(exp != False):
            self.aprend_ref = QME(self.mem_aprend, self.sel_accao, alfa, gama, 100, 1000)
        else:
           self.aprend_ref = QLearning(self.mem_aprend,self.sel_accao, alfa, gama)

    # função de aprendisagem
    def aprender(self, s: Estado, a: Accao, r: float, sn: Estado):
        self.aprend_ref.aprender(s, a, r, sn)
    
    # função para retornar qual a ação indicada
    def seleccionar_accao(self, s: Estado) -> Accao:
        return self.sel_accao.seleccionar_accao(s)
    
    # metodo para obter as politicas 
    def obterPolitca(self):
        # dicionario que indica cada ação que maximiza a accao para cada estado
        politica = {
            s: self.sel_accao.accao_sofrega(s)
            for s in self.mem_aprend.obterEstados()
        }
        return politica
