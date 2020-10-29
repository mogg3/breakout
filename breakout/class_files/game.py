from breakout.class_files.ball import *
from breakout.class_files.paddle import *
from breakout.class_files.box import *
from breakout.class_files.button import *
from breakout.breakout_settings import *

import pygame
import time
import pickle


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

        self.paddle = Paddle(paddle_start_x, paddle_start_y)
        self.ball = Ball(ball_start_x, ball_start_y)
        self.screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

        self.heart = pygame.transform.scale(heart_img, (100, 75))
        self.menu_bg = pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\menu.png')

        self.level = 1
        self.score = 0
        self.start_score = 0
        self.lives = 3
        self.boxes = []

        self.first_run = True
        self.in_menu = True
        self.paused = False
        self.loaded = False
        self.won = False
        self.gameover = False

    def get_stats(self):
        self.lvl_text = stats_font.render(f'Level {self.level}', True, BLACK, None)
        self.lvl_textrect = self.lvl_text.get_rect()
        self.lvl_textrect.center = ((BOARD_WIDTH // 4), 25)

        self.score_text = stats_font.render(f"Score: {self.score}", True, BLACK, None)
        self.score_textrect = self.score_text.get_rect()
        self.score_textrect.center = ((BOARD_WIDTH // 4) * 3, 25)

        self.p_text = pause_font.render(f"P TO PAUSE", True, BLACK, None)
        self.p_textrect = self.lvl_text.get_rect()
        self.p_textrect.center = (750, 590)

    def show_stats(self):
        self.get_stats()
        self.screen.blit(self.lvl_text, self.lvl_textrect)
        self.screen.blit(self.score_text, self.score_textrect)
        for i in range(self.lives):
            self.screen.blit(self.heart, (40 * i, 525))

    def menu_screen(self):
        new_game_btn = Button(268, 216, 260, 39)
        load_game_btn = Button(251, 284, 295, 39)
        quit_btn = Button(336, 354, 127, 39)

        self.screen.blit(self.menu_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if new_game_btn.inside():
            self.screen.blit(
                pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\menu_newgame.png'),
                (0, 0))
            pygame.display.update()
            if new_game_btn.clicked():
                self.fade("menu")
                self.in_menu = False

        if load_game_btn.inside():
            self.screen.blit(pygame.image.load(
                r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\menu_loadgame.png'), (0, 0))
            pygame.display.update()
            if load_game_btn.clicked():
                with open("pickle_files/boxes.txt", "rb") as boxes_file:
                    self.boxes = pickle.load(boxes_file)
                with open("pickle_files/level.txt", "rb") as level_file:
                    self.level = pickle.load(level_file)
                with open("pickle_files/score.txt", "rb") as score_file:
                    self.score = pickle.load(score_file)
                with open("pickle_files/lives.txt", "rb") as lives_file:
                    self.lives = pickle.load(lives_file)
                self.loaded = True
                self.fade("menu")
                self.in_menu = False

        if quit_btn.inside():
            self.screen.blit(
                pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images'r'\menu_quit.png'),
                (0, 0))
            pygame.display.update()
            if quit_btn.clicked():
                self.fade("menu")
                pygame.display.update()
                time.sleep(1)
                quit()
        pygame.display.update()

    def pause_screen(self):
        continue_btn = Button(306, 229, 187, 28)
        restart_lvl_btn = Button(245, 268, 307, 28)
        restart_game_btn = Button(257, 307, 285, 28)
        quitsave_btn = Button(269, 346, 260, 28)
        quit_btn = Button(355, 385, 88, 28)

        self.screen.blit(pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\paused.png'),
                         (200, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if continue_btn.inside():
            self.screen.blit(
                pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\paused_continue.png'),
                (200, 100))
            pygame.display.update()
            if continue_btn.clicked():
                self.paused = False

        if restart_lvl_btn.inside():
            self.screen.blit(
                pygame.image.load(
                    r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\paused_restartlevel.png'),
                (200, 100))
            if restart_lvl_btn.clicked():
                self.restart_level()

        if restart_game_btn.inside():
            self.screen.blit(
                pygame.image.load(
                    r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\paused_restartgame.png'),
                (200, 100))
            pygame.display.update()
            if restart_game_btn.clicked():
                self.restart_game()

        if quitsave_btn.inside():
            self.screen.blit(
                pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\paused_quitsave.png'),
                (200, 100))
            if quitsave_btn.clicked():
                with open("pickle_files/boxes.txt", "wb") as boxes_file:
                    pickle.dump(self.boxes, boxes_file)
                with open("pickle_files/level.txt", "wb") as level_file:
                    pickle.dump(self.level, level_file)
                with open("pickle_files/score.txt", "wb") as score_file:
                    pickle.dump(self.score, score_file)
                with open("pickle_files/lives.txt", "wb") as lives_file:
                    pickle.dump(self.lives, lives_file)
                self.fade("ingame")
                pygame.quit()
                quit()

        if quit_btn.inside():
            self.screen.blit(
                pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\paused_quit.png'),
                (200, 100))
            if quit_btn.clicked():
                pygame.quit()
                quit()

        pygame.display.update()

    def win_screen(self):
        quit_btn = Button(151, 310, 121, 40)
        playagain_btn = Button(345, 310, 316, 40)
        self.screen.blit(pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\win.png'),
                         (0, 0))
        self.paddle.draw_paddle(self.screen)
        self.ball.draw_ball(self.screen)
        self.get_stats()
        self.show_stats()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if playagain_btn.inside():
            self.screen.blit(
                pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\win_playagain.png'),
                (0, 0))
            pygame.display.update()
            if playagain_btn.clicked():
                self.won = False
                self.restart_game()

        if quit_btn.inside():
            self.screen.blit(
                pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\win_quit.png'),
                (0, 0))
            pygame.display.update()
            if quit_btn.clicked():
                self.fade("ingame")
                pygame.display.update()
                time.sleep(1)
                quit()

        pygame.display.update()

    def game_over_screen(self):
        playagain_btn2 = Button(360, 278, 283, 34)
        quit_btn2 = Button(159, 278, 106, 34)

        self.screen.blit(
            pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\gameover.png'),
            (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if playagain_btn2.inside():
            self.screen.blit(
                pygame.image.load(
                    r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\gameover_playagain.png'),
                (0, 0))
            pygame.display.update()
            if playagain_btn2.clicked():
                self.gameover = False
                self.restart_game()

        if quit_btn2.inside():
            self.screen.blit(
                pygame.image.load(r'C:\Users\marcu\PycharmProjects\Breakout\breakout\images\gameover_quit.png'),
                (0, 0))
            pygame.display.update()
            if quit_btn2.clicked():
                quit()

        pygame.display.update()

    def box_gen(self):
        boxes_per_row = columns[self.level - 1]
        for row in range(level_dict[boxes_per_row]):
            random_box_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for i, box in enumerate(range(boxes_per_row)):
                box_width = int((BOARD_WIDTH - 5 * (boxes_per_row + 1)) / boxes_per_row)
                temp_box = Box((5 * (box + 1)) + (box_width * box),
                               50 + (5 * (row + 1)) + (box_height * row), random_box_color, box_width, 1)
                self.boxes.append(temp_box)
            boxes_per_row -= 1
        return self.boxes

    def draw_boxes(self):
        for box in self.boxes:
            box.draw_box(self.screen)

    def wall_bounce(self):
        if not ball_radius <= self.ball.x <= BOARD_WIDTH - ball_radius:
            self.ball.x_step *= -1
        if not ball_radius <= self.ball.y:
            self.ball.y_step *= -1
        if not self.ball.y <= BOARD_HEIGHT - ball_radius:
            self.ball.y_step *= -1
            self.lives -= 1
        if self.lives == 0:
            self.gameover = True

    def box_collide(self, box):
        if self.ball.left >= box.right or box.left >= self.ball.right:
            return False
        if self.ball.top >= box.bottom or box.top >= self.ball.bottom:
            return False
        return True

    def box_bounce(self):
        for i, box in enumerate(self.boxes):
            if self.box_collide(box):
                box.hits += 1
                if box.left <= self.ball.right <= box.left + 10:
                    self.ball.x_step *= -1
                if box.right >= self.ball.left >= box.right - 10:
                    self.ball.x_step *= -1

                if box.top <= self.ball.bottom <= box.top + 10:
                    self.ball.y_step *= -1

                if box.bottom >= self.ball.top >= box.bottom - 10:
                    self.ball.y_step *= -1

                if box.hits == box.required_hits:
                    self.boxes.remove(self.boxes[i])
                    self.score += 50

    def paddle_collide(self):
        ball_mask = self.ball.get_mask()
        paddle_mask = self.paddle.get_mask()

        offset = (round(self.paddle.x - self.ball.x), round(self.paddle.y - self.ball.y))

        collide = ball_mask.overlap(paddle_mask, offset)

        if collide:
            return True

    def paddle_bounce(self):
        if self.paddle_collide():
            for i in range(9):
                if self.paddle.left + i * (paddle_width / 9) < self.ball.x < self.paddle.left + (i + 1) * (
                        paddle_width / 9):
                    if self.ball.x_index == 0:
                        self.ball.x_step = x_steps2[i]
                        self.ball.y_step = y_steps[i]
                    else:
                        self.ball.x_step = self.ball.x_index * x_steps[i]
                        self.ball.y_step = y_steps[i]
                    self.ball.x_step *= self.ball.speed
                    self.ball.y_step *= self.ball.speed

    def no_boxes(self):
        if len(self.boxes) == 0 and not self.first_run:
            self.screen.blit(self.bg_img, (-250, -400))
            if self.level == 6:
                self.won = True
            return True

    def change_level(self):
        self.start_score = self.score
        self.level += 1
        self.fade("ingame")
        if self.loaded:
            self.boxes = self.box_gen()
        self.first_run = True
        self.screen.blit(self.bg_img, (-250, -400))
        self.ball.x = ball_start_x
        self.ball.y = ball_start_y
        self.paddle.x = paddle_start_x
        self.screen.blit(self.bg_img, (-250, -400))

    def restart_game(self):
        self.screen.blit(self.bg_img, (-250, -400))
        self.level = 1
        self.score = 0
        self.lives = 3
        self.boxes = []
        self.first_run = True
        self.paused = False
        self.fade("ingame")
        self.play()

    def restart_level(self):
        self.screen.blit(self.bg_img, (-250, -400))
        self.score = self.start_score
        self.fade("ingame")
        self.paused = False
        self.first_run = True
        self.boxes = []
        self.play()

    def draw(self):
        self.screen.blit(self.bg_img, (-250, -400))
        self.paddle.draw_paddle(self.screen)
        self.ball.draw_ball(self.screen)
        self.draw_boxes()

    def fade(self, screen):
        fade = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
        fade.fill((0, 0, 0))
        for alpha in range(0, 300, 7):
            fade.set_alpha(alpha)
            if screen == "menu":
                self.screen.blit(self.menu_bg, (0, 0))
            else:
                self.draw()
            self.screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(1)

    def play(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = True
                if event.key == pygame.K_b:
                    print(self.ball)

        if self.first_run:
            self.bg_img = bg_list[self.level - 1]
            self.screen.blit(self.bg_img, (-250, -400))
            self.ball.x = ball_start_x
            self.ball.y = ball_start_y
            self.paddle.x = paddle_start_x
            if not self.loaded:
                self.boxes = self.box_gen()
            lvl_text = next_lvl_font.render(f'Level {self.level}', True, WHITE, None)
            textrect = lvl_text.get_rect()
            textrect.center = (BOARD_WIDTH // 2, BOARD_HEIGHT // 2)
            self.screen.blit(lvl_text, textrect)
            pygame.display.update()
            time.sleep(3)
            pygame.display.update()
            time.sleep(1)
            self.draw()
            pygame.display.update()
            time.sleep(3)
            self.first_run = False

        self.draw()

        if self.first_run:
            pygame.display.update()
            time.sleep(3)
            self.first_run = False

        self.show_stats()

        self.ball.move_ball()
        self.paddle.move_paddle()
        self.wall_bounce()
        self.paddle_bounce()
        self.box_bounce()

        self.screen.blit(self.p_text, self.p_textrect)
        pygame.display.update()
