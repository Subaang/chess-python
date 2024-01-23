import board


def generate_rook_moves(p, valid_moves, enemy_color):
    current_row = p.row
    current_col = p.col
    i = 0


    try:  # search upwards
        while True:
            i += 1
            if board.board[current_row + i][current_col] == "__":
                valid_moves.append((current_row + i, current_col))
            else:
                if board.board[current_row + i][current_col].name[0] == enemy_color:
                    valid_moves.append((current_row + i, current_col))
                break

    except (IndexError, TypeError, AttributeError) as e:
        pass

    i = 0

    try:  # search downwards
        while True:
            i += 1
            if board.board[current_row - i][current_col] == "__":
                valid_moves.append((current_row - i, current_col))
            else:
                if board.board[current_row - i][current_col].name[0] == enemy_color:
                    valid_moves.append((current_row - i, current_col))
                break

    except (IndexError, TypeError, AttributeError) as e:
        pass

    i = 0

    try:  # search rightwards
        while True:
            i += 1
            if board.board[current_row][current_col + i] == "__":
                valid_moves.append((current_row, current_col + i))
            else:
                if board.board[current_row][current_col + i].name[0] == enemy_color:
                    valid_moves.append((current_row, current_col + i))
                break

    except (IndexError, TypeError, AttributeError) as e:
        pass

    i = 0

    try:  # search leftwards
        while True:
            i += 1
            if board.board[current_row][current_col - i] == "__":
                valid_moves.append((current_row, current_col - i))
            else:
                if board.board[current_row][current_col - i].name[0] == enemy_color:
                    valid_moves.append((current_row, current_col - i))
                break

    except (IndexError, TypeError, AttributeError) as e:
        pass

