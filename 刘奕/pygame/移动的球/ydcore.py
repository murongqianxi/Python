import pygame
import ydmod
pygame.init()


class B(ydmod.A):
    pass


class G(ydmod.Game):
    pass


wjm = pygame.display.set_mode((800, 600))
pygame.display.set_caption('简单的游戏')
wjm.fill((255, 255, 255))
l1 = B(wjm)
k1 = G()
nnb = 0
pygame.display.flip()

while True:
    if l1.mp == 1:
        k1.ddc(wjm)
        nnb = 1
    for i1 in pygame.event.get():
        if i1.type == pygame.QUIT:
            exit()
        if i1.type == pygame.MOUSEBUTTONDOWN:
            l1.jc(i1)
            l1.mcp()

        if i1.type == pygame.MOUSEBUTTONUP:
            pass
        if i1.type == pygame.KEYDOWN:
            if nnb == 1:
                if chr(i1.key) == 'w':
                    k1.s = 0
                    k1.u = -1
                    k1.a = 0
                if chr(i1.key) == 'a':
                    k1.s = -1
                    k1.u = 0
                    k1.a = 0
                if chr(i1.key) == 'd':
                    k1.s = 1
                    k1.u = 0
                    k1.a = 0


