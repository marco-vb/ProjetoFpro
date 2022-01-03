import pygame, os
from constants import *

SPACESHIP_IMAGE = pygame.image.load(os.path.join('Resources', "spaceship.png"))
SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (SPWID, SPHEI))
SPACE_IMAGE = pygame.image.load(os.path.join('Resources', "space.png"))
SPACE = pygame.transform.scale(SPACE_IMAGE, (WID, HEI))
