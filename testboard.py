board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

board2 = list(map(list, zip(*board)))
print(board2)