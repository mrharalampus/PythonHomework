import csv


def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")


def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def save_scores(player_x, player_o, score_x, score_o):
    with open("scores.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Score"])
        writer.writerow([player_x, score_x])
        writer.writerow([player_o, score_o])


def play_game():
    player_x = input("Enter name for player X: ")
    player_o = input("Enter name for player O: ")

    score_x = 0
    score_o = 0

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        while True:
            print_board(board)

            if current_player == "X":
                player_name = player_x
            else:
                player_name = player_o

            try:
                move = input(f"{player_name} ({current_player}), enter row and column (1-3 1-3): ")
                row, col = map(int, move.split())
                row -= 1
                col -= 1

                if board[row][col] != " ":
                    print("Cell already taken. Try again.")
                    continue

                board[row][col] = current_player

            except (ValueError, IndexError):
                print("Invalid input. Try again.")
                continue

            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == "X":
                    print(f"{player_x} wins!")
                    score_x += 1
                else:
                    print(f"{player_o} wins!")
                    score_o += 1
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        print(f"Score -> {player_x}: {score_x}, {player_o}: {score_o}")

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            save_scores(player_x, player_o, score_x, score_o)
            print("Scores saved to scores.csv. Goodbye!")
            break


if __name__ == "__main__":
    play_game()
