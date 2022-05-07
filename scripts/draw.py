from .settings import *
from .game import Score, Piece


def draw_win(win: pygame.Surface, grid: list, score: Score, next_shape: Piece) -> None:
    win.fill(BLACK)
    draw_piece(win, grid)
    draw_nextshape(win, next_shape)
    draw_grid(win)
    draw_score(win, score)
    pygame.display.update()


def draw_grid(win: pygame.Surface) -> None:
    pygame.draw.rect(win, RED, (BLOCK_X, BLOCK_Y, PWIDTH, PHEIGHT), 5)
    for i in range(ROW):
        pygame.draw.line(win, GRAY, (BLOCK_X, BLOCK_Y + i * BLOCK_SIZE),
                         (BLOCK_X + PWIDTH, BLOCK_Y + i * BLOCK_SIZE))
        for j in range(COL + 1):
            pygame.draw.line(win, GRAY, (BLOCK_X + j * BLOCK_SIZE, BLOCK_Y),
                             (BLOCK_X + j * BLOCK_SIZE, BLOCK_Y + PHEIGHT))


def draw_piece(win: pygame.Surface, grid: list) -> None:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(win, grid[i][j],
                             (BLOCK_X + j * BLOCK_SIZE, BLOCK_Y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)


TXT_FONT = pygame.font.Font(join('scripts', 'game_font.ttf'), 30)
TXT_FONT2 = pygame.font.Font(join('scripts', 'game_font.ttf'), 40)


def draw_score(win: pygame.Surface, score: Score) -> None:
    score_txt = TXT_FONT.render('Score', True, WHITE)
    win.blit(score_txt, (BLOCK_X // 2 - score_txt.get_width() // 2, BLOCK_Y + BLOCK_SIZE * 5))
    highest_txt = TXT_FONT.render('Highest', True, WHITE)
    win.blit(highest_txt, (BLOCK_X // 2 - highest_txt.get_width() // 2, BLOCK_Y + BLOCK_SIZE * 11))
    score_num = TXT_FONT.render(f'{score.score}', True, WHITE)
    win.blit(score_num, (BLOCK_X // 2 - score_num.get_width() // 2, BLOCK_Y + BLOCK_SIZE * 7))
    high_num = TXT_FONT.render(f'{score.highest}', True, WHITE)
    win.blit(high_num, (BLOCK_X // 2 - high_num.get_width() // 2, BLOCK_Y + BLOCK_SIZE * 13))


def draw_nextshape(win: pygame.Surface, piece: Piece) -> None:
    nextshape_txt = TXT_FONT.render('Next Shape', True, WHITE)
    win.blit(nextshape_txt, (BLOCK_X * 3 // 2 + PWIDTH - nextshape_txt.get_width() // 2, BLOCK_Y + BLOCK_SIZE * 8))
    shape = piece.shape[piece.rotation]
    for i, line in enumerate(shape):
        row = list(line)
        for j, col in enumerate(row):
            if col == '0':
                pygame.draw.rect(win, WHITE, (BLOCK_X * 5 // 4 + PWIDTH + j * BLOCK_SIZE,
                                              BLOCK_Y * 3 // 2 + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 5)
                pygame.draw.rect(win, piece.color, (BLOCK_X * 5 // 4 + PWIDTH + j * BLOCK_SIZE,
                                                    BLOCK_Y * 3 // 2 + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)


def draw_menu(win: pygame.Surface) -> None:
    win.fill(BLACK)
    menu_txt = TXT_FONT2.render('Game Over!', True, WHITE)
    win.blit(menu_txt, (WIDTH // 2 - menu_txt.get_width() // 2, HEIGHT // 2 - menu_txt.get_height() // 2))
    press_txt = TXT_FONT2.render('Press any key to continu...!', True, WHITE)
    win.blit(press_txt, (WIDTH // 2 - press_txt.get_width() // 2, HEIGHT * 3 // 4 - press_txt.get_height()))
    pygame.display.update()
