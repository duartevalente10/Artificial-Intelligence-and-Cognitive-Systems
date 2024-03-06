from agente.estado import Estado
from agente.accao import Accao
from .sel_accao import SelAccao
from .memoria_aprend import MemoriaAprend

"""
A sub-classe AprendRef, serve como base para ser utilizada por outras classes para aprender sobre determinados valores de input
Como entrada, receve a memoria de aprendisagem (do tipo MemoriaAprend), a seleção de Accao, o valor alfa( taxa de aprendisagem) e o valor gamma
A funcao aprender ainda nao esta implementada pois deve ser implementada por classes que herdem esta mesma classe
"""

class AprendRef:
    def __init__(self, mem_aprend: MemoriaAprend, sel_accao: SelAccao, alfa: float, gama: float):
        self.mem_aprend = mem_aprend
        self.sel_accao = sel_accao
        self.alfa = alfa
        self.gama = gama
        
    def aprender(s: Estado, a: Accao, r: float, sn: Estado, an:Accao=None):
        raise NotImplementedError