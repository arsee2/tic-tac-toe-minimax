from game import *
import minimax

game = TicTacToe()
print(game)
while game.winner() == "No":
    print("Enter two numbers x y")
    inp = input()
    y, x = inp.split(" ")
    y = int(y)
    x = int(x)
    if game.possible_move((x, y)):
        game.make_turn((x, y), "O")
    else:
        print("Incorrect input, try again")
        continue

    if game.winner()!="No":
        break
    print(game)
    print("wait")
    t =  minimax.next_turn(game)
    print("Minimax turn:", t)
    game.make_turn(t,"X")
    print(game)


print("Winner: ", game.winner())
