from breakout.breakout_settings import *


class Box:
    def __init__(self, x, y, box_color, box_width, required_hits):
        self.x = x
        self.y = y
        self.color = box_color
        self.width = box_width
        self.required_hits = required_hits
        self.hits = 0

    def draw_box(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, box_height])
        pygame.draw.rect(screen, WHITE, [self.x, self.y, self.width, box_height], 3)

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + box_height

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width

