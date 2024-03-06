import random

'''
A classe MemoriaExperiencia, tem como objetivo criar uma memória que consegue
armazenar e recuperar experiências passadas, para permitir ao agente tomar 
decisões informadas com base na experiencia.
'''

class MemoriaExperiencia:

    # construtor da classe
    def __init__(self, dim_max: int):
        # dimenção maxima
        self.dim_max = dim_max
        # lista da memoria
        self.memoria = []

    # função atualizar a memoria
    def atualizar(self, e):
        # verificar se a memoria já esta na dimenção maxima
        if len(self.memoria) == self.dim_max:
            # eliminar o mais antigo da lista
            del(self.memoria[0])
        self.memoria.append(e)

    # função que devolve o valor minimo do valor m com a dimenção da memoria
    def amostrar(self, n):
        n_amostras = min(n, len(self.memoria))
        return random.sample(self.memoria, n_amostras)