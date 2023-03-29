import pygame
import os
from sound import Sound
from theme import Theme


class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('Futura', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav'))
        self.change_sound = Sound(
            os.path.join('assets/sounds/change.wav')
        )

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        brown = Theme((237, 214, 176), (185, 135, 97), (247, 235, 88),
                      (220, 196, 49), (215, 193, 159), (166, 122, 88))
        red = Theme((240, 216, 191), (186, 85, 70), (244, 232, 170),
                    (217, 167, 109), (217, 195, 172), (168, 77, 63))
        green = Theme((237, 238, 209), (119, 153, 82), (247, 247, 105),
                      (188, 205, 40), (214, 215, 188), (107, 138, 73))
        blue = Theme((236, 236, 215), (77, 109, 146), (118, 201, 236),
                     (38, 138, 201), (213, 213, 194), (69, 98, 132))
        purple = Theme((239, 239, 239), (136, 119, 183), (183, 206, 221),
                       (131, 147, 193), (216, 216, 216), (123, 107, 165))
        ice = Theme((216, 228, 231), (112, 149, 171), (151, 218, 234),
                    (106, 185, 209), (196, 206, 209), (110, 143, 161))

        self.themes = [brown, red, green, blue, purple, ice]
