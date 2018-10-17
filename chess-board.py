# Chessboard

rows = 8
cols = 8

board = [['EE' for c in range(cols)] for r in range(rows) ]
pieces = ['R','K','B','Q','K','B','K','R']

p = 0

for c in range(cols):
    board[0][c] = 'B'+pieces[p]
    p += 1

for c in range(cols):
    board[1][c] = 'BP'

p = 0

for c in range(cols):
    board[7][c] = 'W'+pieces[p]
    p += 1

for c in range(cols):
    board[6][c] = 'WP'

# Print out the board
for r in range(rows):
    for c in range(cols):
        print(board[r][c],' ', end='')
    print()
