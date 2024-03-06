import os
import sys
import numpy as np

# Adicione o diretório raiz do seu projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classe_teste import TesteAprendRef
import matplotlib.pyplot as plt

NUM_AMBIENTE = 2
NUM_EPISODIOS = 100

# chamar a classe de teste
teste = TesteAprendRef()

# testar para o Qlearning
num_passos_episodio, politica_e = teste.testar(NUM_AMBIENTE, NUM_EPISODIOS, False, 0)

# testar para o QME
num_passos_episodio_exp, politica_exp = teste.testar(NUM_AMBIENTE, NUM_EPISODIOS, True, 0)

# teste valor inicial != de 0
num_passos_episodio_valor_otimista, politica_v_o = teste.testar(NUM_AMBIENTE, NUM_EPISODIOS, False, 1)

# mostar a politica no ecran
# gerar politica
# utilizar o qsa para mostar a melhor polica:
# para cada estado indicar a melhor ação desse estado

def plot_politica(politica):
    # Obter as posições e ações do dicionário
    posicoes = list(politica.keys())
    acoes = [acao.value for acao in politica.values()]

    # Extrair as coordenadas x e y
    x = [posicao[0] for posicao in posicoes]
    y = [posicao[1] for posicao in posicoes]

    # Mapear as ações para setas
    setas = {'↑': np.array([0, 1]), '↓': np.array([0, -1]), '←': np.array([-1, 0]), '→': np.array([1, 0])}
    vetores_acoes = [setas[acao] for acao in acoes]

    # Criar o gráfico de dispersão com setas
    fig, ax = plt.subplots()
    ax.quiver(x, y, np.array(vetores_acoes)[:, 0], np.array(vetores_acoes)[:, 1], angles='xy', scale_units='xy', scale=1, color='b')

    # Adicionar rótulos e título
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Política Obtida pelos Agentes')

    # Exibir o gráfico
    plt.show()

plot_politica(politica_e)
plot_politica(politica_exp)
plot_politica(politica_v_o)
print(politica_e)
print(politica_exp)
print(politica_v_o)

# visualizar a evolucao do agente ao longo dos episódios
plt.plot(num_passos_episodio, label="Q-Learning")

# visualizar a evolucao do agente ao longo dos episódios com memoria de experiencia
plt.plot(num_passos_episodio_exp, label="QME")

# visualizar a evolucao do agente ao longo dos episódios com memoria esparca com valores otimistas
plt.plot(num_passos_episodio_valor_otimista, label="Q-Learning Valor otimista")

plt.title("Ambiente %d" % NUM_AMBIENTE)
plt.xlabel("Episodio")
plt.ylabel("Numero de passos")
plt.legend()
plt.show()