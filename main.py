# import os
# import sys
#
# import pygame as pygame
#
# pygame.init()
# width = 850
# height = 550
# size = 850, 550
# screen = pygame.display.set_mode(size)
#
#
# ############################ Загрузка и обработка изображения ################################
# def load_image(name, colorkey=None):
#     fullname = os.path.join('backside', name)
#     # если файл не существует, то выходим
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     return image
#
#
# fon = pygame.transform.scale(load_image('back.jpg'), (width, height))
# screen.blit(fon, (0, 0))
#
# ###################################### Создаем меню ############################################
#
# Arial = pygame.font.SysFont('arial', 45)


# class Menu:
#     def __init__(self):
#         self.option_surfaces = []
#         self.callbacks = []
#         self.last_option_index = 0
#
#     def append_option(self, sth_new, callback):
#         self.option_surfaces.append(Arial.render(sth_new, True, 'White'))
#         self.callbacks.append(callback)
#
#     def switch(self, direction):
#         self.last_option_index = max(0, min(self.last_option_index + direction, len(self.option_surfaces) - 1))
#
#     def select(self):
#         self.callbacks[self.last_option_index]()
#
#     def draw(self, surface, x, y, padding):
#         for index, option in enumerate(self.option_surfaces):
#             option_rect = option.get_rect()
#             option_rect.topleft = (x, y + index * padding)
#             if index == self.last_option_index:
#                 pygame.draw.rect(surface, (0, 69, 36), option_rect)
#             surface.blit(option, option_rect)
    #
    # def delete(self):
    #     for opt in self.option_surfaces:
    #         for i in range(20):
    #             self.option_rect.topleft = (self.x + i, self.y)




# menu = Menu()
# menu.append_option('Начать игру', lambda: print('afsdfsdfsf'))
# menu.append_option('выход', quit)



##################################### Основной игровой цикл #####################################


# while running:
#     menu.draw(screen, 320, 300, 50)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 menu.switch(-1)
#             elif event.key == pygame.K_DOWN:
#                 menu.switch(1)
#             elif event.key == pygame.K_RETURN:
#                 menu.select()
#
#     pygame.display.flip()
# quit()



import os
import sys
import random

import pygame as pygame

running = True

pygame.init()
width = 850
height = 550
size = 850, 550
screen = pygame.display.set_mode(size)

fps = 30
clock = pygame.time.Clock()

all_enemies = {}



############################ Загрузка и обработка изображения ################################

def load_image(name, colorkey=None):
    fullname = os.path.join('backside', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


fon = pygame.transform.scale(load_image('back.jpg'), (width, height))
screen.blit(fon, (0, 0))



###################################### Создание основного окна ############################################

class Window:
    def __init__(self):
        self.hp = 100
        self.current_enemies_amount = 0

    def update_enemy_location(self, object): # в object передаётся словарь
        for i in object.keys():
            i.move()
            all_enemies[i] = i.return_pos()
            pygame.draw.circle(screen, (255, 0, 0), all_enemies[i], 10)



###################################### Класс Врага ############################################
class Enemy:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.has_reached_field = False

    def return_pos(self): # возвращает позицию врага в виде кортежа
        return self.x, self.y

    def move(self):
        if self.has_reached_field:
            pass
        else:
            global width
            self.y += 1
            if self.x > width / 2:
                self.x -= 0.3
            elif self.x < width / 2:
                self.x += 0.3
            else:
                pass

###################################### Функция Создания Врага ############################################
def create_enemy(pos):
    global all_enemies
    enemy = Enemy(pos)
    all_enemies = {enemy: enemy.return_pos()}
    return enemy
###################################### Игровой цикл ############################################



create_enemy((random.randint(0, width), 100))

LEVEL_INCREASE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(LEVEL_INCREASE_EVENT,  45 * 1000)
# level = 1
# каждые 45 секунд повышается уровень сложности - спавнится больше птиц .
window = Window()
running = True
while running:
    screen.blit(fon, (0, 0))
    for event in pygame.event.get():
        if event.type == LEVEL_INCREASE_EVENT:
            pass
        if event.type == pygame.QUIT:
            running = False
    window.update_enemy_location(all_enemies)
    pygame.display.flip()
    clock.tick(fps)

print(all_enemies.values())



