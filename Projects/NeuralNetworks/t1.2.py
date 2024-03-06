import numpy as np
import matplotlib.pyplot as plt

# função de ativação
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# função de ativação derivada para ser utilziada na retropropagação
def sigmoidDeriv(x):
    return x * (1 - x)

# classe RedeNeuronal
class RedeNeuronal:
    def __init__(self, camada_entrada, num_neuronios_escondida, camada_saida):
        # iniciar os pressos aleatoriamente pois vao ser ajustados durante o treino do modelo
        self.pesos_entrada = np.random.uniform(-1, 1, (camada_entrada, num_neuronios_escondida))
        self.pesos_saida = np.random.uniform(-1, 1, (num_neuronios_escondida, camada_saida))

        # iniciar os bias aleatoriamente pois vao ser ajustados durante o treino do modelo
        self.bias_escondida = np.random.uniform(-1, 1, (1, num_neuronios_escondida))
        self.bias_saida = np.random.uniform(-1, 1, (1, camada_saida))


    def train(self, X, y, learning_rate, epochs):
        error_history = [] # var para guardar os valores dos erros para mostrar gráficamente
        for epoch in range(epochs):
            # propagar pela rede
            hidden_layer_input = np.dot(X, self.pesos_entrada) + self.bias_escondida
            hidden_layer_output = sigmoid(hidden_layer_input)
            output_layer_input = np.dot(hidden_layer_output, self.pesos_saida) + self.bias_saida
            output_layer_output = sigmoid(output_layer_input)

            # calcular o erro
            error = y - output_layer_output # comparar os resultados com o que era suposto obter
            error_history.append(np.mean(np.abs(error))) # adicionar à history para mostrar nos graficos

            # retropropagacao
            delta_output = error * sigmoidDeriv(output_layer_output)
            error_hidden = delta_output.dot(self.pesos_saida.T)
            delta_hidden = error_hidden * sigmoidDeriv(hidden_layer_output)

            # atualizar os pesos e os bias
            self.pesos_saida += hidden_layer_output.T.dot(delta_output) * learning_rate
            self.pesos_entrada += X.T.dot(delta_hidden) * learning_rate
            self.bias_saida += np.sum(delta_output, axis=0, keepdims=True) * learning_rate
            self.bias_escondida += np.sum(delta_hidden, axis=0, keepdims=True) * learning_rate

        return error_history

    # função para prever valores
    def predict(self, X): 
        # propagar os valores de entrada pela rede e retorna a output da rede como resultado
        hidden_layer_input = np.dot(X, self.pesos_entrada) + self.bias_escondida
        hidden_layer_output = sigmoid(hidden_layer_input)
        output_layer_input = np.dot(hidden_layer_output, self.pesos_saida) + self.bias_saida
        output_layer_output = sigmoid(output_layer_input)
        return output_layer_output

# função que defene as inputs e parametros da rede e do treino e que mostra as previzoes e gráficos de evoluçao da rede
def train_predict_plot(operator):
    # conjunto de entrada da rede
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    
    # defenir o conjunto que se pretende obter tendo em conta o operador escolhido
    if operator == "OR":
        y = np.array([[0], [1], [1], [1]])
    elif operator == "AND":
        y = np.array([[0], [0], [0], [1]])
    elif operator == "NOT":
        X = np.array([[0], [1]]) # para o not o conjunto de entrada da rede é difernte
        y = np.array([[1], [0]])
    elif operator == "XOR":
        y = np.array([[0], [1], [1], [0]])
    else:
        raise ValueError("Operador desconhecido")

    camada_entrada = X.shape[1] # número de entradas na rede
    num_neuronios_escondida = 2  # núemro de neuronios da camada escondida
    camada_saida = 1 # número de saidas

    # criar a rede
    redeNeuronal = RedeNeuronal(camada_entrada, num_neuronios_escondida, camada_saida)

    # treino
    learning_rate = 0.1 # taxa de aprendizagem
    epochs = 10000 # numero de epocas de treino
    error_history = redeNeuronal.train(X, y, learning_rate, epochs) # history para mostrar gráficamente a evolução da rede

    # imprimir as previsoes do modelo
    print(f"Operador lógico {operator}:")
    for i in range(X.shape[0]):
        input_data = X[i]
        prediction = redeNeuronal.predict(input_data) # utilizar a função predict da redeNeuronal para obter as previsoes do operador pretendido
        predicted_value = prediction[0][0] # passar para a formatação de forma a mostrar o resuldado
        print(f"Entrada: {input_data}, Saída Prevista: {predicted_value:.2f}")

    # mostrar gráficamente a evolução do erro
    plt.plot(range(epochs), error_history)
    plt.xlabel('Época')
    plt.ylabel('Erro Médio Absoluto')
    plt.title(f'Evolução do Erro para o Operador {operator}')
    plt.show()

# efetua todo o processo da função train_predict_plot para cada operador
train_predict_plot("OR")
train_predict_plot("AND")
train_predict_plot("NOT")
train_predict_plot("XOR")
