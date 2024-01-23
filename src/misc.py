import board


def chess_to_cart(alph, num):
    row = 8 - int(num)
    col = ord(alph) - ord('a')

    return row, col


def change_turn(n):
    if n == 0:
        return 1
    else:
        return 0
