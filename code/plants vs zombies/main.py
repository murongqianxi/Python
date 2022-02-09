import pygame
import sys

pygame.init()

screen_size = (1200, 600)
pygame.display.set_mode(screen_size)
pygame.display.set_caption('plants vs zombies')

def main():
    while True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    main()