# The canvas displays all visual information
import pygame

import Sprites

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Canvas:

    def __init__(self, width, height):
        # initialize our pygame instance
        pygame.init()

        # setting our width/height
        self._width = width
        self._height = height

        # setting our display
        self._display = pygame.display.set_mode((width, height))

        self._selectionStart = (0,0)
        self._selectionEnd = (0,0)
        self._selecting = False

    """
    updates the canvas
    """
    def update(self, x, y, inputHandler, npc):

        self._display.fill(WHITE)

        self._display.blit(npc.sprite, (400, 600))

        inputHandler.console.display(inputHandler.user_input, self.display,self._height,self._width)

        self._display.blit(Sprites.CHAR_N, (x, y))
        self._display.blit(npc.sprite, (npc.x, npc.y))

        # draw queue stuff
        if self._selecting:
            width = self._selectionEnd[0] - self._selectionStart[0]
            height = self._selectionEnd[1] - self._selectionStart[1]
            pygame.draw.rect(self._display, BLACK, (self._selectionStart[0],self._selectionStart[1] ,width, height), 1)

        pygame.display.update()

    def startDrawSelection(self, x, y):
        self._selecting = True
        self._selectionStart = (x,y)
        self._selectionEnd = (x, y)

    def drawSelectionBox(self, x, y):
        self._selectionEnd = (x,y)

    def endDrawSelection(self):
        self._selecting = False

    """
    Get's the game width
    """
    @property
    def width(self):
        return self._width

    """
    Retrieves game height
    """
    @property
    def height(self):
        return self._height

    """
    Retrieves the display
    """
    @property
    def display(self):
        return self._display
