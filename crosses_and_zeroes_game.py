def greet():
    print("-------------------")
    print("  Добро пожаловать  ")
    print("      в игру       ")
    print("  крестики-нолики  ")
    print(" (‾́◡‾́) (‾́◡‾́)(‾́◡‾́)")
    print()
    print("   Удачной игры!   ")
    print()


greet()


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, symbol):
    # Проверка строк
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Проверка столбцов
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True

    # Проверка диагоналей
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_symbol = 'X'

    while True:
        print_board(board)
        row = int(input(f"Игрок {current_symbol}, введите номер строки (0, 1, 2): "))
        col = int(input(f"Игрок {current_symbol}, введите номер столбца (0, 1, 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_symbol

            if check_winner(board, current_symbol):
                print_board(board)
                print(f"Игрок {current_symbol} победил!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break

            current_symbol = 'O' if current_symbol == 'X' else 'X'
        else:
            print("Некорректный ход. Повторите попытку.")


if __name__ == "__main__":
    tic_tac_toe()
