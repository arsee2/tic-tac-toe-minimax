import copy


def score(game, minmax):
    '''
    :param game: current state of the game
    :param minmax: str can have following values 'min' or 'max'
    :return:
    '''

    # print("------------------")
    # print(game)
    # print("------------------")
    if game.winner() == "O":
        return -10
    if game.winner() == "X":
        return 10
    if game.winner() == "Tie":
        return -1

    scores = []
    for i in range(1, 4):
        for j in range(1, 4):
            game_copy = copy.deepcopy(game)
            if game_copy.possible_move((i, j)):

                if minmax == 'max':
                    game_copy.make_turn((i, j), "X")
                    scores.append(score(game_copy, "min"))
                else:
                    game_copy.make_turn((i, j), "O")
                    scores.append(score(game_copy, "max"))

    if minmax == 'max':
        return max(scores)
    else:
        return min(scores)


def next_turn(game):
    scores = {}
    for i in range(1, 4):
        for j in range(1, 4):
            game_copy = copy.deepcopy(game)
            if game_copy.possible_move((i, j)):
                game_copy.make_turn((i, j), "X")
                scores[(i, j)] = score(game_copy, "min")


    return max(scores, key=scores.get)
