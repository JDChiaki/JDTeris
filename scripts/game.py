from .settings import *
from random import choice
from sys import exit


class Piece:
    def __init__(self, col: int, row: int, shape: list[list[list[str]]]):
        self.x = col
        self.y = row
        self.shape = shape
        self.color = choice(shapes_colors)
        self.rotation = 0


class Score:
    def __init__(self):
        self.score = 0
        with open(join('scripts', 'score.txt'), 'r') as f:
            self.highest = int(f.readline().strip())

    def check(self) -> None:
        if self.score > self.highest:
            self.highest = self.score
            with open(join('scripts', 'score.txt'), 'w') as f:
                f.write(str(self.score))


def create_grid(locked_pos=None) -> list[list[tuple[int, int, int]]]:
    if not locked_pos:
        locked_pos = {}
    grid = [[BLACK for _ in range(COL)] for _ in range(ROW)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                grid[i][j] = locked_pos[(j, i)]

    return grid


def get_shape() -> Piece:
    return Piece(5, 0, choice(shapes))


def convert_shape_format(piece: Piece) -> list:
    position = []
    format_ = piece.shape[piece.rotation % len(piece.shape)]

    for i, line in enumerate(format_):
        row = list(line)
        for j, col in enumerate(row):
            if col == '0':
                position.append((piece.x + j, piece.y + i))

    for i, pos in enumerate(position):
        position[i] = (pos[0] - 2, pos[1] - 4)

    return position


def is_valid(piece: Piece, grid: list[list[tuple[int, int, int]]]) -> bool:
    ok_pos = [[(j, i) for j in range(COL) if grid[i][j] == BLACK] for i in range(ROW)]
    ok_pos = [j for sub in ok_pos for j in sub]
    shape = convert_shape_format(piece)

    for pos in shape:
        if pos not in ok_pos:
            if pos[1] > -1:
                return False

    return True


def clear_row(grid: list[list[tuple[int, int, int]]], locked_pos: dict, score: Score) -> None:
    inc = 0  # number of rows to clear
    ind = None  # index of last row to move down
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if BLACK not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                del locked_pos[(j, i)]
    if inc > 0:
        score.score += inc
        score.check()
        CLEAR_SFX.play()
        for key in sorted(list(locked_pos), key=lambda pos: pos[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked_pos[newKey] = locked_pos.pop(key)


def check_lost(locked_position: dict) -> bool:
    for pos in locked_position:
        if pos[1] < 1:
            pygame.mixer.music.pause()
            GAMEOVER_SFX.play()
            return True
    return False


def pause(win: pygame.Surface) -> None:
    pausing = True
    PAUSE_FONT = pygame.font.Font(join('scripts', 'game_font.ttf'), 50)
    pause_txt = PAUSE_FONT.render('Pause', True, WHITE)
    while pausing:
        win.fill(BLACK)
        win.blit(pause_txt, (WIDTH // 2 - pause_txt.get_width() // 2, HEIGHT // 2 - pause_txt.get_height() // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    PAUSE_SFX.play()
                    pausing = False
                    pygame.mixer.music.unpause()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
