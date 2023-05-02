# AKI 09/03/2023

import pygame as py  # Import the pygame library and give it the alias py
import sys  # Import the sys library for system-level operations
from const import *  # Import all constants from the const module
from game import Game  # Import the Game class from the game module
from square import Square  # Import the Square class from the square module
from move import Move  # Import the Move class from the move module


class Main:

    def __init__(self):                                         # Method called on new class object creation.
        py.init()                                               # Initialize py library
        self.interface = py.display.set_mode((WIDTH, HEIGHT))   # Create game display surface with given dimensions.
        py.display.set_caption("CHESS")                         # caption of application
        self.game = Game()                                      # Instantiate Game class and store in 'game' attribute.

    # load the icon image
    icon = py.image.load('assets/images/icon.png')
    # set the icon
    py.display.set_icon(icon)  # new icon

    def mainloop(self): # main loop

        interface = self.interface      # Assigning the interface object
        game = self.game                # Assigning the game object
        board = self.game.board         # Assigning the board object
        dragger = self.game.dragger     # Assigning the dragger object

        def show_method(interface):
            game.show_bg(interface)            # Show the game background on the interface
            game.show_last_move(interface)     # Show the last move on the interface
            game.show_moves(interface)         # Show the valid moves for the current piece on the interface
            game.show_pieces(interface)        # Show the chess pieces on the interface

        while True:
            # show methods
            show_method(interface)
            
            game.show_hover(interface)         # Show the hover effect on the interface

            if dragger.dragging:
                dragger.update_blit(interface)  # Check if player is dragging the piece.

            for event in py.event.get():

                # click
                if event.type == py.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_col = dragger.mouseX // SQSIZE  # col = x
                    clicked_row = dragger.mouseY // SQSIZE  # row = y

                    # if clicked square has piece ?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece (color)?
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, flag=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            # show method
                            show_method(interface)

                # mouse motion
                elif event.type == py.MOUSEMOTION:
                    # Calculates the row and column of the square that the mouse is currently over
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    # Sets the hover effect on the square that the mouse is currently over
                    game.set_hover(motion_row, motion_col)

                    # If the user is currently dragging a piece, update its position to follow the mouse
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        show_method(interface)          # Show the available moves for the piece being dragged
                        game.show_hover(interface)      # Display hover effect on destination square for dragged piece
                        dragger.update_blit(interface)  # Update the display with the new position of the dragged piece

                # release
                elif event.type == py.MOUSEBUTTONUP:
                    # If the user is currently dragging a piece
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        # Update the position of the dragged piece to match the mouse
                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # valid move?
                        if board.valid_move(dragger.piece, move):
                            captured = board.squares[released_row][released_col].has_piece()

                            # Make the move on the board
                            board.move(dragger.piece, move)
                            board.set_true_en_passant(dragger.piece)

                            # If the move captures a piece, play a sound
                            game.play_sound(captured)  
                            # show methods
                            show_method(interface)
                            if piece.moved == True:
                                print(str(Square.get_alphacol(final.col)) +
                                      str(ROWS-final.row))
                            # next turn
                            game.next_turn()
                    # End the drag operation
                    dragger.undrag_piece()

                # key press
                elif event.type == py.KEYDOWN:
                    # change themes
                    if event.key == py.K_t:     # If the "t" key is pressed, change the theme and play a sound effect
                        print('theme change')
                        game.change_effect()
                        game.change_theme()
                    # reset
                    if event.key == py.K_r:     # If the "r" key is pressed, reset the game and play a sound effect
                        game.reset()
                        # add sound effect
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # quit
                elif event.type == py.QUIT:
                    py.quit()
                    sys.exit()

            py.display.update()     # Update the Pygame display


main = Main()           # Create an instance of the Main class
print("Running...")     # Print a message to indicate that the program is running
main.mainloop()         # Start the main event loop of the Pygame library