class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def possible_move(self, position):
        '''
        :param position: is a tuple of ints (x,y)
        :return: whether it is possible to place figure on position (x,y)
        '''
        x, y = position
        if 1 <= x <= 3 and 1 <= y <= 3 and self.board[x - 1][y - 1] == ' ':
            return True
        else:
            return False

    def make_turn(self, position, player):
        '''
        :param position: is tuple of ints (x,y) 1<=x<=3 1<=y<=3
        :param player: str "O" or  "X"
        '''
        x, y = position
        if player != "O" and player != "X":
            raise ("Incorrect player:" + player)
        self.board[x - 1][y - 1] = player

    def __isWinner(self, player):
        win_indexes = []
        # add rows
        for i in range(3):
            win_indexes.append([(i, j) for j in range(3)])
        # add columns
        for i in range(3):
            win_indexes.append([(j, i) for j in range(3)])

        # add diagonal
        win_indexes.append([(j, j) for j in range(3)])

        # add another diagonal
        win_indexes.append([(j, 2 - j) for j in range(3)])

        for ind in win_indexes:
            if all(self.board[r][c] == player for r, c in ind):
                return True

    def winner(self):
        '''
        :return: winner of the game. One of the following 4 values can be returned "O", "X", "No" "Tie"
        '''
        if self.__isWinner("O"):
            return "O"

        if self.__isWinner("X"):
            return "X"

        if sum(sum(y != " " for y in x) for x in self.board) >= 3 * 3:
            return "Tie"

        return "No"

    def __str__(self):
        return "\n______\n".join(["|".join([self.board[i][j] for j in range(3)]) for i in range(3)])
