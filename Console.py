# this is our font size we use for our console
import pygame
from pygame import font

from parsing.parse import Parser
from Canvas import WHITE, BLACK

CONSOLE_FONT_SIZE = 16
# how long the console should be
CONSOLE_LENGTH = 5
CONSOLE_LINE_WIDTH = 3

class Console:

    def __init__(self,size):
        # length of the console
        self._size = 20

        # stores our Message objects in a list
        self._log = []
        # initialize our log to the empty string for each entry
        for i in range(0,self._size):
            self._log.append(Message(["?"*40]))

        # parsing for commands
        self._parser = Parser(self)

    """
    Returns overall size of the console
    """
    @property
    def size(self):
        return self._size

    @property
    def log(self):
        return self._log

    """
    pushes a message onto the console
    """
    def push(self, message):
        # if we are pushing a trivial string we wrap it around our Message class for ease
        if isinstance(message, str):
            # we have to try and parse this message
            self._parser.parse(message)

            print("converted...")
            message = Message([message])

        # iterate from the top, pushing each message up 1
        for i in range(self._size-1, 0, -1):

            self._log[i] = self._log[i-1]
        # finally set the bottom equal to the message

        self._log[0] = message

    """
    displays the console to the screen given a valid display
    """
    def display(self, display, height, width, userinput):
        # console text
        font = pygame.font.Font('freesansbold.ttf', CONSOLE_FONT_SIZE)

        for i in range(0, self.size):
            currMessage = self._log[i]
            # we continue outputting, until the bitter end
            string, image = currMessage.pop(0)
            j = 0
            # why python have no do while whatever
            # shift from previous text/images
            shift = 0
            while string:

                currect = pygame.Rect(shift, height - (i+2)*CONSOLE_FONT_SIZE, width,CONSOLE_FONT_SIZE)
                curtext = font.render(string, True, WHITE, BLACK)
                shift += len(string)*CONSOLE_FONT_SIZE/1.9
                # if we got a image
                if image:
                    # need to scale it down to our font size
                    display.blit(pygame.transform.scale(image, (CONSOLE_FONT_SIZE + 1, CONSOLE_FONT_SIZE + 1)), (shift, height - (i+2) * CONSOLE_FONT_SIZE), special_flags = pygame.BLEND_RGBA_MULT)
                    shift += CONSOLE_FONT_SIZE
                display.blit(curtext, currect)
                j += 1
                string, image = currMessage.pop(j)

        # create a text surface object,
        # on which text is drawn on it.
        text = font.render(userinput, True, WHITE, BLACK)

        # text surface object
        textRect = text.get_rect()
        textRect.midleft = (0, height - CONSOLE_FONT_SIZE / 2)
        display.blit(text, textRect)

        # 'text console' output for text based aspect
        consolestart = height - ((self.size + 1) * CONSOLE_FONT_SIZE)
        pygame.draw.line(display, BLACK, (0, consolestart), (width, consolestart), CONSOLE_LINE_WIDTH)

class Message:

    """
    Initializes a message with pairs of strings/images
        ie. string1 -> image1 -> string2 -> image2 ... StringN -> ImageN
        can choose ordering, ie. image before message?
    """
    def __init__(self, strings, images=None):
        self._strings = strings
        if images:
            self._images = images
        else:
            self._images = [None]

    """
    Pop's a String and Image pair off of the 'image and string lists
    not really popping, changed to use a index because I was having issues
    with copying the objects, and thought this is faster anyways, more code
    but more eficent
    """
    def pop(self, i):
        if i >= len(self._images):
            # if out of strings and images return (None,None) Tuple
            if i >= len(self._strings):
                return None, None
            # otherwise return (String,None) Tuple
            return self._strings[i], None
        # otherwise we pop off a pair of a string and a image
        return self._strings[i], self._images[i]
