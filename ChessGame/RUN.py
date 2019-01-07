# import the pygame module, so you can use it
import pygame
import os
import Game
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Chess!!!")
    ChessGame = Game.Game(screen) 
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        ChessGame.DisplayBoard()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            #sets move src and dst with mouse location
            if pygame.mouse.get_pressed()[0] == 1:
                ChessGame.getMousePos()
                
            # moves pieces
            if pygame.key.get_pressed()[pygame.K_RETURN] == True and ChessGame.moved == False:
                ChessGame.movePiece()
    
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
pygame.quit()
