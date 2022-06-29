MARKERS = {0: 'O', 1: 'X'}     # Маркеры


class Player:
    def __init__(self, name: str, marker: int):
        assert marker in MARKERS.keys(), 'Invalid marker id'
        self.marker = marker
        self.name = name


class Board:
    def __init__(self):
        self.__board = [[None for i in range(3)] for i in range(3)]
        self.__players = []
        self.__step = 0             # четные для первого игрока, нечетные для второго
        self.__state = False, None  # Завершена ли игра, Победитель

    def get_board(self):
        """ Возвращает доску """
        return self.__board

    def update_board(self, marker: int, position: tuple):
        """ Устанавливает маркер в указаную позицию """
        if self.__board[position[0]][position[1]] is None:
            self.__board[position[0]][position[1]] = marker
            return True
        else:
            return False

    @property
    def state(self):
        return self.__state

    def check_combinations(self, lst: list):
        """ Проверка выигрышной комбинации """
        for row in lst:
            if row[0] is None:
                continue
            if len(set(row)) == 1:
                self.__state = True, self.fetch_player_by_marker(row[0])

    def check_board(self):
        """ Проверяет доску на предмет чьей-то победы """
        # 1) Поиск выиграшных комбинаций
        rows = [row for row in self.__board]
        columns = [[row[i] for row in self.__board] for i in range(3)]
        diagonals = [[self.__board[i][i] for i in range(3)],                       # Главная диагональ
                     [self.__board[i][3 - i - 1] for i in range(3)]]      # Побочная диагональ
        self.check_combinations(rows)
        self.check_combinations(columns)
        self.check_combinations(diagonals)

        # 2) Есть ли свободные ячейки
        isEmpty = False
        for row in self.__board:
            if None in row:
                isEmpty = True
                break
        if isEmpty is False:
            # Игра завершена, но победителя нет
            self.__state = True, None

        return self.__state

    @property
    def players(self):
        """ Возвращает список игроков """
        return self.__players

    def add_player(self, player: Player):
        """ Добавляет игрока в базу """
        assert len(self.__players) < 2, 'Only 2 players allowed'
        self.__players.append(player)

    def fetch_player_by_marker(self, marker: int):
        """ Возвращает игрока по указанному id маркера """
        assert marker in MARKERS.keys(), f'Unknown marker id {marker!r}'
        players = {player.marker: player for player in self.__players}
        return players[marker]

    @property
    def step(self):
        return self.__step

    def next_step(self):
        self.__step += 1

    @staticmethod
    def get_allowed_moves():
        """ Возвращает координаты человеческим языком """
        table = {
            't1': (0, 0), 't2': (0, 1), 't3': (0, 2),
            'c1': (1, 0), 'c2': (1, 1), 'c3': (1, 2),
            'b1': (2, 0), 'b2': (2, 1), 'b3': (2, 2)
        }
        return table


class Controller:
    def __init__(self, board, view):
        self.board = board
        self.view = view

    def read(self):
        """ Читает команды от пользователя """
        if self.board.state[0]:
            return False
        command = input("> ").replace(' ', '').lower()
        allowed_moves = self.board.get_allowed_moves()
        if command in allowed_moves.keys():
            position = allowed_moves[command]
            player = self.board.players[self.board.step % 2]
            self.move(player, position)
        else:
            self.view.notify("Unknown command")
        return True

    def move(self, player: Player, position: tuple):
        """ Устанавливает значок игрока в указанное место """
        isMoved = self.board.update_board(player.marker, position)
        if isMoved is False:
            return self.view.notify('This position is already taken, try another')
        self.board.next_step()
        self.view.notify(f"{player.name} makes a move:")
        self.view.draw(self.board.get_board())
        # Проверяем состояние игры (то есть доски)
        self.check_game_results()

    def check_game_results(self):
        """ Возвращает состояние доски """
        # Проверяем доску только после пятого хода, поскольку до этого выиграшных комбинаций не может быть
        if self.board.step > 3:
            state = self.board.check_board()
            if state[0]:
                self.view.results(state)

    def play(self):
        """ Запуск игры """
        name_playerA = input('Please input name first player>')
        playerA = Player(name_playerA, 1)
        name_playerB = input('Please input name second player>')
        playerB = Player(name_playerB, 0)
        self.board.add_player(playerA)
        self.board.add_player(playerB)
        self.view.instructions()
        self.run = True
        self.view.draw(self.board.get_board())
        self.view.send(f"{playerA.name} please make a move!")
        while self.run:
            self.run = self.read()
        input()     # Чтобы окно не закрывалось моментально после итогов игры


class View:
    @staticmethod
    def draw(board):
        for i in range(3):
            print("\t", end='')
            for j in range(3):
                marker = '.' if board[i][j] is None else MARKERS[board[i][j]]
                print(f"  {marker}  ", end='')
                if j < 3-1:
                    print("|", end='')
            if i < 3-1:
                print(f"\n\t—————{'+—————'*(3 - 1)}")
            else:
                print("")

    @staticmethod
    def notify(message):
        """ Отправка уведомлений """
        print(f"[!] {message}")

    @staticmethod
    def send(message):
        """ Отправка просто сообщений """
        print(f"[*] {message}")

    @staticmethod
    def instructions():
        print('='*30)
        print("You can make a move by entering the corresponding cell number:")
        print(f"\t  T1 |  T2 |  T3 \n",
              f"\t—————+—————+—————\n",
              f"\t  C1 |  C2 |  C3 \n",
              f"\t—————+—————+—————\n",
              f"\t  B1 |  B2 |  B3 \n")
        print('='*30)

    def results(self, state):
        if state[1]:
            self.notify(f"Game over: {state[1].name} won this game!")
        else:
            self.notify(f"Game over: Draw!")


if __name__ == "__main__":
    game = Controller(Board(), View())
    game.play()
