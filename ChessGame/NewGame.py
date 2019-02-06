import pygame
import os
import BoardState
from Constants import *


'''
-loads sprites for all of the different pieces
-blits them onto the board
-updates the board
'''
class Game(object):
    '''
     - Initializes the Game
     - The screen parameter is the main screen where the game will appear, it is saved in the field screen
     - The board field stores the BoardState Object
     
    '''
    def __init__(self, screen):
        self.Board = BoardState.BoardState()
        self.screen = screen
        self.mouseClicked = -1
        self.prevClicked = -1
        self.moved = False 
    '''
     -Updates what is displayed on the screen
    '''
    def DisplayBoard(self):
        #initalizes and displays chessboard backround
        backround = pygame.image.load(os.path.join('Sprites', 'Board.png' ))
        self.screen.blit(backround,(0,0))
        

        # Initializing indicator sprites for source and destination spots for moving pieces and then
        # blitting indicators to the screen
        Destination = pygame.image.load(os.path.join('Sprites', 'Destination.png'))
        Source = pygame.image.load(os.path.join('Sprites', 'Source.png'))
        if(self.prevClicked != -1 and not self.moved):
            sRow = int(self.prevClicked / 8)
            sRow = sRow * 100 
            sColumn = int(self.prevClicked % 8)
            sColumn = sColumn * 100  
            self.screen.blit(Source, (sColumn, sRow))
        if(self.mouseClicked != -1 and not self.moved):
            dRow = int(self.mouseClicked / 8)
            dRow = dRow * 100 
            dColumn = int(self.mouseClicked % 8)
            dColumn = dColumn * 100  
            self.screen.blit(Destination, (dColumn, dRow))
                             

        for i in range(B_START, B_END):
            row = int(i / 8)
            row = row * 100 + 20
            column = int(i % 8)
            column = column * 100 + 20
            if(self.Board.boardArray[i] != 0):
                self.screen.blit(self.Board.boardArray[i].sprite, (column , row ))
        pygame.display.flip()
        

    '''
    -sets the mouse clicked  and previous clicked fields
    -sets them in terms of board square4
    '''
    def getMousePos(self):
        position = pygame.mouse.get_pos()
        x = position[0]
        y = position[1]
        x = int(x / 100)
        y = int(y / 100)
        self.prevClicked = self.mouseClicked
        self.mouseClicked = (y * 8) + x
        self.moved = False
    '''
    - moves a piece from prev clicked to mouseclicked positions
    '''
    def movePiece(self):
        self.Board.move(self.prevClicked, self.mouseClicked)
        self.moved = True

    
                    
                                                                               
