from modelo_mundo import ModeloMundo
from estado import Estado
from typing import List
from accao import Accao
from math import dist

'''
Classe que expecializa a clase abstrata ModeloMundo e que implementa as funçoes da class abstrata
'''

class ModeloMundo2D(ModeloMundo):

    ALVO = '+'
    OBSTACULO = '#'

    # construtor da class 
    def __init__(self):
        # possiveis açoes
        accoes = [(0,1), (0,-1), (1,0), (-1,0)]
        self._A = accoes
        self.estados = []

    # retorna o conjunto de estados do mundo percepcao
    def S(self) -> List[Estado]:
        return self._S

    # retorna o conjunto de ações possiveis
    def A(self) -> List[Accao]:
        # Acções possiveis
        return self._A
    
    # get do valor de x_max
    @property
    def x_max(self) -> int:
        return self._x_max

    # get do valor de y_max
    @property
    def y_max(self) -> int:
        return self._y_max
    
    
    # função para calcular o proximo estado do modelo2D
    def T(self, s: Estado, a: Accao) -> Estado:
        '''Utiliza o metodo simular_accao'''
        return self.simular_accao(s,a)

    
    # função para calcular a distancia entre estados
    def distancia(self, s: Estado, sn: Estado) -> float:

        print("Estado 1: ",s)
        print("Estado 2: ",sn)
        # retornar o valor da distancia
        return dist(s, sn)

    # atualizar o modelo do mundo tendo em contra a sua presecao(listas do ambiente)
    def atualizar (self, precepcao):
        print("Precepcao: ",precepcao)
        self.elementos = precepcao
        # atualizar x_max e y_max
        self._x_max = len(precepcao[0]) # len da linha 
        self._y_max = len(precepcao) # numero de linhas
        # estados -> conjunto de possicoes que nao tem objstaculo
        # x entre 0 e x_max e y entre 0 e y_max e que o conteudo da precepcao nessa possicao nao é um obstaculo
        self._S = [(x,y) 
                        for x in range(self._x_max)
                        for y in range(self._y_max)
                        if precepcao[y][x] != self.OBSTACULO] 

    def obter_posicoes_alvo(self) -> List[Estado]:
        # lista de todos os estados em que a possicao é um alvo
        list_estados_alvo = [(x,y) for (x,y) in self._S
        if self.elementos[y][x] == self.ALVO]
        # retornar a posição do alvo
        return list_estados_alvo
    
    # funcao para simular uma acao ao encontrar o estado sucessor atravez do estado atual e da accao fornecida
    def simular_accao(self, estado: Estado, accao: Accao) -> Estado:
        # gera um estado sucessor cujo o estado é o x + dx , y + dy 
        (x,y) = estado
        (dx,dy) = accao
        estado_suc = (x + dx, y + dy)
        # verificar se o estado sucesor é valido
        if self.estado_valido(estado_suc):
            return estado_suc
        return estado

    # funcao para validar se o estado sucessor é valido
    def estado_valido(self, estado: Estado) -> bool:
        # passar as componentes x e y do estado
        (x,y) = estado

        # verificar se as coordenadas estão dentro dos limites
        if 0 <= x < self._x_max and 0 <= y < self._y_max:
            # verificar se a posicao esta vazia (' ')
            if self.elementos[y][x] == ' ':
                return True

        return False
        
