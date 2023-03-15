# AKI 09/03/2023

import pygame
import sys
from const import *
from game import Game


class Main:

    def __init__(self):  # method always called when we call an object
        pygame.init()  # when we create an attribute we use "self" keyword
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CHESS")  # caption of application
        self.game = Game()

    def mainloop(self):  # main loop

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_col = dragger.mouseX // SQSIZE  # col = x
                    clicked_row = dragger.mouseY // SQSIZE  # row = y

                    print(dragger.mouseX, clicked_col)
                    print(dragger.mouseY, clicked_row)

                    # if clicked square has piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                # release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                # quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
