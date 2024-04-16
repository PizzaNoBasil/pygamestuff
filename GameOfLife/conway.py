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

class Pixel():
    def __init__(self, x, y):
        #Задаём параметры наших квадратов   
        self.rect = pygame.Rect(x, y, 16, 16)
        self.is_selected = False
            
    def draw_boxes(self, surface):
        pygame.gfxdraw.rectangle(surface, self.rect, GRAY)
        if self.is_selected:
            pygame.gfxdraw.box(surface, self.rect, WHITE)

    def is_inside(self):
        a = pygame.mouse.get_pos()
        collision = self.rect.collidepoint(a) 
        return collision 
    
    def setselected(self, value):
        self.is_selected = value
        
    
#Создаём окружение
class Game():

    def __init__(self):
        #Задаём размеры окна
        self.screen_width = userinputW
        self.screen_height = userinputH

        #Задаём FPS игры
        self.fps_controller = pygame.time.Clock()
        self.pixels = []
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    #Проверка как запустится pygame
    def check_for_errors(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()

        else:
            print('Ok')

    #mouse-tracking
    def mousestuff(self):
        pygame.mouse.get_pos()

    #Задаём поверхность окна
    def basegame(self):
        pixel_amount = self.screen_width//16, self.screen_height//16
        self.screen.fill(BLACK)

        baseline_x = 0
        baseline_y = 0

        for i in range(pixel_amount[0]):
            baseline_y = 0
            for y in range(pixel_amount[1]):
                pixel = Pixel(baseline_x, baseline_y)
                self.pixels.append(pixel)
                baseline_y += 16
            baseline_x += 16
            #pygame.gfxdraw.vline(self.screen, baseline_x, 0, self.screen_height, GRAY)
            #baseline_y += 16
            #pygame.gfxdraw.hline(self.screen, 0, self.screen_width, baseline_y, GRAY)

    #Запуск игры
    def Run(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN: 
                    for m in self.pixels:
                        if m.is_inside():
                            m.setselected(True)
            for x in self.pixels:
                x.draw_boxes(self.screen)
            pygame.display.update()

#Запуск игры  :)
game = Game()
game.basegame()
game.Run()




