import pygame
pygame.init()
s=int(input())
d=int(input())
win=pygame.display.set_mode((s, d))
win.fill((0,0,0))
pygame.draw.line(win, (225,225,225), (s,d),(0,0),5)
pygame.draw.line(win, (225,225,225), (0,d),(s,0),5)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
