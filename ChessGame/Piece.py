import pygame
import os


class Piece(object):
    def output(self):
        print(self.row)
        print(self.column)
        print(self.name)
        
class WKing(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "White King"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WKING.png'))

class WQueen(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "White Queen"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WQueen.png'))



class WRook(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "White Rook"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WRook.png'))

class WBishop(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "White Bishop"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WBishop.png'))

class WKnight(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "White Knight"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WKnight.png'))
        
class WPawn(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "White Pawn"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'WPawn.png'))

class BKing(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "Black King"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BKING.png'))


class BQueen(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "Black Queen"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BQueen.png'))


class BRook(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "Black Rook"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BRook.png'))


class BBishop(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "Black Bishop"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BBishop.png'))


class BKnight(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "Black Knight"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BKnight.png'))

class BPawn(Piece):
    def __init__(self):
        self.column = 20
        self.row = 10
        self.name = "Black Pawn"
        self.sprite = pygame.image.load(os.path.join('Sprites', 'BPawn.png'))
