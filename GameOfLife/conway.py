import pygame
import pygame.gfxdraw
import sys
import random
import time

#Запрашиваем у пользователя ширину/ высоту приложения
print("Введите ширину экрана")
userinputW = int(input())
if userinputW%8 != 0:
    print("Некорректная ширина экрана, введите число кратное 8")
    sys.exit(1)

print("Введите высоту экрана")
userinputH = int(input())
if userinputH%8 != 0:
    print("Некорректная высота экрана, введите число кратное 8")
    sys.exit(1)

#Задаём цвета
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)

#Создаём окружение
class Game():

    def __init__(self):
        #Задаём размеры окна
        self.screen_width = userinputW
        self.screen_height = userinputH

        #Задаём FPS игры
        self.fps_controller = pygame.time.Clock()

    #Проверка как запустится pygame
    def check_for_errors(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()

        else:
            print('Ok')

    #Задаём поверхность окна
    def basegame(self):
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pixel_amount = self.screen_width//2, self.screen_height//2
        screen.fill(BLACK)

        baseline_x = 0
        baseline_y = 0

        for i in range(pixel_amount[0]):
            baseline_x += 16
            pygame.gfxdraw.vline(screen, baseline_x, 0, self.screen_height, GRAY)
            baseline_y += 16
            pygame.gfxdraw.hline(screen, 0, self.screen_width, baseline_y, GRAY)
    
    def Run(self):
        while True:
            for e in pygame.event.get():
                pygame.display.update()
game = Game()
game.basegame()
game.Run()
                



