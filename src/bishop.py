import board


def generate_bishop_moves(p, valid_moves, enemy_color):
    current_row = p.row
    current_col = p.col
    i = 0

    try:  # search North East
        while True:
            i += 1
            if board.board[current_row + i][current_col + i] == "__":
                valid_moves.append((current_row + i, current_col + i))

            else:
                if board.board[current_row + i][current_col + i].name[0] == enemy_color:
                    valid_moves.append((current_row + i, current_col + i))
                break

    except (IndexError, TypeError, AttributeError) as e:
        pass

    i = 0

    try:  # search South West
        while True:
            i += 1
            if board.board[current_row - i][current_col - i] == "__":
                valid_moves.append((current_row - i, current_col - i))
            else:
                if board.board[current_row - i][current_col - i].name[0] == enemy_color:
                    valid_moves.append((current_row - i, current_col - i))
                break

    except (IndexError, TypeError, AttributeError) as e:
        pass

    i = 0

    try:  # search North West
        while True:
            i += 1
            if board.board[current_row + i][current_col - i] == "__":
                valid_moves.append((current_row, current_col + i))
            else:
                if board.board[current_row + i][current_col - i].name[0] == enemy_color:
                    valid_moves.append((current_row + i, current_col - i))
                break

    except (IndexError, TypeError, AttributeError) as e:
        pass

    i = 0

    try:  # search South East
        while True:
            i += 1
            if board.board[current_row - i][current_col + i] == "__":
                valid_moves.append((current_row - i, current_col + i))
            else:
                if board.board[current_row - i][current_col + i].name[0] == enemy_color:
                    valid_moves.append((current_row - i, current_col + i))
                break

    except (IndexError, TypeError, AttributeError) as e:
        pass
