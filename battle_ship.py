import random


class Ship:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.hits = set()


class Board:
    def __init__(self, ships):
        self.ships = ships
        self.board_size = 6
        self.board = [['О' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.shots = set()

    def display_board(self):
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
        for i, row in enumerate(self.board, start=1):
            print(f"{i} | {' | '.join(row)} |")

    def place_ships(self):
        for ship in self.ships:
            for coord in ship.coordinates:
                row, col = coord
                self.board[row][col] = '■'

    def check_shot(self, row, col):
        if (row, col) in self.shots:
            print("Вы уже стреляли в эту клетку. Попробуйте заново.")
            return False

        self.shots.add((row, col))
        for ship in self.ships:
            if (row, col) in ship.coordinates:
                ship.hits.add((row, col))
                self.board[row][col] = 'X'
                return True
        self.board[row][col] = 'T'
        return False


def generate_ships():
    ships = []
    for _ in range(4):  # 4 single-cell ships
        row = random.randint(0, 5)
        col = random.randint(0, 5)
        ships.append(Ship([(row, col)]))

    for _ in range(2):  # 2 two-cell ships
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(0, 5)
            col = random.randint(0, 4)
            coordinates = [(row, col), (row, col + 1)]
        else:
            row = random.randint(0, 4)
            col = random.randint(0, 5)
            coordinates = [(row, col), (row + 1, col)]
        ships.append(Ship(coordinates))

    for _ in range(1):  # 1 three-cell ship
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(0, 5)
            col = random.randint(0, 3)
            coordinates = [(row, col), (row, col + 1), (row, col + 2)]
        else:
            row = random.randint(0, 3)
            col = random.randint(0, 5)
            coordinates = [(row, col), (row + 1, col), (row + 2, col)]
        ships.append(Ship(coordinates))

    return ships


def main():
    player_ships = generate_ships()
    computer_ships = generate_ships()

    player_board = Board(player_ships)
    computer_board = Board(computer_ships)

    player_board.place_ships()
    computer_board.place_ships()

    player_score = 0
    computer_score = 0

    while player_score < 14 and computer_score < 14:
        print("\nДоска игрока:")
        player_board.display_board()
        print("\nДоска компьютера:")
        computer_board.display_board()

        try:
            player_row = int(input("Введите строку (1-6): ")) - 1
            player_col = int(input("Введите столбец (1-6): ")) - 1
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
            continue

        if not (0 <= player_row < 6 and 0 <= player_col < 6):
            print("Вы пытаетесь выстрелить в доску. Попробуйте заново.")
            continue

        if computer_board.check_shot(player_row, player_col):
            player_score += 1
            print("Попал!")
        else:
            print("Промазал!")

        computer_row = random.randint(0, 5)
        computer_col = random.randint(0, 5)

        if player_board.check_shot(computer_row, computer_col):
            computer_score += 1
            print("Компьютер попал в ваш корабль!")
        else:
            print("Компьютер промахнулся!")

    print("\nИгра окончена!")

    if player_score > computer_score:
        print("Поздравляю! Вы выиграли!")
    elif player_score < computer_score:
        print("Компьютер победил. Возможно вам повезет в другой раз!")
    else:
        print("Ничья! Вы и компьютер набрали одинаковое количество очков.")


if __name__ == "__main__":
    main()
