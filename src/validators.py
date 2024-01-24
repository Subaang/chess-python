import board
import king
import misc
import pieces
import pawn


def input_validator(move):
    if len(move) != 5:
        return False

    if move[2] != '-':
        return False

    if move[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return False

    if move[3] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return False

    if move[1] not in ['8', '7', '6', '5', '4', '3', '2', '1']:
        return False

    if move[4] not in ['8', '7', '6', '5', '4', '3', '2', '1']:
        return False

    return True


def origin_validator(move):
    cart_origin = misc.chess_to_cart(move[0], move[1])

    if board.board[cart_origin[0]][cart_origin[1]] == "__":
        return False

    return True


def move_validator(move, turn):
    cart_origin = misc.chess_to_cart(move[0], move[1])
    cart_destination = misc.chess_to_cart(move[3], move[4])

    if cart_destination not in pieces.generate_valid_moves(board.board[cart_origin[0]][cart_origin[1]], turn):
        return False


def turn_validator(move, turn):
    cart_origin = misc.chess_to_cart(move[0], move[1])
    piece_color = board.board[cart_origin[0]][cart_origin[1]].name[0]

    if turn == 0 and piece_color == "b":
        return False

    if turn == 1 and piece_color == "w":
        return False

    return True


def king_validator(move, turn, alive_pieces, white_king, black_king):
    cart_origin = misc.chess_to_cart(move[0], move[1])
    cart_destination = misc.chess_to_cart(move[3], move[4])
    enemy_piece_list = []
    checked_squares = []

    if turn == 0:
        king_piece = white_king
    else:
        king_piece = black_king

    king_color = king_piece.color

    # Temporarily removing the king so that he can't block his own checked squares
    board.board[king_piece.row][king_piece.col] = "__"

    if turn == 0:
        for i in alive_pieces:
            if i.name[0] == "b":
                enemy_piece_list.append(i)
    else:
        for i in alive_pieces:
            if i.name[0] == "w":
                enemy_piece_list.append(i)

    for i in enemy_piece_list:
        if i.name[1] != "p":
            checked_squares += pieces.generate_valid_moves(i, misc.change_turn(turn))
        else:
            # King is the enemy of the pawn. so enemy_color == king_color
            valid_moves = []
            pawn.generate_pawn_attack_squares(i, valid_moves, king_color)
            checked_squares += valid_moves

    board.board[king_piece.row][king_piece.col] = king_piece

    if (king_piece.row, king_piece.col) in checked_squares:
        return False

    return True


def mate(white_king, black_king, alive_pieces):
    for king_piece in [white_king, black_king]:
        in_check = False
        king_pos = king_piece.row, king_piece.col
        enemy_piece_list = []
        checked_squares = []
        turn = 0

        king_color = king_piece.name[0]
        enemy_color = ""
        if king_color == "w":
            turn = 0
            enemy_color = "b"
        else:
            turn = 1
            enemy_color = "b"

        # Temporarily removing the king so that he can't block his own checked squares
        board.board[king_pos[0]][king_pos[1]] = "__"

        if king_color == "w":
            for i in alive_pieces:
                if i.name[0] == "b":
                    enemy_piece_list.append(i)
        else:
            for i in alive_pieces:
                if i.name[0] == "w":
                    enemy_piece_list.append(i)

        for i in enemy_piece_list:
            if i.name[1] != "p":
                checked_squares += pieces.generate_valid_moves(i, misc.change_turn(turn))
            else:
                # King is the enemy of the pawn. so enemy_color == king_color
                valid_moves = []
                pawn.generate_pawn_attack_squares(i, valid_moves, king_color)
                checked_squares += valid_moves

        board.board[king_pos[0]][king_pos[1]] = king_piece

        if king_pos in checked_squares:
            in_check = True

        valid_king_moves = []
        king.generate_king_moves(board.board[king_pos[0]][king_pos[1]], valid_king_moves, enemy_color)

        to_remove = []
        for i in valid_king_moves:
            if i[0] not in range(0, 8):
                to_remove.append(i)

            if i[1] not in range(0, 8):
                to_remove.append(i)

            if i in checked_squares:
                to_remove.append(i)

        valid_king_moves = list(set(valid_king_moves) - set(to_remove))

        if len(valid_king_moves) == 0 and in_check:
            if turn == 0:
                print("Checkmate! Black wins")
            else:
                print("Checkmate! White wins")

        if len(valid_king_moves) == 0 and not in_check:
            print("Stalemate!")


def validate(move, turn, alive_pieces, white_king, black_king):
    if input_validator(move) is False:
        print("1")
        return False

    if origin_validator(move) is False:
        print("2")
        return False

    if turn_validator(move, turn) is False:
        print("3")
        return False

    if move_validator(move, turn) is False:
        print("4")
        return False

    if king_validator(move, turn, alive_pieces, white_king, black_king) is False:
        print("5")
        return False

    return True
