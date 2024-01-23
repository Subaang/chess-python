import board
import misc
import pieces
import validators
import moves

move = ''
turn = 0  # 0 = white, 1 = black

white_king,black_king = pieces.initialize_board()
alive_pieces = pieces.Piece.list_objects()

while True:
    validators.mate(white_king, black_king, alive_pieces)
    board.displayboard()

    move = input(">")

    # checks if input is in correct format
    if validators.validate(move, turn, alive_pieces) is False:
        print("invalid")
        continue

    moves.play_move(move, alive_pieces)

    turn = misc.change_turn(turn)
