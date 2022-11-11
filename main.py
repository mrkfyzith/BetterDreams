'''
NewProject

by mr_kfyzi4(Borovoj Arsenij)
'''
import sys
from classes import *

''' 
Подготовка к запуску игры.
'''
width_screen = 1920
height_screen = 1080
fps = 60
Player = Player()  # Создаём экземпляр класса Player
Game_Engune = GameEngune()  # Создаём экземпляр класса GameEngune
screen = Game_Engune.open_window(width_screen, height_screen)  # Открываем окно
Game_Engune.read_save()  # Читаем файл world.txt что-бы в дальнейшем отрендерить из него мир
clock = pygame.time.Clock()

'''
Игровой цикл
'''

while True:
    pressed_key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pressed_key[pygame.K_ESCAPE]):
            pygame.quit()
            sys.exit()
    Game_Engune.synchronize_offset_and_player_position(Player.move())
    screen.fill((255, 255, 255))
    Game_Engune.do_lists_of_visibility(width_screen, height_screen)
    Game_Engune.render_capture(width_screen, height_screen, screen)
    Game_Engune.change_world(width_screen, height_screen)
    pygame.display.update()
    clock.tick(fps)
