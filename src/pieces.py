import king
import pawn
import rook
import bishop
import knight
import board


def initialize_board():
    for i in range(8):
        board.board[1][i] = Pawn("b", 1, i)

    for i in range(8):
        board.board[6][i] = Pawn("w", 6, i)

    board.board[0][0] = Rook("b", 0, 0)
    board.board[0][7] = Rook("b", 0, 7)
    board.board[7][0] = Rook("w", 7, 0)
    board.board[7][7] = Rook("w", 7, 7)

    board.board[0][1] = Knight("b", 0, 1)
    board.board[0][6] = Knight("b", 0, 6)
    board.board[7][1] = Knight("w", 7, 1)
    board.board[7][6] = Knight("w", 7, 6)

    board.board[0][2] = Bishop("b", 0, 2)
    board.board[0][5] = Bishop("b", 0, 5)
    board.board[7][2] = Bishop("w", 7, 2)
    board.board[7][5] = Bishop("w", 7, 5)

    board.board[0][3] = Queen("b", 0, 3)
    board.board[7][3] = Queen("b", 7, 3)

    board.board[7][4] = King("w", 7, 4)
    board.board[0][4] = King("b", 0, 4)

    return board.board[7][4], board.board[0][4]


#  This also generates negative indices, but dont cause a problem because the user can't input negative indices
def generate_valid_moves(p, turn):
    valid_moves = []
    enemy_color = "b"
    if turn == 1:
        enemy_color = "w"

    if p.name[-1] == "p":  # En-passant not yet added
        pawn.generate_pawn_moves(p, valid_moves, enemy_color)

    if p.name[-1] == "R":
        rook.generate_rook_moves(p, valid_moves, enemy_color)

    if p.name[-1] == "N":
        knight.generate_knight_moves(p, valid_moves, enemy_color)

    if p.name[-1] == "B":
        bishop.generate_bishop_moves(p, valid_moves, enemy_color)

    if p.name[-1] == "Q":
        rook.generate_rook_moves(p, valid_moves, enemy_color)
        bishop.generate_bishop_moves(p, valid_moves, enemy_color)

    if p.name[-1] == "K":
        king.generate_king_moves(p, valid_moves, enemy_color)

    return valid_moves


class Piece:
    alive_pieces = []

    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        Piece.alive_pieces.append(self)

    @classmethod
    def list_objects(Piece):
        return Piece.alive_pieces


class Pawn(Piece):

    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.name = self.color + "p"
        self.first_move = True
        Pawn.list_objects()


class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.name = self.color + "R"


class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.name = self.color + "B"


class Knight(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.name = self.color + "N"


class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.name = self.color + "Q"


class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.name = self.color + "K"
