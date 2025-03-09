import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True
def ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and AI is O.\n")
    print_board(board)

    while True:
        print("\nYour Turn (X):")
        while True:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = "X"
                break
            print("Invalid move. Try again.")
        print_board(board)
        if check_winner(board) == "X":
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        print("\nAI's Turn (O):")
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = "O"
        print_board(board)
        if check_winner(board) == "O":
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break
if __name__ == "__main__":
    main()
