from agente.estado import Estado
from agente.accao import Accao
from .memoria_aprend import MemoriaAprend

'''
A sub-classe SelAccao serve como base para utilizada por outras classes para selecionar uma ação a ser desempenhada com base na aprendisagem anterior
Assim, como entrada, esta sub-classe, deve recever a memoria de aprendisagem (do tipo MemoriaAprend)
Já em relação ao metodo seleccionar_accao, qualquer classe que herde esta subclasse, deve ser implementada esta função para selecionar a ação.
'''

class SelAccao:

    # construtor da classe
    def __init__(self, mem_aprend: MemoriaAprend):
        self.mem_aprend = mem_aprend

    # função para selecionar ações
    def seleccionar_accao(self, s: Estado) -> Accao:
        raise NotImplementedError
    