from unittest import TestCase
from .ball import Ball
from math import sqrt


class TestBall(TestCase):
    def test_step(self):
        ball = Ball(0, 0)
        self.assertAlmostEqual(sqrt(ball.x_step ** 2 + ball.y_step ** 2), ball.speed)
