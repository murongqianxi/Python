import pygame


class A:
    mp = 0
    mvp = True

    def __init__(self, abc):
        pygame.draw.rect(abc, (255, 0, 0), (350, 400, 100, 50))
        pygame.draw.rect(abc, (0, 255, 0), (350, 500, 100, 50))

        t = pygame.font.Font(r'D:\python\刘明帅\pygame\飞机大战2\font\font.ttf', 20)
        self.n = t.render('start game', True, (255, 255, 255))
        v, b = self.n.get_size()
        p = pygame.font.Font(r'D:\python\刘明帅\pygame\飞机大战2\font\font.ttf', 30)
        self.c = p.render('quit', True, (255, 255, 255))
        x, y = self.c.get_size()
        self.g = 350 + 100/2 - v/2
        self.m = 400 + 50/2 - b/2
        self.j= 350 + 100/2 - x/2
        self.k = 500 + 50/2 - y/2

        abc.blit(self.n, (int(self.g), int(self.m)))
        abc.blit(self.c, (int(self.j), int(self.k)))
        self.ab = abc

    def jc(self, a):
        q1, w2 = a.pos
        if 350 <= q1 <= 450 and 400 <= w2 <= 450 and self.mvp:
            pygame.draw.rect(self.ab, (200, 200, 200), (350, 400, 100, 50))
            self.ab.blit(self.n, (int(self.g), int(self.m)))
            pygame.display.update()
            self.mp += 1
            pygame.time.delay(300)
        if 350 <= q1 <= 450 and 500 <= w2 <= 550 and self.mvp:
            pygame.draw.rect(self.ab, (200, 200, 200), (350, 500, 100, 50))
            self.ab.blit(self.c, (int(self.j), int(self.k)))
            pygame.display.update()
            exit()
        '''
    def ku(self):
        if self.mvp:
            pygame.draw.rect(self.ab, (255, 0, 0), (350, 400, 100, 50))
            self.ab.blit(self.n, (int(self.g), int(self.m)))
            pygame.display.update()
            
            pygame.draw.rect(self.ab, (0, 255, 0), (350, 500, 100, 50))
            self.ab.blit(self.c, (int(self.j), int(self.k)))
            
        '''
    def mcp(self):
        if self.mp == 1:
            self.mvp = False


class Game:
    def __init__(self):
        self.s, self.u, self.nm = (0, 0, 0)
        self.a, self.b, self.c = (0, 10, 590)

    def ddc(self, cd):
        while self.a != 100:
            self.a += 1
            cd.fill((255, 255, 255))
            self.b += self.s
            self.c += self.u
            pygame.draw.circle(cd, (0, 0, 0), (self.b, self.c), 10)
            if self.b == 790:
                exit()
            if self.b < 10:
                self.b = 10
            pygame.display.update()
            if self.s == 0 and self.u == -1 and self.a == 99:
                while self.nm != 98:
                    # b += 1
                    self.nm += 1
                    cd.fill((255, 255, 255))
                    self.s, self.u = (0, 1)
                    self.b += self.s
                    self.c += self.u
                    pygame.draw.circle(cd, (0, 0, 0), (self.b, self.c), 10)
                    pygame.display.update()
                self.nm = 0

    def dc(self, av):
        if av.type == pygame.KEYDOWN:
            if chr(av.key) == 'w':
                self.s = 0
                self.u = -1
                self.a = 0
            if chr(av.key) == 'a':
                self.s = -1
                self.u = 0
                self.a = 0
            if chr(av.key) == 'd':
                self.s = 1
                self.u = 0
                self.a = 0
                '''
            if chr(av.key) == 's':
                self.s = 0
                self.u = 1
                self.a = 0
            '''
















