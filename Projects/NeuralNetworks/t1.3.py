import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

# classe RedeNeuronal
class RedeNeuronal:
    def __init__(self, taxa_aprendizagem=0.1, momento=0.0, ordem_apresentacao="fixa"):
        # iniciar a taxa de aprendizagem, momento e ordem de apresentação conforme os fornecidos na configuração do modelo
        self.taxa_aprendizagem = taxa_aprendizagem
        self.momento = momento
        self.ordem_apresentacao = ordem_apresentacao

        # criar o modelo
        self.model = self.criar_modelo() 
        self.hist_treino = None # var para mostrar graficamente a evolução do modelo

    # função para criar o modelo
    def criar_modelo(self):
        # tipo do modelo
        model = Sequential()
        # adicionar as camadas do modelo e o modo de ativação dos neurônios
        model.add(Dense(units=2, activation='sigmoid', input_dim=2)) # input_dim = número de entradas na rede
        model.add(Dense(units=1, activation='sigmoid'))
        
        # otimizador da rede através da taxa de aprendizagem e da var de momento adicionadas
        optimizer = SGD(learning_rate=self.taxa_aprendizagem, momentum=self.momento)
        # compilar o modelo com o cálculo do loss utilizado o MSE e o otimizador definido anteriormente
        model.compile(loss='mean_squared_error', optimizer=optimizer)
        return model

    # função para treinar a rede em 2000 iterações
    def treinar(self, X, y, epochs=2000):
        # se a ordem de apresentação dos dados for aleatória
        if self.ordem_apresentacao == "aleatoria":
            # fazer shuffle dos dados e das labels correspondentes
            X, y = shuffle(X, y)
        
        # introduzir os dados e as respetivas labels na rede de forma a treinar a rede
        hist_treino = self.model.fit(X, y, epochs=epochs, verbose=0)
        # guardar os dados da evolução do treino
        self.hist_treino = hist_treino.history

    # função para prever a label respetiva à input conforme o modelo treinado
    def prever(self, X):
        return self.model.predict(X)

# função para mostrar a curva de aprendizagem do modelo
def plot_curva_aprendizagem(hists_treino, titulos):
    plt.figure()
    for i, hist_treino in enumerate(hists_treino):
        plt.plot(hist_treino['loss'], label=titulos[i])
        erro_final = hist_treino['loss'][-1]  # Obtém o último valor do erro no histórico
        print(f"Erro final para {titulos[i]}: {erro_final}")
    plt.title("Curva de Aprendizagem")
    plt.xlabel('Época')
    plt.ylabel('Erro')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # inputs da rede
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # labels correspondentes a cada input
    y = np.array([0, 1, 1, 0])

    # diferentes configurações da rede de forma a encontrar os parâmetros que obtêm um melhor desempenho 
    configs = [
        {"taxa_aprendizagem": 0.1, "momento": 0.1, "ordem_apresentacao": "fixa"},
        {"taxa_aprendizagem": 0.1, "momento": 0.9, "ordem_apresentacao": "fixa"},
        {"taxa_aprendizagem": 0.5, "momento": 0.1, "ordem_apresentacao": "fixa"},
        {"taxa_aprendizagem": 0.5, "momento": 0.9, "ordem_apresentacao": "fixa"},
        {"taxa_aprendizagem": 0.1, "momento": 0.1, "ordem_apresentacao": "aleatoria"},
        {"taxa_aprendizagem": 0.1, "momento": 0.9, "ordem_apresentacao": "aleatoria"},
        {"taxa_aprendizagem": 0.5, "momento": 0.1, "ordem_apresentacao": "aleatoria"},
        {"taxa_aprendizagem": 0.5, "momento": 0.9, "ordem_apresentacao": "aleatoria"}
    ]

    hists_treino = []
    titulos = []

    # treinar um modelo para cada configuração, prever os resultados com base no modelo treinado e mostrar a curva de aprendizagem do modelo
    for i, config in enumerate(configs):
        # definir a rede e as suas configurações
        rede = RedeNeuronal(**config)
        print(f"Configuração {i+1}: Taxa de Aprendizagem={config['taxa_aprendizagem']}, Momento={config['momento']}, Ordem de Apresentação={config['ordem_apresentacao']}")
        # treinar a rede
        rede.treinar(X, y)
        # prever as labels utilizando o modelo treinado
        previsoes = rede.prever(X)
        print(f"Previsões: {previsoes.flatten()}")
        
        hists_treino.append(rede.hist_treino)
        titulos.append(f"Configuração {i+1}")

    # plot da curva de aprendizagem
    plot_curva_aprendizagem(hists_treino, titulos)
