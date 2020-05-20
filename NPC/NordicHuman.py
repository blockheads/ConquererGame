import codecs
import sys

import Sprites
from NPC.Npc import Npc, DATA_PATH
from util import Reader


class NordicHuman(Npc):

    def __init__(self):
        super().__init__(self.genName(),Sprites.NPC_H)

    """
    Generates a nordic human name   
    """
    def genName(self):
        # ensure proper encoding

        # read file, needs to be encoded by utf_8
        f = codecs.open(DATA_PATH + "NORDIC_H.txt", encoding='utf_8')
        firstName = Reader.random_line(f)
        firstName = firstName.rstrip()

        f = codecs.open(DATA_PATH + "NORDIC_H.txt", encoding='utf_8')
        lastName = Reader.random_line(f)
        lastName = lastName.rstrip()

        return firstName + " " + lastName


if __name__ == '__main__':
    # if running from this directory we start at data rather than root
    DATA_PATH = "data/"
    nordichuman = NordicHuman()
    print(nordichuman.name)
