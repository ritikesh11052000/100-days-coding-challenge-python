import random

def get_player_names():
    player1_name = input("Enter player 1's name: ")
    player2_name = input("Enter player 2's name: ")
    return player1_name, player2_name

def get_player_symbol():
    while True:
        player_symbol = input("Do you want to be X or O: ").upper()
        if player_symbol in ['X', 'O']:
            return player_symbol
        else:
            print("Invalid input. Please choose X or O.")

def print_board(board):
    print("   0 1 2")
    for i, row in enumerate(board):
        print(f"{i}  {' '.join(cell if cell else ' ' for cell in row)}")

def make_move_for_robot(board, opponent_symbol):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == "":
            board[row][col] = opponent_symbol
            break

def get_move(board, player_symbol, player_name):
    while True:
        try:
            row = int(input(f"{player_name}, enter row number (0-2): "))
            col = int(input(f"{player_name}, enter column number (0-2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                board[row][col] = player_symbol
                break
            else:
                print("Invalid input. Please enter a valid row and column number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    player1_name, player2_name = get_player_names()
    player1_symbol = get_player_symbol()
    player2_symbol = "O" if player1_symbol == "X" else "X"
    board = [['' for _ in range(3)] for _ in range(3)]

    opponent_choice = input("Do you want to play against a robot (r) or a person (p): ").lower()
    print_board(board)

    current_turn = player1_symbol  # Start with player 1's turn

    while True:
        if opponent_choice == "p":
            if current_turn == player1_symbol:
                get_move(board, player1_symbol, player1_name)
            else:
                get_move(board, player2_symbol, player2_name)
        else:
            if current_turn == player1_symbol:
                get_move(board, player1_symbol, player1_name)
            else:
                print("Robot's turn:")
                make_move_for_robot(board, player2_symbol)

        print_board(board)
        winner = check_win(board)
        if winner:
            if winner == player1_symbol:
                print(f"{player1_name} wins!")
            else:
                print(f"{player2_name} wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

        current_turn = player2_symbol if current_turn == player1_symbol else player1_symbol  # Switch turns

def check_win(board):
    for player in ['X', 'O']:
        for row in board:
            if all(cell == player for cell in row):
                return player
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return player
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return player
    return None

def check_tie(board):
    return all(all(cell != "" for cell in row) for row in board)

if __name__ == "__main__":
    main()

