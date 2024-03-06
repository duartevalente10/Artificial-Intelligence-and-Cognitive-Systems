from abc import abstractproperty
from typing import List
from estado import Estado
from accao import Accao

'''
Classe abstrata do modelo do mundo 
'''

class ModeloMundo:
    def __init__(self, estados: List[Estado], acoes: List[Accao]):
        self._S = estados
        self._A = acoes

    # retorna o conjunto de estados do mundo
    @abstractproperty
    def S(self):
        '''Conjunto de estados'''

    # retorna o conjunto de ações possiveis
    @abstractproperty
    def A(self) -> List[Accao]:
        '''Acções possiveis'''

    # transições de estado
    # T: S*A → S – Função de transição de estado
    def T(self, s: Estado, a: Accao) -> Estado:
        '''Função de transição de estado'''

    # distancia
    def distancia(self, s: Estado, sn: Estado) -> float:
        '''calculo da distancia entre estados'''
