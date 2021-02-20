import pygame
# 初始化
pygame.init()
# 设置大小
wjm =pygame.display.set_mode((800, 600))

# 设置名称
pygame.display.set_caption('简单的游戏')

# 渲染背景颜色
wjm.fill((198,200,199))

# 往主界面上贴图片
# 'photos/荒岛漂流者.jpg是图片
photo = pygame.image.load(r'D:\python\刘奕\pygame\sc\荒岛漂流者.jpg')

# 渲染图片
# blit(渲染的的图片，坐标)
wjm.blit(photo, (0, 0))

# 操作图片
# 1获得图片大小
w, h = photo.get_size()
wjm.blit(photo, (800 - w, 600 - h))

# 2旋转图片/缩放
# （1）scale(缩放对象，目标大小)
# （2）rotozoom(缩放/或者旋转对象，旋转角度，缩放比例)
sf = pygame.transform.scale(photo, (100, 50))   # 这种方法可能照片会形变
wjm.blit(sf,(700, 0))

nb = pygame.transform.rotozoom(photo, 180, 2)
wjm.blit(nb, (0, 150))
# 渲染完之后必须刷新，否则不显示图
pygame.display.flip()   #第一次刷新屏幕必须用这个
# pygame.display.update()         第二次刷新或第二次以上用这个刷新界面
# 循环游戏
while True:
    for i in pygame.event.get():
        # 检测是否退出
        if i.type == pygame.QUIT:
            # 退出
            exit()











