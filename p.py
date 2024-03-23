import pygame
pygame.init()
w=pygame.display.set_mode((500, 500))
x=100
y=50
X=250
Y=100
W=50
s=50
d=50
S=50

dr=1
dc=1
dw=1
dh=1
dl=1
de=1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x=x+dr
    if x+100>500:
        dr=-1
    elif x < 0:
        x=dr=+1

    Y=Y+dc
    if Y+50>500:
        dc=-1
    elif Y-50 < 0:
        dc=1

    W=W+dh
    if W+50>500:
        dh=-1
        dw=-1
    elif W-50<0:
        dh=1

    s = s + dh
    if W + 50 > 500:
        dh = -1
        dw = -1
    elif s - 50 < 0:
        dh = 1

    S = S + de * 8
    if S + 51 > 500:
        de = -1
        dl = -1
    elif s - 51 < 0:
        de = 1

    d = d + dl
    if d + 51 > 500:
        de = -1
        dl = -1
    elif d - 51 < 0:
        dl = 1

    w.fill((255, 255,255))
    pygame.draw.rect(w, (255,255, 0), (x, y, 100, 150))
    pygame.draw.circle(w, (255, 0, 0), (X, Y ), 50)
    pygame.draw.circle(w, (255, 0, 255), (W, s), 50)
    pygame.draw.circle(w, (0, 255, 255), (d, S), 51)
    pygame.display.update()
    pygame.time.delay(10)