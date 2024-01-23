import board
import misc


def play_move(move, alive_pieces):
    cart_origin = misc.chess_to_cart(move[0], move[1])
    cart_destination = misc.chess_to_cart(move[3], move[4])
    piece = board.board[cart_origin[0]][cart_origin[1]]

    if piece.name[-1] == "p":
        piece.first_move = False

    # updates current position of piece
    piece.row = cart_destination[0]
    piece.col = cart_destination[1]

    if board.board[cart_destination[0]][cart_destination[1]] != "__":
        alive_pieces.remove(board.board[cart_destination[0]][cart_destination[1]])

    board.board[cart_destination[0]][cart_destination[1]] = piece
    board.board[cart_origin[0]][cart_origin[1]] = "__"
