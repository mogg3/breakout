import pygame
from breakout.breakout_settings import *


class Button:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.height

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width

    def clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.left < mouse_x < self.right and self.top < mouse_y < self.bottom and pygame.mouse.get_pressed()[0]:
            return True

    def inside(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.left < mouse_x < self.right and self.top < mouse_y < self.bottom:
            return True

    # This is just a tool for creating a button and deciding it's position
    @staticmethod
    def get_mouse_pos():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            print(mouse_x, mouse_y)

    def draw_button(self, screen):
        pygame.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height], 1)
