import pygame
pygame.init()
x = 800
y = 600
wjm = pygame.display.set_mode((x, y))
pygame.display.set_caption('简单的模块')
wjm.fill((255, 255, 255))
speed = [0, 0]
nm = False
ts = pygame.image.load(r'D:\python\刘奕\pygame\sc\tks.png')
l = ts.get_rect()
wjm.blit(ts, l)
m = 0
pygame.display.flip()
while True:

    if nm:
        pygame.time.delay(8)
        wjm.fill((255, 255, 255))
        l = l.move(speed)
        wjm.blit(ts, l)
        pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.KEYDOWN:
            if chr(i.key) == 'w':
                nm = True
                speed[1] = -1
                speed[0] = 0
                ts = pygame.image.load(r'D:\python\刘奕\pygame\sc\tks.png')
            if chr(i.key) == 's':
                nm = True
                speed[0] = 0
                speed[1] = 1
                ts = pygame.image.load(r'D:\python\刘奕\pygame\sc\tkx.png')
            if chr(i.key) == 'd':
                nm = True
                speed[1] = 0
                speed[0] = 1
                ts = pygame.image.load(r'D:\python\刘奕\pygame\sc\tky.png')

            if chr(i.key) == 'a':
                nm = True
                speed[1] = 0
                speed[0] = -1
                ts = pygame.image.load(r'D:\python\刘奕\pygame\sc\tkz.png')

        if i.type == pygame.KEYUP:
            nm = False
















































