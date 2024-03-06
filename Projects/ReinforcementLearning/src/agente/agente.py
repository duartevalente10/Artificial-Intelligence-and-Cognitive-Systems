from .accao import Accao

class Agente:

    def __init__(self, ambiente, mec_aprend):
        # construtor do agente
        self.s = None
        self.sInic = self.ambiente._obter_posicao_inicial()
        self.a = None
        self.ambiente = ambiente
        self.mec_aprend = mec_aprend

    def executar(self):
        # accoes a executar pelo agente sombre o ambiente
        pass

    def gerar_reforco(self):
        # metodo do agente preceber e gerar conhecimento
        pass

    def tomar_accao(self, accao):
        # accao que o agente efetua no ambiente
        self.ambiente.actuar(accao)

    def observar_ambiente(self):
        # observar o ambiente e retorna a posição atual e o elemento nessa posição
        return self.ambiente.observar()

    def reiniciar(self):
        # retorna à posição inicial no ambiente
        self.posicao = self.ambiente.reiniciar()

    def mostrar_politica(self, politica):
        # mostrar politica de acção no ambiente
        self.ambiente.mostrar_politica(politica)
    
    
    
