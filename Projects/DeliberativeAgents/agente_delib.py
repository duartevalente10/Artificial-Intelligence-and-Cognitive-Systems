from abc import ABC, abstractmethod
from estado import Estado
from typing import List

'''
Class abstrata do agente que possui o metodo executar que vai executar todos os metodos abstratos, precepcionar,
actualizar_crencas, deliberar, planear, executar_plano
'''

class AgenteDelib(ABC):

    # função executar 
    def executar(self):
        # observa o mundo
        precepcao = self.precepcionar()
        # atualiza as crencas do agente
        self.actualizar_crencas(precepcao)
        # delibra o que fazer 
        objetivos = self.deliberar()
        # planea como fazer ao gerar um plano de accao
        plano, valores = self.planear(objetivos)
        # executa o plano de açao
        self.executar_plano(plano, valores)

    @abstractmethod
    def precepcionar(self):
        pass

    @abstractmethod
    def actualizar_crencas(self, precepcao):
        pass

    @abstractmethod
    def deliberar(self) -> List[Estado]:
        pass

    @abstractmethod
    def planear(self, objetivos: List[Estado]):
        pass

    @abstractmethod
    def executar_plano(self, plano):
        pass
        