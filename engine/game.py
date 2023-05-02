import pygame as py  # Import the pygame library and give it the alias py
from const import *  # Import all constants from the const module
from board import Board  # Import the Board class from the board module
from dragger import Dragger  # Import the Dragger class from the dragger module
from config import Config  # Import the Config class from the config module
from square import Square  # Import the Square class from the square module


class Game:

    def __init__(self):
    
        self.next_player = 'white'  # Initialize the next player to white
        self.hovered_sqr = None     # Initialize the hovered square to None
        self.board = Board()        # Create a new instance of the Board class
        self.dragger = Dragger()    # Create a new instance of the Dragger class
        self.config = Config()      # Create a new instance of the Config class


    # show methods
    def show_bg(self, surface):

        theme = self.config.theme   # Get the theme for the board from the configuration

        # Iterate over each row and column to color the squares
        for row in range(ROWS):
            for col in range(COLS):
                # Set the color for the square
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                # Set the rect object for the square
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # Draw the square on the surface
                py.draw.rect(surface, color, rect)

                # row cooridnates
                if col == 0:
                    # color
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.config.font.render(str(ROWS-row), 10, color)
                    lbl_pos = (5, 5 + row * SQSIZE)
                    # blit
                    surface.blit(lbl, lbl_pos)

                # col coordinates
                if row == 7:
                    # color
                    color = theme.bg.dark if (
                        row + col) % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.config.font.render(
                        Square.get_alphacol(col), 10, color)
                    lbl_pos = (col * SQSIZE + SQSIZE - 20, HEIGHT - 20)
                    # blit
                    surface.blit(lbl, lbl_pos)

    # Show pieces on the chessboard
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # piece?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    # Check if the current piece is not the one being dragged
                    if piece is not self.dragger.piece:
                        # Set the texture of the current piece
                        piece.set_texture(size=80)
                        # Load the image of the current piece
                        img = py.image.load(piece.texture)
                        # Set the center of the image of the current piece
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        # Set the texture rectangle of the current piece
                        piece.texture_rect = img.get_rect(center=img_center)
                        # Blit the image of the current piece on the surface
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        theme = self.config.theme
        # check if there is a piece being dragged
        if self.dragger.dragging:
            piece = self.dragger.piece
            # loop over all valid moves of the piece
            for move in piece.moves:
                # set the color of the move
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                # position
                x = move.final.col * SQSIZE + SQSIZE // 2
                y = move.final.row * SQSIZE + SQSIZE // 2
                # radius
                radius = SQSIZE // 2
                # draw circle
                py.draw.circle(surface, color, (x, y), radius, 8)

    def show_last_move(self, surface):
        theme = self.config.theme
        # check if a move was played previously
        if self.board.last_move:    
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                # color
                color = theme.trace.light if (
                    pos.row + pos.col) % 2 == 0 else theme.trace.dark
                # rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                py.draw.rect(surface, color, rect)

    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (255, 255, 255)
            # rect
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # blit
            py.draw.rect(surface, color, rect, width=2)

    # other methods

    # Change player turn by toggling next_player between 'white' and 'black'.
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    # Set the hovered square object using the given row and column.
    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]

    # Change the current theme by calling the change_theme method of the Config object.
    def change_theme(self):
        self.config.change_theme()

    # Play a sound effect depending on whether a piece was captured or not.
    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()

    # Change the sound effect played when a move is made by calling the change_sound method of the Config object.
    def change_effect(self):
        self.config.change_sound.play()

    # Reset the game by reinitializing the class variables using the init method.
    def reset(self):
        self.__init__()