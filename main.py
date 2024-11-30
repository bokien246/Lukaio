import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, MAX_FRAME_RATE, FONT_PATH
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario


def menu_loop(menu):
    while not menu.start:
        menu.update()


def game_loop(mario, level, dashboard, clock):
    while not mario.restart:
        pygame.display.set_caption("Cuộc phiêu lưu kí của Tuấn Linh {:d} FPS".format(int(clock.get_fps())))
        if mario.pause:
            mario.pauseObj.update()
        else:
            level.drawLevel(mario.camera)
            dashboard.update()
            mario.update()
        pygame.display.update()
        clock.tick(MAX_FRAME_RATE)


def main():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dashboard = Dashboard(FONT_PATH, 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)

    menu_loop(menu)

    mario = Mario(0, 0, level, screen, dashboard, sound)
    game_loop(mario, level, dashboard, clock)

    return 'restart'


if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()
