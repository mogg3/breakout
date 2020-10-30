from breakout.breakout_settings import *
from math import *


class Ball:

    def __init__(self, x, y):
        self.speed = 5
        self.x = x
        self.y = y
        self.x_step = cos(pi / 2) * self.speed
        self.y_step = -sin(pi / 2) * self.speed
        self.step = sqrt(self.x_step ** 2 + self.y_step ** 2)
        self.x_index = 0
        self.ball_img = pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\ball.png')

    def __str__(self):
        return f"X = {self.x}      Y = {self.y}      X_Step = {self.x_step}     Y-Step = {self.y_step}        Step = {self.step}"

    @property
    def top(self):
        return self.y - ball_radius

    @property
    def bottom(self):
        return self.y + ball_radius

    @property
    def left(self):
        return self.x - ball_radius

    @property
    def right(self):
        return self.x + ball_radius

    def draw_ball(self, screen):
        screen.blit(self.ball_img, (self.x - ball_radius, self.y - ball_radius))

    def move_ball(self):
        self.x += self.x_step
        self.y += self.y_step
        if self.x_step < 0:
            self.x_index = -1
        if self.x_step > 0:
            self.x_index = 1
        if self.x_step == -cos(pi / 2) * self.speed or self.x_step == cos(pi / 2) * self.speed:
            self.x_index = 0

    def get_mask(self):
        return pygame.mask.from_surface(self.ball_img)
