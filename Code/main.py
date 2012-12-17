#!/usr/bin/python

###########################################################
# File - Class that handles the exectution of the game
# variables - w, h, cardmanager, cardmovement
# functions - __init__, update, keyUp, keyDown, mouseUp,
#   mouseMotion, draw
# Date Downloaded - 11/1/12 THU 21:03
# Date Modified - 11/7/12 WED 18:30
# Date Last Modified - 11/22/12 FRI 23:40
###########################################################

from pygamehelper import *
from pygame import *
from pygame.locals import *
from math import e, pi, cos, sin, sqrt
from random import uniform

from cardmanager import *

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 1200, 800
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((56, 49, 52)))
        
        # Cardmanager that manages where the cards are in the deck and on the field
        self.cardmanager = Cardmanager()
        # information about the movement of a card
        # consists of [0] = card in hand/played, [1] = cardindex, [2] = cardoffset, TODO: [3] = cardinitialpos
        self.cardmovement = []
        
    def update(self):
        pass
        
    def keyUp(self, key):
        pass
    
    # When the user releases the mouse then the card movement will stop
    def mouseUp(self, button, pos):
        # if the card has been clicked and has been moved
        if self.cardmovement != []:
            # if the card went from the pile to the field, then move it to the corresponding list
            if self.cardmovement[0] == "hand":
                # get the object for the current card being moved from the hand pile
                currentRect = self.cardmanager.handCards[self.cardmovement[1]].getRect()

                for playArea in self.cardmanager.playareas:
                    if currentRect.colliderect(playArea.getRect()):
                        self.cardmanager.playCard(self.cardmovement[1])

            self.cardmovement = []

    # When the mouse is clicked if it clicks on a card then set...
    #   self.cardSelected to true and the card will move in mouseMotion(...)
    #TODO: can probably shorten down these loops or make them more efficient and fix this fucking code blob, jesus
    def mouseDown(self, button, pos):
        playedRects = self.cardmanager.getPlayedRects()
        handRects = self.cardmanager.getHandRects()

        for i in range(len(handRects)):
            # if the mouse was clicked inside the visible area of the card
            if (pos[0] > handRects[i].x and pos[0] < handRects[i].x + handRects[i].width) and\
                (pos[1] > handRects[i].y and pos[1] < handRects[i].y + handRects[i].height):
                    self.cardmovement = ["hand", i, (pos[0] - handRects[i].x, pos[1] - handRects[i].y)]

        for i in range(len(playedRects)):
            # if the mouse was clicked inside the card
            if (pos[0] > playedRects[i].x and pos[0] < playedRects[i].x + playedRects[i].width) and\
                (pos[1] > playedRects[i].y and pos[1] < playedRects[i].y + playedRects[i].height):
                    self.cardmovement = ["played", i, (pos[0] - playedRects[i].x, pos[1] - playedRects[i].y)]

    # When the mouse is moved, if a card is being moved, then move that card...
    #   in relation to the mouse
    #TODO: if statements in here can probably be combined
    def mouseMotion(self, buttons, pos, rel):
        # if the card is moving
        if self.cardmovement != []:
            i = self.cardmovement[1]
            # offset is the x difference between mouse and top left corner of card and y difference
            offset = self.cardmovement[2]

            # if the card being moved is a card from the hand then move the corresponding card from the list
            if self.cardmovement[0] == "hand":
                cardRect = self.cardmanager.getHandRects()[i]
                # set the x and y for the card by getting the position of the mouse then set the rect in the list
                cardRect.x, cardRect.y = pos[0] - offset[0], pos[1] - offset[1]
                # TODO: Change this to a method
                self.cardmanager.handCards[i].x, self.cardmanager.handCards[i].y = cardRect.x, cardRect.y
            # if the card is from the playing field then move it
            elif self.cardmovement[0] == "played":
                cardRect = self.cardmanager.getPlayedRects()[i]
                # set the x and y for the card by getting the mous using the offset in cardMovement
                cardRect.x, cardRect.y = pos[0] - offset[0], pos[1] - offset[1]
                # TODO: Change this to a method
                self.cardmanager.playedCards[i].x, self.cardmanager.playedCards[i].y = cardRect.x, cardRect.y

    def draw(self):
        # Fill the screen will a brown/black/grey color
        self.screen.fill((56, 49, 52))

        for card in self.cardmanager.getAllCards():
            self.screen.blit(card.getImage(), (card.getX(), card.getY()))

        for area in self.cardmanager.playareas:
            self._drawPlayCorners(area)
    
    # Function that when given a play area, will draw the 4 corners for that play area onto self.screen
    # TODO: maybe make x + width/y+height a variable instead of adding them everytime
    def _drawPlayCorners(self, area):
        x, y = area.x, area.y
        width, height = area.width, area.height
        cornerLen = area.cornerLen
        color = area.color
        
        # the top left corner
        pygame.draw.line(self.screen, color, (x, y), (x + cornerLen, y))
        pygame.draw.line(self.screen, color, (x, y), (x, y + cornerLen))
        # the top right corner
        pygame.draw.line(self.screen, color, (x + width, y), ((x + width) - cornerLen, y))
        pygame.draw.line(self.screen, color, (x + width, y), (x + width, y + cornerLen))
        # the bottom left corner
        pygame.draw.line(self.screen, color, (x, y + height), (x + cornerLen, y + height))
        pygame.draw.line(self.screen, color, (x, y + height), (x, (y + height) - cornerLen))
        # the bottom right corner
        pygame.draw.line(self.screen, color, (x + width, y + height), ((x + width) - cornerLen, y + height))
        pygame.draw.line(self.screen, color, (x + width, y + height), (x + width, (y + height) - cornerLen))
        
if __name__ == "__main__":
    s = Starter()
    s.mainLoop(40)
