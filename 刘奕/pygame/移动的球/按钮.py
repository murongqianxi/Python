import pygame


'''
# 1画直线
# line(画在哪里，线的颜色，线的起点，线的终点，线的宽度（默认是1))
pygame.draw.line(wjm, (255, 0, 0), (0, 0), (100, 100), 3)


# 2画图形
# lines(画在哪里，线的颜色, 是否闭合，多个点的坐标（列表）,线的宽度（默认是1))
n = [(0, 100),(100, 100), (250, 0)]
pygame.draw.lines(wjm, (0, 255, 255), True, n, 5)

# 3画圆
# circle(画在哪里，线的颜色，圆心坐标，半径长度，线宽(默认是0，线宽是0就是填充)
pygame.draw.circle(wjm, (0, 0, 255), (400, 300), 200,1)

# 4画矩形
# rect(画在哪里，线的颜色，（x,y,长,宽），线宽(默认是0，线宽是0就是填充))
pygame.draw.rect(wjm, (34, 24,48), (200, 200, 100, 200), 3)

# 5画椭圆
# ellipse(画在哪里，线的颜色，（坐标（x，y），长,宽），线宽(默认是0，线宽是0就是填充))
pygame.draw.ellipse(wjm, (34, 24,48), (200, 200, 100, 200), 1)

# 6画弧线
# arc(画在哪里，线的颜色，(坐标（x，y）,长,宽)，起始弧度，终止弧度，线长)
pygame.draw.arc(wjm, (34, 24,48), (200, 250, 100, 100), 0, pi * 2, 1)
pygame.display.flip()
'''


pygame.init()
wjm = pygame.display.set_mode((800, 600))
pygame.display.set_caption('简单的游戏')
wjm.fill((255, 255, 255))
q, w, e = 100, 200, 50
pygame.draw.rect(wjm, (255, 0, 0), (q, q, q, e))
pygame.draw.rect(wjm, (0, 255, 0), (q, w, q, e))
t = pygame.font.Font(r'D:\python\刘明帅\pygame\飞机大战2\font\font.ttf', 20)
n = t.render('start game', True, (255, 255, 255))
v, b = n.get_size()
g = q + q/2 - v/2
m = q + e/2 - b/2
wjm.blit(n, (int(g), int(m)))
p = pygame.font.Font(r'D:\python\刘明帅\pygame\飞机大战2\font\font.ttf', 30)
c = p.render('quit', True, (255, 255, 255))
x, y = c.get_size()
j = q + q/2 - x/2
k = w + e/2 - y/2
wjm.blit(c, (int(j), int(k)))
pygame.display.flip()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            mx, my = i.pos
            if q <= mx <= q + q and q <= my <= q + e:
                pygame.draw.rect(wjm, (200, 200, 200), (q, q, q, e))
                wjm.blit(n, (int(g), int(m)))
                pygame.display.update()
            if q <= mx <= q + q and w <= my <= w + e:
                pygame.draw.rect(wjm, (200, 200, 200), (q, w, q, e))
                wjm.blit(c, (int(j), int(k)))
                pygame.display.update()
                exit()
        if i.type == pygame.MOUSEBUTTONUP:
            pygame.draw.rect(wjm, (255, 0, 0), (q, q, q, e))
            wjm.blit(n, (int(g), int(m)))
            pygame.draw.rect(wjm, (0, 255, 0), (q, w, q, e))
            wjm.blit(c, (int(j), int(k)))
            pygame.display.update()


































































































