import pygame as py


class Sound:

    def __init__(self, path):
        self.path = path                    #Set path to sound file path
        self.sound = py.mixer.Sound(path)   # Load the sound 

    def play(self):
        # Play the sound 
        py.mixer.Sound.play(self.sound)
