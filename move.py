import pygame

pygame.init()
w = pygame.display.set_mode((500, 500))
x = 100
y = 50

re=255
ye=255
bl=255

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3

    elif keys[pygame.K_UP]:
        y -= 3
    elif keys[pygame.K_DOWN]:
        y += 3

    else:

        if x > 250:
            x = x - 1
        elif x<250:
            x=x+1
        else:
            x = 250
        if y > 250:
            y = y - 1
        elif y<250:
            y=y+1
        else:
            y = 250
    if x < 100 and x > 400:
        color=re



    w.fill((255, 255, 255))
    pygame.draw.circle(w, (0, 255, 255), (x, y), 50)
    pygame.display.update()
    pygame.time.delay(10)
