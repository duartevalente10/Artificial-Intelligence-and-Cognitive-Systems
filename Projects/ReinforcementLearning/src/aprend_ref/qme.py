from .q_learning import QLearning
from .memoria_aprend import MemoriaAprend
from .memoria_experiencia import MemoriaExperiencia
from agente.estado import Estado
from agente.accao import Accao

'''
A classe QME, estende as funcionalidades do Q-learning ao adicionar a memória de experiência 
e a capacidade de realizar simulações com base nessas experiências para melhorar ainda mais o modelo. 
Assim, atraves de um estado, accao, reward e proximo estado, é possivel registar na memoria novas experiencias
e simular a aprendisagem com as amostaras presentes na memoria e aprende com as amostras
'''

class QME(QLearning):

    # construtor da classe
    def __init__(self, mem_aprend: MemoriaAprend, sel_acao, alfa: float, gama: float, num_sim: int, dim_max: int):
        super().__init__(mem_aprend, sel_acao, alfa, gama)
        self.num_sim = num_sim
        self.dim_max = dim_max
        self.memoria_experiencia = MemoriaExperiencia(dim_max)

    # função apra simular com as amostras da memoria de experiencia
    def simular(self):
        # conjunto de amostras guardadas na memoria de experiencia
        amostras = self.memoria_experiencia.amostrar(self.num_sim)
        # para cada amostra aprender pelo QLearning
        for s, a, r, sn in amostras:
            super().aprender(s, a, r, sn)

    # função para aprender e atualiar a memoria de experienceia
    def aprender(self, s: Estado, a: Accao, r: float, sn: Estado):
        super().aprender(s, a, r, sn)
        # criar a nova experiencia
        experiencia = (s, a, r, sn)
        # registar a experiencia na memoria
        self.memoria_experiencia.atualizar(experiencia)
        self.simular()