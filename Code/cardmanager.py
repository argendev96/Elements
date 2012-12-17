#!/usr/bin/python

from card import *
from playarea import *

import pygame

###########################################################
# File - Class that manages the cards and their locations
# variables - cards
# functions - __init__, getCards
# Date Created - 11/5/12 TUES 23:10
# Date Last Modified - 11/23/12 SAT 00:35
###########################################################

class Cardmanager(object):
    # Constructor to set up the location of the players hand
    #   is set it a defined location, not a param
    def __init__(self):
        # the hand consits of overlapping cards with 25 pixels inbetween
        self.overlapHand = 25
        # the playareas are separated along the x-axis by 175 pixels
        self.overlapPlay = 175

        # List of playareas (where the cards in the hand can be moved to)
        # TODO: do something with the heights and the widths (variablize it)
        self.playareas = [Playarea(50 + self.overlapPlay * i, 550, 93, 134) for i in range(5)]

        # List of cards that are shown in the CardHolder
        # An example card is loaded that is an ace of spades with information
        # NOTE: Card dimensions for card class is area that is viewable or clickable of card
        self.handCards = [Card("Ace of Spades", "/home/matias/Documents/Python/Elements/Images/ace_of_spades",\
                        5, "An example for details", 1000, 550 + self.overlapHand * i) for i in range(5)]
        
        # the list of the cards that have been played and are visible
        self.playedCards = []

    # Moves the card from the hand list to the played list because it was played in the game
    def playCard(self, i):
        # get the card moved and then add it to the playedcards and then remove it from cards in hand
        handCard = self.handCards[i]

        self.playedCards.append(handCard)
        self.handCards.pop(i)

    # Getters
    # Gets the rectangles that are visible for each card in the hand (that is stacked)
    def getHandRects(self):
        # use self.overlap as the height of the rect because the
        #   visible part of the card is this high
        # [:-1] will go thru all cards except the last one which has a different visible height
        handrects = [pygame.Rect(card.x, card.y, card.width, self.overlapHand) for card in self.handCards[:-1]]

        # add on the visible portion of the last card in the hand
        # if there are no cards in your hand then this will throw exception
        #   the first part will not and will simply return an empty list
        try:
            lastCard = self.handCards[-1]
            handrects.append(pygame.Rect(lastCard.x, lastCard.y, lastCard.width, lastCard.height))
        except IndexError:
            print "There are no cards in the hand!@!@"

        return handrects

    # Gets the rectangles of the played cards (those that are on the playing field)
    def getPlayedRects(self):
        return [pygame.Rect(card.x, card.y, card.width, card.height) for card in self.playedCards]

    # Return all of the cards including the ones in the hand and the played ones
    def getAllCards(self):
        return self.handCards + self.playedCards

    def getHandCards(self):
        return self.handCards

    def getPlayedCards(self):
        return self.playedCards
