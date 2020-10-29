from breakout.class_files.game import *
from breakout.breakout_settings import *


def main():
    game = Game()
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    while running:

        while game.in_menu:
            game.menu_screen()

        while game.no_boxes():
            if game.won:
                game.win_screen()
            else:
                game.change_level()

        while game.paused:
            game.pause_screen()

        while game.gameover:
            game.game_over_screen()

        game.play()
        clock.tick(60)



if __name__ == "__main__":
    main()
