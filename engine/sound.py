import pygame as py


class Sound:

    def __init__(self, path):
        self.path = path
        self.sound = py.mixer.Sound(path)

    def play(self):
        py.mixer.Sound.play(self.sound)
