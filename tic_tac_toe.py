import pygame as pg
import sys
import os
pg.init()
pg.font.init()


WIDTH, HEIGHT = 600, 600
IMAGE_WIDTH, IMAGE_HEIGHT = 190, 190
LINE_WIDTH = 7

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Tic Tac Toe!')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 165

CIRCLE_IMAGE = pg.image.load(os.path.join('assets', 'circle.png'))
CIRCLE = pg.transform.scale(CIRCLE_IMAGE, (IMAGE_WIDTH, IMAGE_HEIGHT))
CROSS_IMAGE = pg.image.load(os.path.join('assets', 'cross.png'))
CROSS = pg.transform.scale(CROSS_IMAGE, (IMAGE_WIDTH, IMAGE_HEIGHT))

FONT = pg.font.SysFont('comicsans', 100)
TURN_FONT = pg.font.SysFont('comicsans', 20)


def draw_window():
    WIN.fill(WHITE)
    pg.display.update()
    

def draw_cross(x, y):
    WIN.blit(CROSS, (x, y))
    pg.display.update()


def draw_circle(x, y):
    WIN.blit(CIRCLE, (x, y))
    pg.display.update()


def draw_grid():
    block_size = 200     # Set the size of the grid block
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pg.Rect(x, y, block_size, block_size)
            pg.draw.rect(WIN, BLACK, rect, 1)


def check_win():

    global winner
    winner = ''

    for row in range(3):
        if BOARD[row][0] == BOARD[row][1] == BOARD[row][2] and BOARD[row][0] != 0:
            winner = BOARD[row][0]
            pg.draw.line(WIN, BLACK,
                         (0, (row + 1) * HEIGHT / 3 - HEIGHT / 6),
                         (WIDTH, (row + 1) * HEIGHT / 3 - HEIGHT / 6), LINE_WIDTH)
            break

    for column in range(3):
        if BOARD[0][column] == BOARD[1][column] == BOARD[2][column] and BOARD[0][column] != 0:
            winner = BOARD[0][column]
            pg.draw.line(WIN, BLACK, ((column + 1) * WIDTH / 3 - WIDTH / 6, 0),
                         ((column + 1) * WIDTH / 3 - WIDTH / 6, HEIGHT), LINE_WIDTH)
            break

    if (BOARD[0][0] == BOARD[1][1] == BOARD[2][2]) and (BOARD[0][0] != 0):
        # game won diagonally left to right
        winner = BOARD[0][0]
        pg.draw.line(WIN, BLACK, (0, 0), (WIDTH, HEIGHT), LINE_WIDTH)

    if (BOARD[0][2] == BOARD[1][1] == BOARD[2][0]) and (BOARD[0][2] != 0):
        # game won diagonally right to left
        winner = BOARD[0][2]
        pg.draw.line(WIN, BLACK, (WIDTH, 0), (0, HEIGHT), LINE_WIDTH)

    if all([all(row) for row in BOARD]) and winner == '':
        winner = 'Tie!'

    return winner


def delay():
    pg.display.update()
    pg.time.delay(5000)
    main()


def draw_turn(text):
    text_blit = TURN_FONT.render(text, True, BLACK)
    WIN.blit(text_blit, (WIDTH//2 - text_blit.get_width()//2, 0))
    pg.display.update()


def cover_turn():
    pg.draw.rect(WIN, WHITE, (210, 5, 150, 20))


def main():
    clock = pg.time.Clock()
    count = 0

    turn = ''

    draw_window()
    draw_grid()

    global BOARD
    BOARD = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    running = True
    draw_turn("X's turn")
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print('Thanks for playing!')
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if count % 2 == 0:
                    turn = "O's turn"
                    cover_turn()
                    draw_turn(turn)
                    count += 1
                    x_axis, y_axis = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
                    if x_axis < WIDTH/3:
                        if y_axis < WIDTH/3 and BOARD[0][0] == 0:
                            draw_cross(5, 5)
                            BOARD[0][0] = 'X'
                        elif WIDTH/3 < y_axis < WIDTH * (2/3) and BOARD[1][0] == 0:
                            draw_cross(5, 205)
                            BOARD[1][0] = 'X'
                        elif WIDTH * (2/3) < y_axis < WIDTH and BOARD[2][0] == 0:
                            draw_cross(5, 405)
                            BOARD[2][0] = 'X'
                    if WIDTH/3 < x_axis < WIDTH * (2/3):
                        if y_axis < WIDTH/3 and BOARD[0][1] == 0:
                            draw_cross(205, 5)
                            BOARD[0][1] = 'X'
                            draw_turn(turn)
                        elif WIDTH/3 < y_axis < WIDTH * (2/3) and BOARD[1][1] == 0:
                            draw_cross(205, 205)
                            BOARD[1][1] = 'X'
                        elif WIDTH * (2/3) < y_axis < WIDTH and BOARD[2][1] == 0:
                            draw_cross(205, 405)
                            BOARD[2][1] = 'X'
                    if WIDTH * (2/3) < x_axis < WIDTH:
                        if y_axis < WIDTH/3 and BOARD[0][2] == 0:
                            draw_cross(405, 5)
                            BOARD[0][2] = 'X'
                        elif WIDTH/3 < y_axis < WIDTH * (2/3) and BOARD[1][2] == 0:
                            draw_cross(405, 205)
                            BOARD[1][2] = 'X'
                        elif WIDTH * (2/3) < y_axis < WIDTH and BOARD[2][2] == 0:
                            draw_cross(405, 405)
                            BOARD[2][2] = 'X'
                elif count % 2 != 0:
                    count += 1
                    turn = "X's turn"
                    cover_turn()
                    draw_turn(turn)
                    x_axis, y_axis = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
                    if x_axis < WIDTH/3:
                        if y_axis < WIDTH/3 and BOARD[0][0] == 0:
                            draw_circle(5, 5)
                            BOARD[0][0] = 'O'
                        elif WIDTH/3 < y_axis < WIDTH * (2/3) and BOARD[1][0] == 0:
                            draw_circle(5, 205)
                            BOARD[1][0] = 'O'
                        elif WIDTH * (2/3) < y_axis < WIDTH and BOARD[2][0] == 0:
                            draw_circle(5, 405)
                            BOARD[2][0] = 'O'
                    if WIDTH/3 < x_axis < WIDTH * (2/3):
                        if y_axis < WIDTH/3 and BOARD[0][1] == 0:
                            draw_circle(205, 5)
                            BOARD[0][1] = 'O'
                            draw_turn(turn)
                        elif WIDTH/3 < y_axis < WIDTH * (2/3) and BOARD[1][1] == 0:
                            draw_circle(205, 205)
                            BOARD[1][1] = 'O'
                        elif WIDTH * (2/3) < y_axis < WIDTH and BOARD[2][1] == 0:
                            draw_circle(205, 405)
                            BOARD[2][1] = 'O'
                    if WIDTH * (2/3) < x_axis < WIDTH:
                        if y_axis < WIDTH/3 and BOARD[0][2] == 0:
                            draw_circle(405, 5)
                            BOARD[0][2] = 'O'
                        elif WIDTH/3 < y_axis < WIDTH * (2/3) and BOARD[1][2] == 0:
                            draw_circle(405, 205)
                            BOARD[1][2] = 'O'
                        elif WIDTH * (2/3) < y_axis < WIDTH and BOARD[2][2] == 0:
                            draw_circle(405, 405)
                            BOARD[2][2] = 'O'
                check_win()

                if winner == 'Tie!':
                    winner_text = FONT.render(winner, True, BLACK)
                    WIN.blit(winner_text, (WIDTH//2 - winner_text.get_width()//2,
                                           HEIGHT//2 - winner_text.get_height()//2))
                    delay()
                    main()

                elif winner == 'X':
                    text = f'{winner} wins!'
                    winner_text = FONT.render(text, True, BLACK)
                    WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2,
                                           HEIGHT // 2 - winner_text.get_height() // 2))
                    delay()
                    main()

                elif winner == 'O':
                    text = f'{winner} wins!'
                    winner_text = FONT.render(text, True, BLACK)
                    WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2,
                                           HEIGHT // 2 - winner_text.get_height() // 2))
                    delay()
                    main()

        pg.display.update()

    sys.exit()


if __name__ == '__main__':
    main()
