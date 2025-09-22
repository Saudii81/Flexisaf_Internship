import random
import pickle

# Initialize Q-table
Q = {}

def get_state(board):
    return ''.join(board)

def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

def check_win(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def check_tie(board):
    return ' ' not in board

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
def train_q_agent(episodes=20000):
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

            if check_win(board, current_player):
                reward = 1 if current_player == 'O' else -1
                for s, a, ns in reversed(history):
                    update_q(s, a, reward, ns)
                    reward = -reward
                break
            elif check_tie(board):
                for s, a, ns in reversed(history):
                    update_q(s, a, 0, ns)
                break

            current_player = 'X' if current_player == 'O' else 'O'
            state = next_state

    # Save Q-table
    with open("q_table.pkl", "wb") as f:
        pickle.dump(Q, f)
    print("Training complete, Q-table saved.")

# Load Q-table
def load_q_table():
    global Q
    try:
        with open("q_table.pkl", "rb") as f:
            Q = pickle.load(f)
        print("Q-table loaded.")
    except FileNotFoundError:
        print("No Q-table found. Train first with train_q_agent().")

# Play against the trained AI
def play_game():
    load_q_table()
    board = [' '] * 9
    human = 'X'
    ai = 'O'

    def print_board():
        print(f"""
        {board[0]} | {board[1]} | {board[2]}
        ---------
        {board[3]} | {board[4]} | {board[5]}
        ---------
        {board[6]} | {board[7]} | {board[8]}
        """)

    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[move] = human
        if check_win(board, human):
            print_board()
            print("You win! 🎉")
            break
        if check_tie(board):
            print_board()
            print("It's a tie 🤝")
            break

        # AI move
        state = get_state(board)
        moves = available_moves(board)
        action = choose_action(state, moves, epsilon=0)  # always exploit after training
        board[action] = ai
        print(f"AI chooses {action+1}")
        print_board()

        if check_win(board, ai):
            print("AI wins! 💻")
            break
        if check_tie(board):
            print("It's a tie 🤝")
            break


# Example usage:
# train_q_agent(20000)  # Run once to train
# play_game()           # Then play against AI
