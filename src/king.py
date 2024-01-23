import board


def generate_king_moves(p, valid_moves, enemy_color):
    # We have to handle index error because out of board can be generated even when move is played on board
    # The same isn't true for pawns

    try:
        if board.board[p.row + 1][p.col] == "__":
            valid_moves.append((p.row + 1, p.col))
    except IndexError:
        pass

    try:
        if board.board[p.row - 1][p.col] == "__":
            valid_moves.append((p.row - 1, p.col))
    except IndexError:
        pass

    try:
        if board.board[p.row][p.col + 1] == "__":
            valid_moves.append((p.row, p.col + 1))
    except IndexError:
        pass

    try:
        if board.board[p.row][p.col - 1] == "__":
            valid_moves.append((p.row, p.col - 1))
    except IndexError:
        pass

    try:
        if board.board[p.row + 1][p.col + 1] == "__":
            valid_moves.append((p.row + 1, p.col + 1))
    except IndexError:
        pass

    try:
        if board.board[p.row + 1][p.col - 1] == "__":
            valid_moves.append((p.row + 1, p.col - 1))
    except IndexError:
        pass

    try:
        if board.board[p.row - 1][p.col + 1] == "__":
            valid_moves.append((p.row - 1, p.col + 1))
    except IndexError:
        pass

    try:
        if board.board[p.row - 1][p.col - 1] == "__":
            valid_moves.append((p.row - 1, p.col - 1))
    except IndexError:
        pass

    # Below: Capturing enemies. We will remove protected squares for both above and below later

    try:
        if board.board[p.row + 1][p.col].name[0] == enemy_color:
            valid_moves.append((p.row + 1, p.col))
    except (IndexError, AttributeError) as e:
        pass

    try:
        if board.board[p.row - 1][p.col].name[0] == enemy_color:
            valid_moves.append((p.row - 1, p.col))
    except (IndexError, AttributeError) as e:
        pass

    try:
        if board.board[p.row][p.col + 1].name[0] == enemy_color:
            valid_moves.append((p.row, p.col + 1))
    except (IndexError, AttributeError) as e:
        pass

    try:
        if board.board[p.row][p.col - 1].name[0] == enemy_color:
            valid_moves.append((p.row, p.col - 1))
    except (IndexError, AttributeError) as e:
        pass

    try:
        if board.board[p.row + 1][p.col + 1].name[0] == enemy_color:
            valid_moves.append((p.row + 1, p.col + 1))
    except (IndexError, AttributeError) as e:
        pass

    try:
        if board.board[p.row + 1][p.col - 1].name[0] == enemy_color:
            valid_moves.append((p.row + 1, p.col - 1))
    except (IndexError, AttributeError) as e:
        pass

    try:
        if board.board[p.row - 1][p.col + 1].name[0] == enemy_color:
            valid_moves.append((p.row - 1, p.col + 1))
    except (IndexError, AttributeError) as e:
        pass

    try:
        if board.board[p.row - 1][p.col - 1].name[0] == enemy_color:
            valid_moves.append((p.row - 1, p.col - 1))
    except (IndexError, AttributeError) as e:
        pass
