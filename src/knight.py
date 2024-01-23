import board


def generate_knight_moves(p, valid_moves, enemy_color):

    try:
        if board.board[p.row + 2][p.col + 1] == "__" or board.board[p.row + 2][p.col + 1].name[0] == enemy_color:
            valid_moves.append((p.row + 2,p.col + 1))
    except IndexError:
        pass

    try:
        if board.board[p.row + 1][p.col + 2] == "__" or board.board[p.row + 1][p.col + 2].name[0] == enemy_color:
            valid_moves.append((p.row + 1,p.col + 2))
    except IndexError:
        pass

    try:
        if board.board[p.row + 2][p.col - 1] == "__" or board.board[p.row + 2][p.col - 1].name[0] == enemy_color:
            valid_moves.append((p.row + 2,p.col - 1))
    except IndexError:
        pass

    try:
        if board.board[p.row - 2][p.col - 1] == "__" or board.board[p.row - 2][p.col - 1].name[0] == enemy_color:
            valid_moves.append((p.row - 2,p.col - 1))
    except IndexError:
        pass

    try:
        if board.board[p.row - 2][p.col + 1] == "__" or board.board[p.row - 2][p.col + 1].name[0] == enemy_color:
            valid_moves.append((p.row - 2,p.col + 1))
    except IndexError:
        pass

    try:
        if board.board[p.row - 1][p.col - 2] == "__" or board.board[p.row - 1][p.col - 2].name[0] == enemy_color:
            valid_moves.append((p.row - 1,p.col - 2))
    except IndexError:
        pass

