# AKI 09/03/2023

import pygame as py
import sys
from const import *
from game import Game
from square import Square
from move import Move


class Main:

    def __init__(self):                                         # Method called on new class object creation.
        py.init()                                           # Initialize py library
        self.interface = py.display.set_mode((WIDTH, HEIGHT))  # Create game display surface with given dimensions.
        py.display.set_caption("CHESS")                     # caption of application
        self.game = Game()                                      # Instantiate Game class and store in 'game' attribute.

    # load the icon image
    icon = py.image.load('assets/images/icon.png')
    # set the icon
    py.display.set_icon(icon)  # new icon

    def mainloop(self): # main loop

        interface = self.interface            # Assigning the interface object
        game = self.game                # Assigning the game object
        board = self.game.board         # Assigning the board object
        dragger = self.game.dragger     # Assigning the dragger object

        while True:
            # show methods
            game.show_bg(interface)            # Show the game background on the interface
            game.show_last_move(interface)     # Show the last move on the interface
            game.show_moves(interface)         # Show the valid moves for the current piece on the interface
            game.show_pieces(interface)        # Show the chess pieces on the interface
            game.show_hover(interface)         # Show the hover effect on the interface

            if dragger.dragging:
                dragger.update_blit(interface) # Check if player is dragging the piece.

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
                            board.calc_moves(
                                piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            # show method
                            game.show_bg(interface)
                            game.show_last_move(interface)
                            game.show_moves(interface)
                            game.show_pieces(interface)

                # mouse motion
                elif event.type == py.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(interface)
                        # show methods
                        game.show_last_move(interface)
                        game.show_moves(interface)
                        game.show_pieces(interface)
                        game.show_hover(interface)
                        dragger.update_blit(interface)

                # release
                elif event.type == py.MOUSEBUTTONUP:

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # create possible move
                        initial = Square(dragger.initial_row,
                                         dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # valid move?
                        if board.valid_move(dragger.piece, move):
                            captured = board.squares[released_row][released_col].has_piece(
                            )

                            board.move(dragger.piece, move)

                            board.set_true_en_passant(dragger.piece)

                            # sounds
                            game.play_sound(captured)
                            # show methods
                            game.show_bg(interface)
                            game.show_last_move(interface)
                            game.show_moves(interface)
                            game.show_pieces(interface)
                            if piece.moved == True:
                                print(str(Square.get_alphacol(final.col)) +
                                      str(ROWS-final.row))
                            # next turn
                            game.next_turn()

                    dragger.undrag_piece()

                # key press
                elif event.type == py.KEYDOWN:
                    # change themes
                    if event.key == py.K_t:
                        print('theme change')
                        game.change_effect()
                        game.change_theme()
                    # reset
                    if event.key == py.K_r:
                        game.reset()
                        # add sound effect
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # quit
                elif event.type == py.QUIT:
                    py.quit()
                    sys.exit()

            py.display.update()


main = Main()
print("Running...")
main.mainloop()
