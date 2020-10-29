from breakout.breakout_settings import *


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paddle_img = pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\paddle.png')

    def move_paddle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.x = mouse_x - paddle_width / 2

    def draw_paddle(self, screen):
        screen.blit(self.paddle_img, (self.x, self.y))

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + paddle_height

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + paddle_width

    def get_mask(self):
        return pygame.mask.from_surface(self.paddle_img)
