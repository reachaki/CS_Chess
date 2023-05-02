import pygame as py  # Import Pygame library for creating games
from const import *  # Import constants from another module called "const"

class Dragger:

    def __init__(self):
        self.piece = None  # Initialize piece to None
        self.dragging = False  # Initialize dragging to False
        self.mouseX = 0  # Initialize mouseX to 0
        self.mouseY = 0  # Initialize mouseY to 0
        self.initial_row = 0  # Initialize initial_row to 0
        self.initial_col = 0  # Initialize initial_col to 0

    # blit method
    def update_blit(self, surface):
        # set_texture method
        self.piece.set_texture(size=100)  # Set texture size
        texture = self.piece.texture  # Get texture
        # load image
        img = py.image.load(texture)  # Load image from texture
        # set image center
        img_center = (self.mouseX, self.mouseY)  # Get center of image
        self.piece.texture_rect = img.get_rect(center=img_center)  # Set texture rect
        # blit
        surface.blit(img, self.piece.texture_rect)  # Draw image on surface

    # other method
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos  # Set mouseX and mouseY to current position of mouse

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE  # Set initial row to integer division of y-coordinate of pos by SQSIZE
        self.initial_col = pos[0] // SQSIZE  # Set initial col to integer division of x-coordinate of pos by SQSIZE

    def drag_piece(self, piece):
        self.piece = piece  # Set piece to the input parameter
        self.dragging = True  # Set dragging to True

    def undrag_piece(self):
        self.piece = None  # Set piece to None
        self.dragging = False  # Set dragging to False
