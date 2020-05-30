from time import sleep

import numpy as np
import pygame
import random

# game dimension (x,y)
from Canvas import Canvas

# load our canvas
import Console
from NPC.NordicHuman import NordicHuman
import InputHandler

canvas = Canvas(800, 800)

crashed = False

def start():

    pygame.display.set_caption('SECRET SAUCE ALPHA')


cur_x = 100
cur_y = 100
x_change = 0
y_change = 0
clock = pygame.time.Clock()

user_input = ">"

inputHandler = InputHandler.Handler()

if __name__ == "__main__":

    # start the game
    start()

    # generate a nordic npc
    npc = NordicHuman()
    npc._x = 400
    npc._y = 300

    sayMode = False

    # main loop
    while not crashed:
        for event in pygame.event.get():
            inputHandler.handle(event, npc, canvas)

        cur_x += x_change
        cur_y += y_change
        canvas.update(cur_x, cur_y, inputHandler, npc)

        rand = random.randint(0, 1000)
        if rand == 69:
            InputHandler.console.push("howdy gamer")
            pass

    pygame.quit()
    quit()
