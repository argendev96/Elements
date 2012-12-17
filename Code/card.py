#!/usr/bin/python

import pygame

###########################################################
# File - Class that represents a card from Elements
# variables - name, image, level, details
# functions - __init__, getName, getImage, getLevel,
#   getDetails, x, y
# Date Created - 11/5/12 TUES 22:16
# Date Last Modified - 11/22/12 THU 23:55
###########################################################

class Card(object):
    # Constructor to set up properties of the card
    #   level, image, name, details, etc
    def __init__(self, name, image, level, details, x, y):
        self.name = name
        self.level = level
        self.details = details

        self.x, self.y = x, y
        self.width, self.height = 90,131

        # load file from filename and then transfrom it to certain dimensions
        self.image = pygame.image.load(image).convert()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    # Getters
    def getName(self):
        return self.name

    def getImage(self):
        return self.image

    def getLevel(self):
        return self.level

    def getDetails(self):
        return self.details

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
