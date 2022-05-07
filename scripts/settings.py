import pygame
from os.path import join

pygame.init()

WIDTH, HEIGHT = 800, 700
PWIDTH, PHEIGHT = 300, 600

BLOCK_SIZE = 30
ROW = 20
COL = 10

BLOCK_X = (WIDTH - PWIDTH) // 2
BLOCK_Y = HEIGHT - PHEIGHT

FPS = 30

CLEAR_SFX = pygame.mixer.Sound(join('sfx', 'clear.wav'))
GAMEOVER_SFX = pygame.mixer.Sound(join('sfx', 'gameover.wav'))
LOCKED_SFX = pygame.mixer.Sound(join('sfx', 'locked.wav'))
ROTATE_SFX = pygame.mixer.Sound(join('sfx', 'rotate.mp3'))
PAUSE_SFX = pygame.mixer.Sound(join('sfx', 'pause.mp3'))

pygame.mixer.music.load(join('sfx', 'bgm.mp3'))
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)
PINK = (255, 0, 255)
GRAY = (128, 128, 128)

shapes_colors = [RED, GREEN, BLUE, YELLOW, AQUA, PINK, GRAY]

S_ = [['.....',
       '.....',
       '..00.',
       '.00..',
       '.....'],
      ['.....',
       '..0..',
       '..00.',
       '...0.',
       '.....']]

Z_ = [['.....',
       '.....',
       '.00..',
       '..00.',
       '.....'],
      ['.....',
       '..0..',
       '.00..',
       '.0...',
       '.....']]

I_ = [['..0..',
       '..0..',
       '..0..',
       '..0..',
       '.....'],
      ['.....',
       '0000.',
       '.....',
       '.....',
       '.....']]

O_ = [['.....',
       '.....',
       '.00..',
       '.00..',
       '.....']]

J_ = [['.....',
       '.0...',
       '.000.',
       '.....',
       '.....'],
      ['.....',
       '..00.',
       '..0..',
       '..0..',
       '.....'],
      ['.....',
       '.....',
       '.000.',
       '...0.',
       '.....'],
      ['.....',
       '..0..',
       '..0..',
       '.00..',
       '.....']]

L_ = [['.....',
       '...0.',
       '.000.',
       '.....',
       '.....'],
      ['.....',
       '..0..',
       '..0..',
       '..00.',
       '.....'],
      ['.....',
       '.....',
       '.000.',
       '.0...',
       '.....'],
      ['.....',
       '.00..',
       '..0..',
       '..0..',
       '.....']]

T_ = [['.....',
       '..0..',
       '.000.',
       '.....',
       '.....'],
      ['.....',
       '..0..',
       '..00.',
       '..0..',
       '.....'],
      ['.....',
       '.....',
       '.000.',
       '..0..',
       '.....'],
      ['.....',
       '..0..',
       '.00..',
       '..0..',
       '.....']]

shapes = [S_, Z_, I_, O_, J_, L_, T_]
