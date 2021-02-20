import pygame
import settings
import sys
from pygame.locals import *

settings = settings.Settings()

pygame.init()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('恐龙快跑')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()