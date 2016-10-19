

def clear_screen():
    print("\033c", end="")



test_board2 = list(itertools.repeat(list(itertools.repeat(EMPTY,BOARD_SIZE)),BOARD_SIZE))

print_board(test_board)