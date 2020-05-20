# credit to https://medium.com/@yvanscher/playing-with-perlin-noise-generating-realistic-archipelagos-b59f004d8401
# <3

import noise
import numpy as np
import Game
import random


scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]
snow = [255, 250, 250]
mountain = [139, 137, 137]

# testing
crimson = [220, 20, 60]
CRIMSON_BIOMES = 3

import math

# scans in N,W,E,S for initializing Biome by anything that isn't water
def biome_scan(biomeMap, terrain, x, y):

    while True:
        # base case
        if np.array_equal(terrain[x][y], blue):
            return
        else:
            # set biome here
            biomeMap[(x, y)] = True
            terrain[x][y] = crimson

            # recurse
            biome_scan(biomeMap, terrain, x+1, y)
            biome_scan(biomeMap, terrain, x, y+1)
            biome_scan(biomeMap, terrain, x, y-1)
            biome_scan(biomeMap, terrain, x-1, y)

#
#
# def gen():
#
#     terrain = np.zeros(shape+(3,))
#
#     # terrain generation without biomes
#     for i in range(shape[0]):
#         for j in range(shape[1]):
#             x = noise.pnoise2(i / scale,
#                                         j / scale,
#                                         octaves=octaves,
#                                         persistence=persistence,
#                                         lacunarity=lacunarity,
#                                         repeatx=1024,
#                                         repeaty=1024,
#                                         base=5)
#
#             if x < -0.05:
#                 terrain[i][j] = blue
#             elif x < 0:
#                 terrain[i][j] = beach
#             elif x < .2:
#                 terrain[i][j] = green
#             elif x < .4:
#                 terrain[i][j] = mountain
#             elif x < .5:
#                 terrain[i][j] = snow
#     biomeMap = {}
#
#     # biome generation
#     for x in range(shape[0]):
#         for y in range(shape[1]):
#             if (x,y) in biomeMap:
#                 continue
#             # water biome
#             if np.array_equal(terrain[x][y], blue):
#                 pass
#             # mark this area as a biome
#             else:
#                 pass
#                 # scan in all four directions for anything that isn't water
#                 # biome_scan(biomeMap, terrain, x, y)
#                 # choose a random biome? or base it off of distance from start area maybe?


    # this code might be useful for ore or material generation, what materials are present where?

    # # go over and initialize biomes
    # for i in range(CRIMSON_BIOMES):
    #     epicenter_x = random.randint(0, Game.GAME_X)
    #     epicenter_y = random.randint(0, Game.GAME_Y)
    #
    #     for i in range(epicenter_x-320, epicenter_x+320):
    #
    #         if i < 0 or i >= Game.GAME_X:
    #             continue
    #
    #         for j in range(epicenter_y-320, epicenter_y+320):
    #             # chance_green = 0.0
    #
    #             if j < 0 or j >= Game.GAME_Y:
    #                 continue
    #
    #             if not (j < epicenter_y - 280 or j > epicenter_y + 280 or i > epicenter_x + 280 or i < epicenter_x - 280):
    #
    #                 zzz = noise.pnoise2(i / scale,
    #                                   j / scale,
    #                                   octaves=16,
    #                                   persistence=.3,
    #                                   lacunarity=3.0,
    #                                   repeatx=5,
    #                                   repeaty=5,
    #                                   base=10)
    #
    #                 if zzz < -.05 and np.array_equal(terrain[i][j], green):
    #                     terrain[i][j] = crimson


    # find center of each 'island'
    # scan in x till height decreases then set x rand between start and when decreased
    # same with y
    # set x and y range as biome
    # we scan from water to water
    # if not starting on water, just scan from start to water

    return terrain

