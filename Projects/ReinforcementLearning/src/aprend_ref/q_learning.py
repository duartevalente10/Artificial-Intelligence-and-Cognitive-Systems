from .aprend_ref import AprendRef
from agente.estado import Estado
from agente.accao import Accao

'''
A classe QLearning é responsavel por atualizar os valores Q à medida que o agente interage com o ambiente.
Valor este que representa o conhecimento do a gente sombre a qualidade das acções em diferentes estados.
Assim, atravez do estado, accao atual, da recompensa, do proximo estado, da proxmima acção, da taxa de aprendisagem e com o fator de desconto,
é possivel calcular um novo valor de Q e atualizar a memoria. 
'''

class QLearning(AprendRef):

    # metodo chamado quando o agente interage com o ambiente recebendo o estado , a accao, a recompensa e o proximo estado
    def aprender(self, s: Estado, a: Accao, r: float, sn: Estado, an: Accao = None):
        # calcular a proxima ação utilizado o e-gred
        an = self.sel_accao.accao_sofrega(sn)
        print("Proxima accao:", an)
        # obter o valor atual q para o estado "s" e accao "a" na memoria de aprendisagem
        #qsa = self.mem_aprend.q(s, a)
        qsa = self.mem_aprend.q(s, a)
        print("valor atual de Q:", qsa)
        # obter o valor q para o proximo estado "sn" e para a proxima accao "an"
        qsnan = self.mem_aprend.q(sn, an)
        print("Valor de q para o proximo estado:", qsnan)
        # utilizar os valores de q para o estado e accao atual e para o estado e accao seguintes juntamente com a taxa de aprendisagem alfa
        # e com o fator gama pra calcular o novo valor de q 
        print("Alfa: ", self.alfa)
        print("Reward:", r)
        q = qsa + self.alfa * (r + self.gama * qsnan - qsa)
        #print("Q-Value", q)
        # atualizar a memoria com o novo valor para o estado e accao atual
        self.mem_aprend.atualizar(s, a, q)

