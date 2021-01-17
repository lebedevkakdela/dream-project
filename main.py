import pygame

# уровни в списках
level1 = [[11, 0, 0, 4, 5, 8, 8, 8, 5, 5],
          [2, 3, 0, 7, 9, 0, 0, 10, 4, 5],
          [5, 6, 0, 0, 10, 0, 0, 0, 4, 5],
          [5, 6, 0, 0, 0, 0, 0, 0, 7, 8],
          [5, 5, 2, 3, 0, 0, 0, 0, 0, 10],
          [5, 5, 5, 6, 0, 1, 2, 3, 0, 10],
          [5, 5, 5, 6, 0, 4, 5, 6, 0, 10],
          [5, 5, 5, 9, 0, 4, 5, 6, 0, 10],
          [5, 5, 6, 10, 0, 4, 5, 6, 0, 10],
          [5, 5, 5, 2, 2, 5, 5, 5, 3, 10]]

level2 = [[11, 0, 0, 0, 0, 5, 0, 0, 0, 10],
          [3, 0, 0, 0, 0, 5, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 5, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 5, 0, 0, 0, 10],
          [6, 0, 10, 0, 0, 5, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 8, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 0, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 2, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 5, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 5, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 5, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 5, 0, 0, 0, 10],
          [6, 0, 0, 0, 0, 5, 0, 0, 0, 10]]

level3 = [[11, 0, 4, 5, 8, 5, 5, 5, 5, 5],
          [3, 0, 7, 9, 10, 7, 5, 5, 5, 5],
          [6, 0, 0, 0, 10, 0, 7, 5, 5, 5],
          [5, 3, 0, 0, 0, 0, 0, 7, 5, 5],
          [5, 5, 2, 3, 0, 0, 0, 0, 4, 5],
          [5, 8, 5, 6, 0, 1, 3, 0, 4, 5],
          [6, 10, 4, 6, 0, 4, 6, 0, 7, 8],
          [6, 0, 7, 9, 0, 4, 6, 10, 0, 10],
          [6, 0, 0, 10, 0, 4, 5, 3, 0, 0],
          [5, 2, 2, 2, 2, 5, 5, 5, 3, 10]]


class Board:
    # создание поля
    def __init__(self, w, h, level, a):
        # переменные
        self.record = None
        self.a = a
        self.count = 0
        self.cursor_x = 0
        self.cursor_y = 0
        self.score = 0
        self.time = 0
        self.records = []
        self.width = w
        self.height = h
        # значения по умолчанию
        self.board = [[0] * w for _ in range(h)]
        # задание уровней
        if level == 1:
            self.board = level1
        if level == 2:
            self.board = level2
        if level == 3:
            self.board = level3
        self.left = 0
        self.top = 0
        self.cell_size = 50

    def render(self, screen):
        # отрисовка уровня
        colors = {1: pygame.image.load('img/luc.jpg').convert(),
                  2: pygame.image.load('img/u.jpg').convert(),
                  3: pygame.image.load('img/ruc.jpg').convert(),
                  4: pygame.image.load('img/l.jpg').convert(),
                  5: pygame.image.load('img/wall.jpg').convert(),
                  6: pygame.image.load('img/r.jpg').convert(),
                  7: pygame.image.load('img/ldc.jpg').convert(),
                  8: pygame.image.load('img/d.jpg').convert(),
                  9: pygame.image.load('img/rdc.jpg').convert(),
                  10: pygame.image.load('img/t.jpg').convert(),
                  11: pygame.image.load('img/c.jpg').convert(),
                  0: pygame.image.load('img/g.jpg').convert()
                  }
        for x in range(self.width):
            for y in range(self.height):
                screen.blit(colors[self.board[y][x]],
                            (x * self.cell_size + self.left, y * self.cell_size + self.top,
                             self.cell_size - 1,
                             self.cell_size - 1))
                pygame.draw.rect(screen, pygame.Color(1, 50, 32), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top,
                    self.cell_size - 1,
                    self.cell_size - 1), 2)

    def board_chek(self):
        # проверка не закончились ли яблоки
        kol = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.board[x][y] == 10:
                    kol += 1
        if kol == 0:
            return False
        else:
            return True

    def get_click(self, code):
        # изменения уровня и перемещение
        if code == 0 and self.cursor_y != 0 and (
                self.board[self.cursor_y - 1][self.cursor_x] == 0 or self.board[self.cursor_y - 1]
                [self.cursor_x] == 10):
            if self.board[self.cursor_y - 1][self.cursor_x] == 10:
                self.count += 100
                self.a.play()
            self.board[self.cursor_y][self.cursor_x] = 0
            self.board[self.cursor_y - 1][self.cursor_x] = 11
            self.cursor_y -= 1

        elif code == 1 and self.cursor_y != 9 and (
                self.board[self.cursor_y + 1][self.cursor_x] == 0 or self.board[self.cursor_y + 1]
                [self.cursor_x] == 10):
            if self.board[self.cursor_y + 1][self.cursor_x] == 10:
                self.count += 100
                self.a.play()
            self.board[self.cursor_y][self.cursor_x] = 0
            self.board[self.cursor_y + 1][self.cursor_x] = 11
            self.cursor_y += 1

        elif code == 2 and self.cursor_x != 0 and (
                self.board[self.cursor_y][self.cursor_x - 1] == 0 or self.board[self.cursor_y]
                [self.cursor_x - 1] == 10):
            if self.board[self.cursor_y][self.cursor_x - 1] == 10:
                self.count += 100
                self.a.play()
            self.board[self.cursor_y][self.cursor_x] = 0
            self.board[self.cursor_y][self.cursor_x - 1] = 11
            self.cursor_x -= 1

        elif code == 3 and self.cursor_x != 9 and (
                self.board[self.cursor_y][self.cursor_x + 1] == 0 or self.board[self.cursor_y]
                [self.cursor_x + 1] == 10):
            if self.board[self.cursor_y][self.cursor_x + 1] == 10:
                self.count += 100
                self.a.play()
            self.board[self.cursor_y][self.cursor_x] = 0
            self.board[self.cursor_y][self.cursor_x + 1] = 11
            self.cursor_x += 1

    def record_update(self):
        # перезапись рекордов
        # считывание рекордов
        f = open('records.txt', mode='r+', encoding='utf8')
        self.records = [int(x) for x in f.read().split(', ')]
        self.records.append(self.time // 100)
        self.records.sort()
        a = []
        a.extend(self.records)
        self.records.clear()
        self.records = [str(x) for x in a]
        f.close()
        # перезапись рекордов
        self.record = ', '.join(self.records[:10])
        f1 = open('records.txt', mode='w+', encoding='utf8')
        f1.write(self.record)
        f1.close()


def menu(coords):
    # проверка нажатий мыши на кнопки выбора уровней
    x, y = coords
    if (240 < y < 290) and (282 < x < 332):
        return 1, False
    elif (240 < y < 290) and (332 < x < 382):
        return 2, False
    elif (240 < y < 290) and (382 < x < 432):
        return 3, False
    else:
        return 1, True


def main():
    # создание окна
    pygame.init()
    size = 800, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Farmer')
    working = True  # working(в переводе: 'работа') - переменная отвечает за
    running = True
    level = 0
    while running:
        # кадры пока пользователь выбирает уровень
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                level, running = menu(event.pos)
            if event.type == pygame.QUIT:
                running = False
                working = False
        screen.fill((128, 217, 255))
        font = pygame.font.Font(None, 50)
        text = font.render("CHOOSE LEVEL:", True, (228, 217, 123))
        text1 = font.render('1   2    3 ', True, (228, 217, 123))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (282, 240, 50, 50), 2)
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (332, 240, 50, 50), 2)
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (382, 240, 50, 50), 2)
        screen.blit(text, (250, 200))
        screen.blit(text1, (300, 250))
        pygame.display.flip()
    # создание игрового поля
    board = Board(10, 10, level, pygame.mixer.Sound('img/t.mp3'))
    clock = pygame.time.Clock()
    t = 0
    running = True
    # отрисовка игрового поля
    while running and working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                working = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    board.get_click(0)
                elif event.key == pygame.K_DOWN:
                    board.get_click(1)
                elif event.key == pygame.K_RIGHT:
                    board.get_click(3)
                elif event.key == pygame.K_LEFT:
                    board.get_click(2)
        screen.fill((128, 217, 255))
        board.render(screen)
        font = pygame.font.Font(None, 50)
        text = font.render("Score:" + str(board.count), True, (228, 217, 123))
        text1 = font.render('Time: ' + str(t // 100), True, (228, 217, 123))
        screen.blit(text, (500, 100))
        screen.blit(text1, (500, 130))
        pygame.display.flip()
        clock.tick(60)
        t += 1
        board.time = t
        running = board.board_chek()
    board.record_update()
    screen.fill((128, 217, 255))
    running = True
    # вывод последнего экрана
    while running and working:
        screen.fill((128, 217, 255))
        font = pygame.font.Font(None, 50)
        text = font.render("Score:" + str(board.count), True, (228, 217, 123))
        text1 = font.render('Time: ' + str(t // 100), True, (228, 217, 123))
        text2 = font.render('Records: ' + board.record, True, (228, 217, 123))
        screen.blit(text, (250, 100))
        screen.blit(text1, (250, 130))
        screen.blit(text2, (100, 160))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                working = False
            if event.type == pygame.QUIT:
                running = False
                working = False

    pygame.quit()


if __name__ == '__main__':
    main()
