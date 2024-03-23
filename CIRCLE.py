import pygame

pygame.init()
w = pygame.display.set_mode((500, 500))


class Circle:
    def __init__(self, x, y, color, rad):
        self.x = x
        self.y = y
        self.color = color
        self.rad = rad
        self.sp = 30
        self.s_jmp = False

    def move(self):
        if self.s_jmp:
            if self.sp >= -30:
                self.y -= self.sp
                self.sp -= 3
            else:
                self.s_jmp = False
                self.sp = 30
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3

        if keys[pygame.K_UP]:
            self.y -= 3
        elif keys[pygame.K_DOWN]:
            self.y += 3

        if keys[pygame.K_SPACE]:
            self.s_jmp = True

    def draw(self, root):
        pygame.draw.circle(root, self.color, (self.x, self.y), self.rad)


c = Circle(3, 5, (245, 200, 30), 57)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    c.move()

    w.fill((255, 255, 255))
    c.draw(w)
    pygame.display.update()
    pygame.time.delay(15)
