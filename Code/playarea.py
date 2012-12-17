#!/usr/bin/python

###########################################################
# File - Class that is the area where the cards can
#   can be played
# variables - x, y, width, height, color
# functions - __init__, getRect
# Date Created - 11/23/12 FRI 12:30
# Date Last Modified - 11/23/12 FRI 12:31
###########################################################

import pygame

class Playarea(object):
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height

        self.color = (255, 255, 255)
        
        # Length of the corner to be drawn
        self.cornerLen = 10

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
