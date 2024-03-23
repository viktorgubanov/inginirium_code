import pygame as pg

BLACK = (0,) * 3
GRAY = (100,) * 3
WHITE = (255,) * 3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

CROSS = '#046582'
CIRCLE = '#e4bad4'

pg.init()

FPS = 30
W, H = (600,) * 2

win = pg.display.set_mode((W, H))
pg.display.set_caption('TIC')


def draw_circle(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    pg.draw.circle(sc, CIRCLE, (x, y), (size - 3) // 2, 3)


def draw_cross(sc, x, y, size):
    x = x * size + 3
    y = y * size + 3
    pg.draw.line(sc, CROSS, (x, y), (x + size - 3, y + size - 3), 3)
    pg.draw.line(sc, CROSS, (x + size - 6, y), (x, y + size - 6), 3)


def is_end(board):
    check_i_line = lambda x, i: x[i][0] == x[i][1] == x[i][2] != 0
    check_i_col = lambda x, i: x[0][i] == x[1][i] == x[2][i] != 0
    check_main_diag = lambda x: x[0][0] == x[1][1] == x[2][2] != 0
    check_secondary_diag = lambda x: x[2][0] == x[1][1] == x[0][2] != 0

    for i in range(3):
        if check_i_col(board, i):
            return 'col', i
        if check_i_line(board, i):
            return 'line', i
    if check_main_diag(board):
        return 'diag', 1
    if check_secondary_diag(board):
        return 'diag', 2
    return None


class Board:
    def __init__(self, w, h, size):
        self.W, self.H = w, h
        self.size = size
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.move = 1

    def check_end(self):
        is_end_info = is_end(self.board)
        shift = self.W // 10
        if is_end_info is not None:
            type_end = is_end_info[0]
            number = is_end_info[1]
            if type_end == 'col':
                x0, y0 = (number + .5) * self.size, shift
                x1, y1 = x0, self.H - shift
            elif type_end == 'line':
                x0, y0 = shift, (number + .5) * self.size
                x1, y1 = self.W - shift, y0
            elif type_end == 'diag':
                if number == 1:
                    x0, y0 = shift, shift
                    x1, y1 = self.W - shift, self.H - shift
                elif number == 2:
                    x0, y0 = shift,self.H - shift
                    x1, y1 = self.W - shift, shift
            pg.draw.line(win, RED, (x0, y0), (x1, y1), 10)
            pg.display.update()
            pg.time.delay(3000)
            return True
        else:
            return False

    def click(self, mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move

    def render(self, screen):
        pg.draw.line(screen, GRAY, (0, 200), (self.W, 200))
        pg.draw.line(screen, GRAY, (0, 400), (self.W, 400))
        pg.draw.line(screen, GRAY, (200, 0), (200, self.H))
        pg.draw.line(screen, GRAY, (400, 0), (400, self.H))
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    draw_cross(screen, x, y, self.size)
                elif self.board[y][x] == -1:
                    draw_circle(screen, x, y, self.size)


board = Board(W, H, 200)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)
    win.fill(WHITE)
    board.render(win)
    pg.display.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE] or board.check_end():
        pg.quit()
        exit()
