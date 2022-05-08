from scripts import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JDTetris')
ICON_SURFACE = pygame.image.load(join('scripts', 'icon.png')).convert_alpha()
pygame.display.set_icon(ICON_SURFACE)


def main() -> None:
    running = True
    clock = pygame.time.Clock()
    locked_pos = {}
    current_piece = get_shape()
    next_piece = get_shape()
    change_piece = False
    score = Score()
    DWN = pygame.USEREVENT
    pygame.time.set_timer(DWN, 1000)
    pygame.mixer.music.unpause()
    while running:
        clock.tick(FPS)
        grid = create_grid(locked_pos)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_DOWN]:
            current_piece.y += 1
            if not is_valid(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1

        for event in pygame.event.get():
            if event.type == DWN:
                current_piece.y += 1
                if not is_valid(current_piece, grid) and current_piece.y > 0:
                    current_piece.y -= 1
                    change_piece = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.pause()
                    PAUSE_SFX.play()
                    pause(WIN)
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not is_valid(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not is_valid(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation = (current_piece.rotation + 1) % len(current_piece.shape)
                    if not is_valid(current_piece, grid):
                        current_piece.rotation = (current_piece.rotation - 1) % len(current_piece.shape)
                    else:
                        ROTATE_SFX.play()
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_pos[p] = current_piece.color
            current_piece = next_piece
            LOCKED_SFX.play()
            next_piece = get_shape()
            change_piece = False
            clear_row(grid, locked_pos, score)
        draw_win(WIN, grid, score, next_piece)

        if check_lost(locked_pos):
            running = False
    _menu()


def _menu() -> None:
    running = True
    while running:
        draw_menu(WIN)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                main()
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == '__main__':
    main()
