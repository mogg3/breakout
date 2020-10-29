import pygame
from pygame.font import FontType
from math import *
import random

BOARD_WIDTH = 800
BOARD_HEIGHT = 600

pygame.display.set_caption("Breakout Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

box_height = 30

paddle_color = BLACK
paddle_width = 90
paddle_height = 20
paddle_step = 1
paddle_speed = 20
paddle_start_x = (BOARD_WIDTH / 2) - (paddle_width / 2)
paddle_start_y = 550

ball_color = BLACK
ball_radius = 7
ball_start_x = 400
ball_start_y = paddle_start_y - (ball_radius + 5)

# {columns : rows, columns : rows, .....}
#    (level 1)         (level 2)

level_dict = {3: 3, 6: 3, 9: 3, 12: 5, 15: 7, 18: 7}
columns = list(level_dict.keys())

pygame.font.init()
stats_font = pygame.font.Font('freesansbold.ttf', 32)
next_lvl_font = pygame.font.Font('freesansbold.ttf', 60)
pause_font = pygame.font.Font('freesansbold.ttf', 20)

# Images
level1_img = pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\bluemoon.png')
level2_img = pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\sunnyday.png')
level3_img = pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\cityskyline.png')
level4_img = pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\snowymountains.png')
level5_img = pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\graveyard.png')
level6_img = pygame.image.load(r"C:\Users\marcu\PycharmProjects\Breakout\breakout\images\foggy.png")
heart_img = pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\heart.png')

bg_list = [level1_img, level2_img, level3_img, level4_img, level5_img, level6_img]

x_steps = [
            cos(pi/16),
            cos(pi/8),
            cos(pi/4),
            cos(pi/3),
            cos(pi/2),
            cos(pi/3),
            cos(pi/4),
            cos(pi/8),
            cos(pi/16)
            ]

x_steps2 = [
            -cos(pi/16),
            -cos(pi/8),
            -cos(pi/4),
            -cos(pi/3),
            cos(pi/2),
            cos(pi/3),
            cos(pi/4),
            cos(pi/8),
            cos(pi/16)
            ]

y_steps = [
            -sin(pi/16),
            -sin(pi/8),
            -sin(pi/4),
            -sin(pi/3),
            -sin(pi/2),
            -sin(pi/3),
            -sin(pi/4),
            -sin(pi/8),
            -sin(pi/16)
            ]

