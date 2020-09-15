import numpy as np


class TicTacToe:
    def __init__(self):
        self.board = [[[" " for _ in range(3)] for _ in range(3)] for _ in range(3)]

    def __hash__(self):
        return hash((str(self.board)))

    def __eq__(self, other):
        return np.array_equal(np.array(self.board),np.array(other.board))

    def possible_move(self, position):
        '''
        :param position: is a tuple of ints (x,y)
        :return: whether it is possible to place figure on position (x,y)
        '''
        x, y = position
        if 1 <= x <= 3 and 1 <= y <= 3 and self.board[x - 1][y - 1][2] == ' ':
            return True
        else:
            return False

    def make_turn(self, position, player):
        '''
        :param position: is tuple of ints (x,y) 1<=x<=3 1<=y<=3
        :param player: str "O" or  "X"
        '''
        x, y = position
        z = [i for i, v in enumerate(self.board[x - 1][y - 1]) if v == ' '][0]
        if player != "O" and player != "X":
            raise ("Incorrect player:" + player)

        self.board[x - 1][y - 1][z] = player

    def __is_winner_2D(self, matrix, player):
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
            if all(matrix[r][c] == player for r, c in ind):
                return True

    def __is_winner_diags_3D(self, player):
        win_indexes = []
        # add diags
        win_indexes.append([(j, j, j) for j in range(3)])
        win_indexes.append([(j, 2 - j, j) for j in range(3)])
        win_indexes.append([(j - 2, j, j) for j in range(3)])
        win_indexes.append([(j - 2, 2 - j, j) for j in range(3)])
        for ind in win_indexes:
            if all(self.board[r][c][d] == player for r, c, d in ind):
                return True

    def __get_all_matrices(self):
        tensor = np.array(self.board)
        matrices = []
        for i in range(3):
            matrices.append(tensor[i, :, :])
            matrices.append(tensor[:, i, :])
            matrices.append(tensor[:, :, i])
        return matrices

    def is_winner_3d(self, player):
        matrices = self.__get_all_matrices()
        if any([self.__is_winner_2D(matrix, player) for matrix in matrices]):
            return True

        if self.__is_winner_diags_3D(player):
            return True

        return False

    def winner(self):
        '''
        :return: winner of the game. One of the following 4 values can be returned "O", "X", "No" "Tie"
        '''
        if self.is_winner_3d("O"):
            return "O"

        if self.is_winner_3d("X"):
            return "X"

        if sum(sum(sum(z != " " for z in y) for y in x) for x in self.board) >= 3 * 3 * 3:
            return "Tie"

        return "No"

    def __str__(self):
        answer = ""
        for z in range(2,-1,-1):
            answer += "\n\n"
            answer += "\n______\n".join(["|".join([self.board[i][j][z] for j in range(3)]) for i in range(3)])
            answer += "\n\n"
        return answer
