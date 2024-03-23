import random

import pygame

pygame.init()

FPS = 600
W, H = 500, 500
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('stary sky')


class Star:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.color = [255, ] * 3

    def draw(self, screen):
        if self.color[0] > 0:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 10)
            self.color = [self.color[0] - 1, ] * 3


stars = []
presed = False
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            presed = True
        if event.type == pygame.MOUSEBUTTONUP:
            presed = False

    if presed:
        stars.append(Star())

    for star in stars:
        star.draw(win)
    if len(stars) > 0:
        if stars[0].color[0] == 0:
            stars.pop(0)

    for _ in range(0, 3, 1):
        pygame.draw.circle(win, (75,) * 3, (random.randint(0, W), random.randint(0, H)), 1)

    pygame.display.update()
    clock.tick(FPS)
