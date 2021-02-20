import pygame

pygame.init()
size = height, weigh = 800, 600
wjm = pygame.display.set_mode(size)
pygame.display.set_caption('简单的游戏')
wjm.fill((255, 255, 255))
speed = [-2, 1]
tim = pygame.image.load(r'D:\python\刘奕\pygame\sc\tks.png')
wjm.blit(tim, (0, 0))
tgr = tim.get_rect()
pygame.display.flip()

while True:
    # pygame.time.delay(10)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    if tgr.left < 0 or tgr.right > height:
        speed[0] = -speed[0]
    if tgr.top < 0 or tgr.bottom > weigh:
        speed[1] = -speed[1]
    tgr = tgr.move(speed)
    wjm.blit(tim, tgr)
    pygame.display.update()
    wjm.fill((255, 255, 255))



































