import pygame
import pygame.locals
import pygame.gfxdraw
import pygame.time
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
        if self.is_selected:
            pygame.gfxdraw.box(surface, self.rect, WHITE)
        else:
            pygame.gfxdraw.box(surface, self.rect, BLACK)
       
        pygame.gfxdraw.rectangle(surface, self.rect, GRAY)


    def is_inside(self):
        a = pygame.mouse.get_pos()
        collision = self.rect.collidepoint(a) 
        return collision 
    
    #def setselected(self, value):
        #self.is_selected = value
        
    def toggle_selected(self):
        if self.is_selected:
            self.is_selected = False
        else:
            self.is_selected = True

    
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
        self.is_running = False
        self.pixel_amount = self.screen_width//16, self.screen_height//16

    ##Обработка самой игры 
    #Поиск игровых пикселей
    def find_pixel(self, x, y):
        for p in range(len(self.pixels)):
            pixel = self.pixels[p]
            
            if pixel.rect.x == x and pixel.rect.y == y:
                return p
        return -1
    
    def rules_processing(self):
        print("Is running")
        y = 0
        for times_y in range(self.pixel_amount[1]):
            x = 0
            for times_x in range(self.pixel_amount[0]):
                current_pixel = self.find_pixel(x, y)
                neighbors_count = 0
                #print(f"{current_pixel} {x} {y}")
                pixel = self.pixels[current_pixel]   
                if pixel.is_selected:
                    print("Found selected pixel:", (x, y))             
                for neighbor in [
                    (x + 16, y),
                    (x - 16, y),
                    (x, y + 16),
                    (x, y - 16),
                    (x + 16, y + 16),
                    (x - 16, y - 16),
                    (x+16 , y -16),
                    (x - 16, y + 16)
                 ]:
                    print("got current pixel", (x, y), ", trying neighbor ", neighbor)
                    neighbor_pixel = self.find_pixel(neighbor[0], neighbor[1])
                    if neighbor_pixel >= 0 and self.pixels[neighbor_pixel].is_selected:
                        print("neighbor found:", neighbor)
                        neighbors_count += 1

                if (neighbors_count < 2 or neighbors_count > 3) and pixel.is_selected:
                    pixel.toggle_selected()
                    print("killed pixel", x, y, " because neighbor count = ", neighbors_count)
                elif neighbors_count == 3 and not pixel.is_selected:
                    pixel.toggle_selected()
                #elif neighbors_count == 2:
                #    pass
                

                x += 16

            y += 16
        print("~~~~~~~~~~~~~~~")

    #Проверка как запустится pygame
    def check_for_errors(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()

        else:
            print('Ok')

    #keyboard-events
    #def on_spacebar(self):
        
    #mouse-tracking
    #def mousestuff(self):
        #pygame.mouse.get_pos()

    #Задаём поверхность окна
    def basegame(self):
        #self.pixel_amount = self.screen_width//16, self.screen_height//16
        self.screen.fill(BLACK)

        baseline_x = 0
        baseline_y = 0

        for i in range(self.pixel_amount[0]):
            baseline_y = 0
            for y in range(self.pixel_amount[1]):
                pixel = Pixel(baseline_x, baseline_y)
                self.pixels.append(pixel)
                baseline_y += 16
            baseline_x += 16
            #pygame.gfxdraw.vline(self.screen, baseline_x, 0, self.screen_height, GRAY)
            #baseline_y += 16
            #pygame.gfxdraw.hline(self.screen, 0, self.screen_width, baseline_y, GRAY)

    #Запуск игры
    def Run(self):
        self.fps_controller.tick(10)
        while True:
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN: 
                    for m in self.pixels:
                        if m.is_inside():
                            m.toggle_selected()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.locals.K_SPACE:
                        self.is_running = not self.is_running
                    
            if self.is_running == True:
                self.rules_processing()

            for x in self.pixels:
                x.draw_boxes(self.screen)
            pygame.display.update()

#Запуск игры  :)
game = Game()
game.basegame()
game.Run()




