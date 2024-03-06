from .memoria_aprend import MemoriaAprend
from agente.estado import Estado
from agente.accao import Accao

'''
A classe MemoriaEsparsa, tem como objetivo criar uma memória para permitir ao agente 
tomar decisões informadas. Assim, as informações relativas aos pares Estado - Accao são 
armazenadas nesta memoria de maneira a avaliarem a qualidade das ações em diferentes estados
'''

class MemoriaEsparsa(MemoriaAprend):

    # construtor da classe
    def __init__(self, valor_omissao: float = 0):
        # valor default para caso esteja vazio
        self.valor_omissao = valor_omissao
        # dicionario que vai sendo atualizado
        self.memoria = {}
        # guardar os estados
        self.estados = set()

    # função para atualizar o dicionario com o estado e acçao passada com o valor de q
    def atualizar(self, s: Estado, a: Accao, q: float):
        self.memoria[(s, a)] = q
        self.estados.add(s) # atualizar os estados 

    # função publica para devolver os estados
    def obterEstados(self):
        return self.estados

    # função para obter o valor correspondete a um estado e uma acção no dicionario
    def q(self, s: Estado, a: Accao) -> float:
        valor = self.memoria.get((s, a), self.valor_omissao)
        #print("Estado: ", s)
        #print("Acao: ", a)
        #print("Valor: ", valor)
        return valor
    