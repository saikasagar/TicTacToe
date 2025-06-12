

from game import TicTacToe, HumanPlayer

def play(game, x_player, o_player):
    game.print_board_nums()
    letter = "X"

    while game.empty_squares():
        if letter == "X":
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            print(f"\n{letter} makes a move to square {square}")
            game.print_board()
            print()

            if game.current_winner:
                print(f"{letter} wins!")
                return

            letter = "O" if letter == "X" else "X"

    print("It's a tie!")


if __name__ == "__main__":
    game = TicTacToe()
    x_player = HumanPlayer("X")
    o_player = HumanPlayer("O")
    play(game, x_player, o_player)
