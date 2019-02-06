from Piece import *
from Constants import *
import pdb


"""
-Creates list to store of all of the neccessary bitBoards
-Creates each list, initializes it, and stores it in boardList
-Creates array for the overall Board
"""
class BoardState(object):
    def __init__(self):
        self.boardArray = [0] * 64 
        self.setStartBoard()
    
    """
    - Sets the board to a starter board
    """
        
    def setStartBoard(self):
        self.boardArray[0] = BRook(0)
        self.boardArray[1] = BKnight(1)
        self.boardArray[2] = BBishop(2)
        self.boardArray[3] = BQueen(3)
        self.boardArray[4] = BKing(4)
        self.boardArray[5] = BBishop(5)
        self.boardArray[6] = BKnight(6)
        self.boardArray[7] = BRook(7)
        self.boardArray[63] = WRook(63)
        self.boardArray[62] = WKnight(62)
        self.boardArray[61] = WBishop(61)
        self.boardArray[60] = WKing(60, self.boardArray)
        print(self.boardArray)
        self.boardArray[59] = WQueen(59)
        self.boardArray[58] = WBishop(58)
        self.boardArray[57] = WKnight(57)
        self.boardArray[56] = WRook(56)
        
        for i in range(0, 8):
            self.boardArray[i + 8] = BPawn(i + 8)
            self.boardArray[i + 48] = WPawn(i + 48)
    '''
    - moves a piece from one spot on the board to another
    '''
    def move(self, src, dst):
        if(src >= 0 and src < 64 and dst >= 0 and dst < 64 and self.boardArray[src] != 0):
            self.boardArray[dst] = self.boardArray[src]
            self.boardArray[src] = 0
            self.boardArray[dst].location = dst
            self.boardArray[dst].moves = [0] * 64
        else:
            print("Invalid Inputs")
        




            
        
