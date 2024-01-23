import board


def generate_pawn_moves(p, valid_moves, enemy_color):
    if enemy_color == "w":  # I.E current player is playing with Black
        if board.board[p.row + 1][p.col] == "__":
            valid_moves.append((p.row + 1, p.col))

        if p.first_move is True and board.board[p.row + 2][p.col] == "__":
            valid_moves.append((p.row + 2, p.col))

        try:
            if board.board[p.row + 1][p.col + 1].name[0] == enemy_color:
                valid_moves.append((p.row + 1, p.col + 1))

        except (IndexError, TypeError, AttributeError) as e:
            pass

        try:
            if board.board[p.row + 1][p.col - 1].name[0] == enemy_color:
                valid_moves.append((p.row + 1, p.col - 1))
        except (IndexError, TypeError, AttributeError) as e:
            pass

    else:
        if board.board[p.row - 1][p.col] == "__":
            valid_moves.append((p.row - 1, p.col))

        if p.first_move is True and board.board[p.row - 2][p.col] == "__":
            valid_moves.append((p.row - 2, p.col))

        try:
            if board.board[p.row - 1][p.col - 1].name[0] == enemy_color:
                valid_moves.append((p.row - 1, p.col - 1))
        except (IndexError, TypeError, AttributeError) as e:
            pass

        try:
            if board.board[p.row - 1][p.col + 1].name[0] == enemy_color:
                valid_moves.append((p.row - 1, p.col + 1))
        except (IndexError, TypeError, AttributeError) as e:
            pass


def generate_pawn_attack_squares(p, valid_moves, enemy_color):
    if enemy_color == "w":  # I.E current player is playing with Black
        valid_moves.append((p.row + 1, p.col + 1))
        valid_moves.append((p.row + 1, p.col - 1))

    else:
        valid_moves.append((p.row - 1, p.col - 1))
        valid_moves.append((p.row - 1, p.col + 1))
