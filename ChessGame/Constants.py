#Bit Representations of each type of piece at the start of a game of chess
#64 Bits, represented in hex
WK_BOARD = 0x0800000000000000
WQ_BOARD = 0x1000000000000000
WR_BOARD = 0x8100000000000000
WB_BOARD = 0x2400000000000000
WKN_BOARD = 0x4200000000000000
WP_BOARD = 0x00FF000000000000
BK_BOARD = 0x0000000000000008
BQ_BOARD = 0x0000000000000010
BR_BOARD = 0x0000000000000081
BB_BOARD = 0x0000000000000024
BKN_BOARD = 0x0000000000000042
BP_BOARD = 0x000000000000FF00

#Values of each type of piece
KING_VALUE = 1000000000000000000000000000000000000000000000000000000000
QUEEN_VALUE = 9
ROOK_VALUE = 5
BISHOP_VALUE = 3
KNIGHT_VALUE = 3
PAWN_VALUE = 1

#Avoiding Magic Numbers
B_START = 0
B_END = 64




