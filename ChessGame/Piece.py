import pygame
import os
from BoardState import *

class Piece(object):

    def checkPiece(self, loc):
        if(self.board[loc] == 0):
            return 1
        elif(self.board[loc].color == 0):
            return 0
        else:
            return 2    
    
    #Calculates valid moves for one space in the diagonal direction
    def diagonal(self):
        if(self.location - 9 >= 0 and self.location % 8 > 0 ):
            self.moves[self.location - 9] = 1
        if(self.location - 7 >= 0 and self.location % 8 < 7):
            self.moves[self.location - 7] = 1
        if(self.location + 7 <= 63 and self.location % 8 > 0):
            self.moves[self.location + 7 ] = 1
        if(self.location + 9 <= 63 and self.location % 8 < 7):
            self.moves[self.location + 9] = 1
    #Calculates valid moves for one space in a horizontal or vertical direction 
    def horiz_vert(self):
        if(self.location + 8 <= 63):
            self.moves[self.location + 8] = 1
        if(self.location - 8 >= 0): 
            self.moves[self.location - 8] = 1
        if(self.location - 1 >= 0 and self.location % 8 > 0):
            self.moves[self.location - 1] = 1
        if(self.location + 1 <= 63 and self.location % 8 < 7):
            self.moves[self.location + 1] = 1

    #Calculates one move down from a pieces current
    def downMove(self):
        if(self.location + 8 <= 63):
            self.moves[self.location + 8] = 1

    #Calculates one move up from a pieces current
    def upMove(self):
        if(self.location - 8 >= 0):
            self.moves[self.location - 8] = 1

    #Calculates the valid "L" moves for Knight pieces
    def knightMoves(self):
        loc = self.location

        #U1-L2
        if(loc / 8 > 0 and loc % 8 > 1 and loc - 10 > 0):
            self.moves[loc - 10] = 1

        #U1-R2
        if(loc / 8 > 0 and loc % 8 < 6 and loc - 6 > 0):
            self.moves[loc - 6] = 1

        #U2-L1
        if(loc / 8 > 1 and loc % 8 > 0 and loc - 17 > 0):
            self.moves[loc - 17] = 1

        #U2-R1
        if(loc / 8 > 1 and loc % 8 < 7 and loc - 15 > 0):
            self.moves[loc - 15] = 1
            
        #D1-L2
        if(loc / 8 < 7 and loc % 8 > 1 ):
            self.moves[loc + 6] = 1

        #D1-R2
        if(loc / 8 < 7 and loc % 8 < 6):
            self.moves[loc + 10] = 1

        #D2-L1
        if(loc / 8 < 6 and loc % 8 > 1):
            self.moves[loc + 15] = 1

        #D2-L1
        if(loc / 8 < 6 and loc % 8 < 7):
            self.moves[loc + 17] = 1


    #Calculates moves on the horizontal line that the piece is on
    def horizontalLine(self):
        temp = self.location - int(self.location % 8)
        lastInRow = temp + 7
        while(temp <= lastInRow):
            if(temp != self.location):
                self.moves[temp] = 1
            temp = temp + 1
        
    #Calculates moves on the vertical line that the piece is on
    def verticalLine(self):
        temp = int(self.location % 8)
        lastInColumn = temp + 56
        while(temp <= lastInColumn):
            if(temp != self.location):
                self.moves[temp] = 1
            temp = temp + 8
        
    #Calculates moves on the diagonal lines that the piece is on
    def diagonalLine(self):
        temp = self.location
        back = int(self.location % 8)
        forward = 7 - int(self.location % 8)
        #down right
        while(forward > 0 and temp + 9 <= 63):
            temp += 9
            self.moves[temp] = 1
            forward -= 1

        temp = self.location

        #down left
        while(back > 0 and temp + 7 < 63):
            temp += 7
            self.moves[temp] = 1
            back -= 1

        temp = self.location
        forward = 7 - int(self.location % 8)

        #up right
        while(forward > 0 and temp - 7 > 0):
            temp -= 7
            self.moves[temp] = 1
            forward -= 1
        back = int(self.location % 8)
        temp = self.location
        print(back)
        #up left
        while(back > 0 and temp - 9 >= 0):
            temp -= 9
            self.moves[temp] = 1
            back -= 1
        
'''
 -All classes below are more specific piece classes
 -They all have a set of fields representative of that piece
 -They also all can calculate valid moves based on the type of piece they are
'''
class WKing(Piece):
    def __init__(self, loc, boardArray):
        self.board = boardArray
        self.moves = [0] * 64
        self.color = 1
        self.location = loc
        self.name = "White King"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WKING.png'))
        
    def calculateMoves(self):
        self.diagonal()
        self.horiz_vert()    

class WQueen(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 1
        self.location = loc
        self.name = "White Queen"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WQueen.png'))
    def calculateMoves(self):
        self.diagonalLine()
        self.horizontalLine()
        self.verticalLine()


class WRook(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 1
        self.location = loc
        self.name = "White Rook"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WRook.png'))
    def calculateMoves(self):
        self.horizontalLine()
        self.verticalLine()
        
class WBishop(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 1
        self.location = loc
        self.name = "White Bishop"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WBishop.png'))
    def calculateMoves(self):
        self.diagonalLine()
        
class WKnight(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 1
        self.location = loc
        self.name = "White Knight"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WKnight.png'))
    def calculateMoves(self):
        self.knightMoves()
        
class WPawn(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 1
        self.location = loc
        self.name = "White Pawn"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WPawn.png'))
    def calculateMoves(self):
        self.upMove()

class BKing(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 0
        self.location = loc
        self.name = "Black King"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BKING.png'))
    def calculateMoves(self):
        self.diagonal()
        self.horiz_vert()

class BQueen(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 0
        self.location = loc
        self.name = "Black Queen"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BQueen.png'))
    def calculateMoves(self):
        self.diagonalLine()
        self.horizontalLine()
        self.verticalLine()

class BRook(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 0
        self.location = loc
        self.name = "Black Rook"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BRook.png'))
    def calculateMoves(self):
        self.horizontalLine()
        self.verticalLine()

class BBishop(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 0
        self.location = loc
        self.name = "Black Bishop"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BBishop.png'))
    def calculateMoves(self):
        self.diagonalLine()

class BKnight(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64
        self.color = 0
        self.location = loc
        self.name = "Black Knight"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BKnight.png'))
    def calculateMoves(self):
        self.knightMoves()
        
class BPawn(Piece):
    def __init__(self, loc):
        self.moves = [0] * 64 
        self.color = 0
        self.location = loc
        self.name = "Black Pawn"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BPawn.png'))
    def calculateMoves(self):
        self.downMove()

