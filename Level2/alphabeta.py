import copy

cache = {}
hit = 0
miss = 0


def score(game, minmax, depth):
    '''
    :param depth:
    :param alpha:
    :param beta:
    :param game: current state of the game
    :param minmax: str can have following values 'min' or 'max'
    :return:
    '''
    global cache
    global hit, miss

    if game in cache:
        hit += 1
        return cache[game]
    else:
        miss += 1

    if game.winner() == "O":
        return -10
    if game.winner() == "X":
        return 10
    if game.winner() == "Tie":
        return 0
    if depth <= 0:
        return 0

    scores = []
    for i in range(1, 4):
        for j in range(1, 4):
            game_copy = copy.deepcopy(game)
            if game_copy.possible_move((i, j)):

                if minmax == 'max':
                    game_copy.make_turn((i, j), "X")
                    s = score(game_copy, "min", depth - 1)
                    scores.append(s)

                else:
                    game_copy.make_turn((i, j), "O")
                    s = score(game_copy, "max", depth - 1)
                    scores.append(s)

    if minmax == 'max':
        answer = max(scores)
    else:
        answer = min(scores)

    cache[game] = answer
    return answer


def next_turn(game):
    scores = {}

    for i in range(1, 4):
        for j in range(1, 4):
            game_copy = copy.deepcopy(game)
            if game_copy.possible_move((i, j)):
                game_copy.make_turn((i, j), "X")
                scores[(i, j)] = score(game_copy, "min", 4)

    return max(scores, key=scores.get)
