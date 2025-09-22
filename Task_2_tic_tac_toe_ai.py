import random
import pickle

# Initialize Q-table
Q = {}

def get_state(board):
    return ''.join(board)

def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

def choose_action(state, moves, epsilon=0.1):
    if random.random() < epsilon or state not in Q:
        return random.choice(moves)
    return max(Q[state], key=Q[state].get)

def update_q(state, action, reward, next_state, alpha=0.5, gamma=0.9):
    if state not in Q:
        Q[state] = {a: 0 for a in range(9)}
    if next_state not in Q:
        Q[next_state] = {a: 0 for a in range(9)}
    Q[state][action] += alpha * (reward + gamma * max(Q[next_state].values()) - Q[state][action])

# Training loop
def train_q_agent(episodes=10000):
    for _ in range(episodes):
        board = [' '] * 9
        state = get_state(board)
        history = []

        current_player = 'O'
        while True:
            moves = available_moves(board)
            action = choose_action(state, moves)
            board[action] = current_player
            next_state = get_state(board)
            history.append((state, action, next_state))

            if check_win(current_player):
                reward = 1 if current_player == 'O' else -1
                for s, a, ns in reversed(history):
                    update_q(s, a, reward, ns)
                    reward = -reward  # alternate reward for opponent
                break
            elif check_tie():
                for s, a, ns in reversed(history):
                    update_q(s, a, 0, ns)
                break

            current_player = 'X' if current_player == 'O' else 'O'
            state = next_state

    # Save Q-table
    with open("q_table.pkl", "wb") as f:
        pickle.dump(Q, f)
