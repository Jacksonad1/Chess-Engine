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
        self.boardArray[0] = BRook()
        self.boardArray[1] = BKnight()
        self.boardArray[2] = BBishop()
        self.boardArray[3] = BQueen()
        self.boardArray[4] = BKing()
        self.boardArray[5] = BBishop()
        self.boardArray[6] = BKnight()
        self.boardArray[7] = BRook()
        self.boardArray[63] = WRook()
        self.boardArray[62] = WKnight()
        self.boardArray[61] = WBishop()
        self.boardArray[60] = WKing()
        self.boardArray[59] = WQueen()
        self.boardArray[58] = WBishop()
        self.boardArray[57] = WKnight()
        self.boardArray[56] = WRook()
        
        for i in range(0, 8):
            self.boardArray[i + 8] = BPawn()
            self.boardArray[i + 48] = WPawn()
    '''
    - moves a piece from one spot on the board to another
    '''
    def move(self, src, dst):
        if(src >= 0 and src < 64 and dst >= 0 and dst < 64 and self.boardArray[src] != 0):
            self.boardArray[dst] = self.boardArray[src]
            self.boardArray[src] = 0
        else:
            print("Invalid Inputs")
        




            
        
