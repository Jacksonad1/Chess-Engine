'''
Diagonal Up Left: position - 9
Diagonal Up Right: position - 7

Diagonal Down Left: position + 7
Diagonal Down Right: position + 9

Vertical Up: position - 8
Vertical Down: position + 8

Horizontal left: position - 1
Horizontal Right: position + 1


def diagonalMove(position):
    temp = position
    while temp
'''

def horizontalMoves(position):
    moves = [0] * 8
    temp = position - int(position % 8)
    lastInRow = temp + 7
    while(temp <= lastInRow):
        moves[temp % 8] = temp
        temp = temp + 1;
    return moves

def verticalMoves(position):
    moves = [0] * 8
    temp = int(position % 8)
    lastInColumn = temp + 56
    while(temp <= lastInColumn):
        moves[int(temp / 8)] = temp
        temp = temp + 8
    print(moves)

def diagonalMoves(position)



#verticalMoves(7)
#horizontalMoves(50)
