from time import sleep

import TerrainGen
import numpy as np
import pygame
import random

# game dimension (x,y)
from Canvas import Canvas, WHITE, BLACK

# load our canvas
from Console import Console, Message
from NPC.NordicHuman import NordicHuman

canvas = Canvas(800, 800)

crashed = False

def start():

    pygame.display.set_caption('SECRET SAUCE ALPHA')


cur_x = 100
cur_y = 100
x_change = 0
y_change = 0
clock = pygame.time.Clock()

# list of legal keys we can type into console
legal_console_keys = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h,
                      pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p,
                      pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x,
                      pygame.K_y, pygame.K_z]

user_input = ">"
if __name__ == "__main__":

    # start the game
    start()

    # initialize a console
    console = Console(10)

    # generate a nordic npc
    npc = NordicHuman()
    npc._x = 400
    npc._y = 300

    # main loop
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if npc.collided(x, y):
                    # custom message with images
                    # color sprite
                    colorimage = pygame.surfarray.array3d(npc.sprite)
                    colorimage = colorimage[1,:,:]
                    out = pygame.surfarray.make_surface(colorimage)
                    message = Message(["selected", npc.name, "haha funnies", "poopoo","asdfdsafa","asdfdsaasdfdsaasddfsasdfasdfsdfsfdsfsfdsdfsdfsdfsdf"], [npc.sprite, out])
                    console.push(message)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                elif event.key == pygame.K_RIGHT:
                    x_change = 1
                if event.key == pygame.K_UP:
                    y_change = -1
                elif event.key == pygame.K_DOWN:
                    y_change = 1

                # console input
                if event.key == pygame.K_SPACE:
                    user_input += " "
                elif event.key == pygame.K_BACKSPACE:
                    if user_input != ">":
                        user_input = user_input[:len(user_input) - 1]
                elif event.key == pygame.K_RETURN:
                    console.push(user_input[1:])
                    user_input = ">"
                # if it wasn't a movement't option it was textual input for the console
                elif event.key in legal_console_keys:
                    key = pygame.key.name(event.key)

                    user_input += key.upper()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

        cur_x += x_change
        cur_y += y_change
        canvas.update(cur_x, cur_y, user_input, console, npc)

        rand = random.randint(0, 1000)
        if rand == 69:
            console.push("howdy gamer")
            pass

    pygame.quit()
    quit()
