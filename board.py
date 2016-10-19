import itertools

class Board:
    BOARD_SIZE = 10
    EMPTY = 'O'
    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    MISS = '.'
    HIT = '*'
    SUNK = '#'
    def __init__(self):
        board = list(itertools.repeat(list(itertools.repeat(EMPTY,BOARD_SIZE)),BOARD_SIZE))
        self.board = board

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


    def print_board(self, board):
        print_board_heading()

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1