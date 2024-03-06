import numpy as np

# função de ativação
def step_function(x):
    return np.where(x > 0, 1, 0)

# função da rede neural XOR
def xor_perceptron(input_data):
    # Pesos e pendores
    w_hidden = np.array([[1, -1], [-1, 1]])   # pesos da camada oculta
    b_hidden = np.array([-0.5, -0.5])         # pendor da camada oculta
    w_output = np.array([1, 1])               # pesos da camada de saída
    b_output = -0.5                           # pendor da camada de saída
    
    # camada oculta
    hidden_layer_input = np.dot(input_data, w_hidden) + b_hidden
    hidden_layer_output = step_function(hidden_layer_input)
    
    # camada de saída
    output_layer_input = np.dot(hidden_layer_output, w_output) + b_output
    final_output = step_function(output_layer_input)
    
    return final_output

# teste
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

for input_data in inputs:
    result = xor_perceptron(input_data)
    print(f"Input: {input_data}, Output: {result}")
