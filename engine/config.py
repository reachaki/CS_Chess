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
        # font
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        brown = Theme()
        red = Theme()
        orange = Theme()
        green = Theme()
        blue = Theme()
        purple = Theme()
        ice = Theme()

        self.theme = [brown, red, orange, green, blue, purple, ice]
