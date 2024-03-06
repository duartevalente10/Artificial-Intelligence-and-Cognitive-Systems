from .aprend_ref import AprendRef
from agente.estado import Estado
from agente.accao import Accao
from ambiente.ambiente import Ambiente
from ambiente.elemento import Elemento
from .mec_aprend_ref import MecAprendRef
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output

'''
classe que interage com o ambiente utilizando o mecanismo de aprendizgem por reforço
a classe executa os episódios no ambiente, selecionando ações, observando estados, 
gerando reforços e aprendendo com base nessas interações 
'''

class AgenteAprendRef:

    # construtor da classe AgenteAprendRef
    def __init__(self, ambiente: Ambiente, mec_aprend: MecAprendRef, r_max: float =100):
        self.ambiente = ambiente
        self.mec_aprend = mec_aprend
        self.r_max = r_max
        self.__s, self.__elem = ambiente.observar()
    
        
    # metodo para executar os episodios
    def executar(self, num_episodios):
        num_pesos_episodio = []
        for _ in range(num_episodios):
            print("Numero do empisodio: ", _)
            self.__s = self.ambiente.reiniciar()
            self.__s, self.__elem = self.ambiente.observar()
            num_passos = 0
            while not self.fim_episodio():
                self.passo_episodio()
                num_passos += 1  
            num_pesos_episodio.append(num_passos)
            print(f"Número de passos no episódio {_}: {num_passos}")
        return num_pesos_episodio

    # fim de cada episodio
    def fim_episodio(self) -> bool:
        if self.__elem == Elemento.ALVO:
            return True
        return False
    
    def passo_episodio(self):
        # selecionar uma accao
        self.__a = self.mec_aprend.seleccionar_accao(self.__s)
        # executar essa accao
        self.ambiente.actuar(self.__a)
        # observar o resultado da accao e obter a nova possicao e o elemento dessa possicao
        sn, elem = self.ambiente.observar()
        # ober a reward ao gerar o reforco
        r = self.gerar_reforco(elem, self.__s, sn)
        # aprender com a accao efetuada
        self.mec_aprend.aprender(self.__s, self.__a, r, sn)
        # atualizar a possição atual para a nova possicao
        self.__s = sn
        # atualizar o elemento para o elemento atual
        self.__elem = elem
        # se o novo elemeto for um obstaculo volta á possição inicial
        if self.__elem == Elemento.OBSTACULO:
            self.__s = self.ambiente.reiniciar()

    # gerar gerfoco no seguinte episodio
    def gerar_reforco(self, elem: Elemento, s :Estado, sn: Estado) -> float:
        # Ação ótima
        if elem == Elemento.ALVO:
            print("Encontrou o alvo")
            return 1
        elif elem == Elemento.OBSTACULO:
            return -0.5
        else:
            return -0.1

   