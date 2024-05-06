try:
    import numpy as np
except ImportError:
    print("La biblioteca NumPy no está instalada. Por favor, instala NumPy para ejecutar este programa.")
    exit()

# Definir el entorno de la cuadrícula
grid_world = np.array([
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, 0, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 10]
])

# Definir las acciones posibles (arriba, abajo, izquierda, derecha)
actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Inicializar la tabla Q con valores aleatorios
Q_table = np.random.rand(5, 5, 4)

# Parámetros del algoritmo Q-Learning
gamma = 0.8  # Factor de descuento
alpha = 0.2  # Tasa de aprendizaje
epsilon = 0.1  # Factor de exploración

# Función para seleccionar una acción basada en epsilon-greedy
def choose_action(state):
    if np.random.rand() < epsilon:
        return np.random.choice(actions)
    else:
        return actions[np.argmax(Q_table[state])]

# Función principal de Q-Learning
def q_learning():
    # Número de episodios de entrenamiento
    episodes = 1000

    for _ in range(episodes):
        # Reiniciar el estado del agente a la posición inicial (0, 0)
        state = (0, 0)
        
        while True:
            action = choose_action(state)
            
            if action == 'UP':
                next_state = (state[0] - 1, state[1])
            elif action == 'DOWN':
                next_state = (state[0] + 1, state[1])
            elif action == 'LEFT':
                next_state = (state[0], state[1] - 1)
            elif action == 'RIGHT':
                next_state = (state[0], state[1] + 1)
            
            if 0 <= next_state[0] < 5 and 0 <= next_state[1] < 5:
                reward = grid_world[next_state]
                Q_table[state][actions.index(action)] += alpha * (reward + gamma * np.max(Q_table[next_state]) - Q_table[state][actions.index(action)])
                state = next_state
                
                if reward == 10:
                    break

# Entrenar el agente
q_learning()

# Mostrar la tabla Q aprendida
print("Tabla Q aprendida:")
print(Q_table)
