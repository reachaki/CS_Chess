# AKI 09/03/2023

import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move


class Main:

    def __init__(self):  # method always called when we call an object
        pygame.init()  # when we create an attribute we use "self" keyword
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CHESS")  # caption of application
        self.game = Game()

    # load the icon image
    icon = pygame.image.load('assets/images/icon.png')
    # set the icon
    pygame.display.set_icon(icon)

    def mainloop(self):  # main loop

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_col = dragger.mouseX // SQSIZE  # col = x
                    clicked_row = dragger.mouseY // SQSIZE  # row = y

                    # if clicked square has piece ?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece (color)?
                        if piece.color == game.next_player:
                            board.clac_moves(
                                piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            # show method
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        # show methods
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)

                # release
                elif event.type == pygame.MOUSEBUTTONUP:

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
                            # sounds
                            game.play_sound(captured)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                            if piece.moved == True:
                                print(str(Square.get_alphacol(final.col)) +
                                      str(ROWS-final.row))
                            # next turn
                            game.next_turn()

                    dragger.undrag_piece()

                # key press
                elif event.type == pygame.KEYDOWN:
                    # change themes
                    if event.key == pygame.K_t:
                        print('theme change')
                        game.change_effect()
                        game.change_theme()
                    # reset
                    if event.key == pygame.K_r:
                        game.reset()
                        # add sound effect
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
