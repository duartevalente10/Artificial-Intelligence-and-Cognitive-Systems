from estado import Estado
from accao import Accao
from typing import Dict
import matplotlib.pyplot as plt

# class que possiu um metodo para mostar o plano e a politica do agente
class VisValorPol:
    
    # metodo que mostra a plitica e o plano do angente no ambiente
    def mostrar(x_max:int, y_max: int, V: Dict[Estado, float], politica: Dict[Estado, Accao]):
        # 
        fig, grafico = plt.subplots()
        fig.suptitle("Valores e Politica")

        # defenir os eixos
        X = range(x_max) # eixo X
        Y = range(y_max) # eixo Y

        # Z lista de listas em que cada elemento é o valor na possição
        Z = [[V.get((x, y),0) for x in X] for y in Y]
 
        # accao por omissao para os sitios onde não à obstaculos
        ACCAO_OMISSAO = (0,0)
        # lista de lista em que cada dx tem os valores dessa linha
        DX = [[politica.get((x, y), ACCAO_OMISSAO)[0] for x in X] for y in Y]
        DY = [[-politica.get((x, y), ACCAO_OMISSAO)[1] for x in X] for y in Y]

        # mostrar o gráfico
        grafico.imshow(Z)
        grafico.quiver(X, Y, DX, DY, scale_units="xy", scale=2)
        plt.show()