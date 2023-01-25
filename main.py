"""
NewProject

by mr_kfyzi4(Borovoj Arsenij).
"""
import sys  # Импотрируем модуль sys нужный для выхода из программы без ошибок
import pygame  # Импортируем модуль pygame, при помоще него будет отрисовываться изображение
import os
from GameEngune import GameEngune  # Из файла GmaeEngune.py импортируем класс GameEngune
from GameEngune import PlayerClass  # Из файла GmaeEngune.py импортируем класс Player
from UserInterfaceEngune import Button  # Из файла UserInterfaceEngune.py импортируем класс Button
from UserInterfaceEngune import Message  # Из файла UserInterfaceEngune.py импортируем класс Message
from UserInterfaceEngune import Label  # Из файла UserInterfaceEngune.py импортируем класс Label

''' 
Подготовка к запуску игры.
'''
width_screen = 1920
height_screen = 1080
fps = 60
block_scale = 128
world_size = [0, 0]
Player = PlayerClass()  # Создаём экземпляр класса Player
Game_Engune = GameEngune()  # Создаём экземпляр класса GameEngune
screen = Game_Engune.open_window(width_screen, height_screen)  # Открываем окно
clock = pygame.time.Clock()
game_state = "MainMenu"

'''
Игровой цикл
'''

while True:
    if game_state == "MainMenu":
        start_button = Button(10, height_screen - 310, 200, 100, (128, 128, 128), screen, (128, 128, 128), 1, "START", 64)
        options_button = Button(10, height_screen - 210, 200, 100, (128, 128, 128), screen, (128, 128, 128), 1, "OPTIONS", 48)
        exit_button = Button(10, height_screen - 110, 200, 100, (255, 0, 0), screen, (128, 0, 0), 1, "EXIT", 72)
        options_not_working_message = Message(screen, width_screen / 2, height_screen / 2, f"{os.getcwd()}" + "\Assets\panthera-monoletter.ttf", 64)
        game_name_label = Label(screen, width_screen / 2, height_screen / 10, f"{os.getcwd()}" + "\Assets\panthera-monoletter.ttf", 128)
        game_name_label.update_info((255, 255, 255), "BETTER DREAMS")
        while True:
            screen.fill((0, 0, 0))
            Game_Engune.close_window_check(False)
            start = start_button.work()
            exit = exit_button.work()
            options = options_button.work()
            game_name_label.work()
            if start or exit or options:
                if start:
                    game_state = "SavesListMenu"
                    break
                if exit:
                    pygame.quit()
                    sys.exit()
                if options:
                    options_not_working_message.update_info((255, 255, 255), "Sorry, options not working :(", 5)
            options_not_working_message.work()
            pygame.display.update()
            clock.tick(fps)
    if game_state == "SavesListMenu":
        wait_label = Label(screen, width_screen / 2, height_screen / 2, f"{os.getcwd()}" + "\Assets\panthera-monoletter.ttf", 128)
        wait_label.update_info((128, 128, 128), "WAIT A SECOND...")
        game_name_label = Label(screen, width_screen / 2, height_screen / 10, f"{os.getcwd()}" + "\Assets\panthera-monoletter.ttf", 128)
        game_name_label.update_info((255, 255, 255), "BETTER DREAMS")
        save_name_label = Label(screen, width_screen / 2, height_screen / 10 * 2.5 + 13, f"{os.getcwd()}" + "\Assets\panthera-monoletter.ttf", 128)
        save_name_label.update_info((255, 255, 255), "Save name")
        difficulty_label = Label(screen, width_screen / 15 * 11 + 160, height_screen / 15 * 4, f"{os.getcwd()}" + "\Assets\panthera-monoletter.ttf", 64)
        difficulty_label.update_info((255, 255, 255), "DIFFICULTY")
        world_size_label = Label(screen, width_screen / 15 * 11 + 160, height_screen / 15 * 7, f"{os.getcwd()}" + "\Assets\panthera-monoletter.ttf", 64)
        world_size_label.update_info((255, 255, 255), "WORLD SIZE")
        previous_save_button = Button(width_screen / 5 * 1 - 50, height_screen / 5 * 4 - 50, 100, 100, (128, 128, 255), screen, (64, 64, 128), 1, "PREVIOUS", 28)
        main_menu_button = Button(10, 10, 100, 100, (128, 128, 128), screen, (128, 128, 128), 1, "back", 48)
        next_save_button = Button(width_screen / 5 * 4 - 50, height_screen / 5 * 4 - 50, 100, 100, (128, 128, 255), screen, (64, 64, 128), 1, "NEXT", 45)
        play_save_button = Button(width_screen / 7 * 2, height_screen / 5 * 4 - 50, width_screen / 7 * 3, 100, (128, 128, 255), screen, (64, 64, 128), 1, "PLAY", 100)
        new_game_button = Button(width_screen / 7 * 2, height_screen / 10 * 9 - 50, width_screen / 7 * 1.5 - 25, 100, (128, 128, 255), screen, (64, 64, 128), 0.25, "NEW GAME", 64)
        delete_game_button = Button(width_screen / 7 * 3.5 + 25, height_screen / 10 * 9 - 50, width_screen / 7 * 1.5 - 25, 100, (128, 128, 255), screen, (64, 64, 128), 1, "DELETE GAME", 54)
        difficulty_easy_button = Button(width_screen / 15 * 11, height_screen / 15 * 5, 100, 100, (128, 128, 255), screen, (64, 64, 128), 1, "EASY", 52)
        difficulty_normal_button = Button(width_screen / 15 * 11 + 110, height_screen / 15 * 5, 100, 100, (128, 128, 255), screen, (64, 64, 128), 1, "NORMAL", 32)
        difficulty_hard_button = Button(width_screen / 15 * 11 + 220, height_screen / 15 * 5, 100, 100, (128, 128, 255), screen, (64, 64, 128), 1, "HARD", 52)
        world_size_small_button = Button(width_screen / 15 * 11, height_screen / 15 * 5 + 220, 100, 100, (128, 128, 255), screen, (64, 64, 128), 1, "SMALL", 42)
        world_size_normal_button = Button(width_screen / 15 * 11 + 110, height_screen / 15 * 5 + 220, 100, 100, (128, 128, 255), screen, (64, 64, 128), 1, "NORMAL", 32)
        world_size_huge_button = Button(width_screen / 15 * 11 + 220, height_screen / 15 * 5 + 220, 100, 100, (128, 128, 255), screen, (64, 64, 128), 1, "HUGE", 52)
        create_new_save = Button(width_screen / 15 * 11, height_screen / 15 * 9.75, 320, 100, (128, 128, 255), screen, (64, 64, 128), 1, "CREATE NEW WORLD", 32)
        only_saves_dirs = []
        create_save_mode = False
        new_save_world_size = None
        choosed_save = 0
        main_path = os.getcwd()
        saves_path = f"{os.getcwd()}\Saves"
        active_wait_label = False
        while True:
            screen.fill((0, 0, 0))
            game_name_label.work()
            save_name_label.work()
            delete_game_button.work()
            pygame.draw.rect(screen, (128, 128, 255), (width_screen / 7 * 2, height_screen / 10 * 2, width_screen / 7 * 3, height_screen / 10 * 5), 25)
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_ESCAPE] or main_menu_button.work():
                game_state = "MainMenu"
                break
            os.chdir(saves_path)
            all_dirs_list = os.listdir()
            os.chdir(main_path)
            for num in range(len(all_dirs_list)):
                if all_dirs_list[num].startswith("Save_"):
                    only_saves_dirs.append(all_dirs_list[num])
            if len(only_saves_dirs) == 0:
                previous_save_button.update_info(True)
                next_save_button.update_info(True)
                play_save_button.update_info(True)
                delete_game_button.update_info(True)
                create_save_mode = True
            if new_game_button.work():
                if create_save_mode is False:
                    create_save_mode = True
                elif create_save_mode and len(only_saves_dirs) != 0:
                    create_save_mode = False
            if create_save_mode is False:
                previous_save_button.update_info(False)
                next_save_button.update_info(False)
                play_save_button.update_info(False)
                delete_game_button.update_info(False)
            if create_save_mode:
                previous_save_button.update_info(True)
                next_save_button.update_info(True)
                play_save_button.update_info(True)
                delete_game_button.update_info(True)
                difficulty_label.work()
                world_size_label.work()
                if difficulty_easy_button.work():
                    new_save_difficulty = "easy"
                if difficulty_normal_button.work():
                    new_save_difficulty = "normal"
                if difficulty_hard_button.work():
                    new_save_difficulty = "hard"
                if world_size_small_button.work():
                    new_save_world_size = (1500, 500)
                if world_size_normal_button.work():
                    new_save_world_size = (2000, 1000)
                if world_size_huge_button.work():
                    new_save_world_size = (2500, 1500)
                if new_save_world_size is not None:
                    if create_new_save.work():
                        GameEngune.make_new_world(new_save_world_size, only_saves_dirs, main_path)
                        new_save_world_size = None
                        create_save_mode = False
            if previous_save_button.work() and len(only_saves_dirs) != 0:
                new_choosed_save = choosed_save - 1
                if choosed_save > 0:
                    choosed_save = new_choosed_save
                else:
                    new_choosed_save = choosed_save
                save_name_label.update_info((255, 255, 255), only_saves_dirs[choosed_save])
            if next_save_button.work() and len(only_saves_dirs) != 0:
                new_choosed_save = choosed_save + 1
                if choosed_save < len(only_saves_dirs) - 1:
                    choosed_save = new_choosed_save
                save_name_label.update_info((255, 255, 255), only_saves_dirs[choosed_save])
            if play_save_button.work():
                active_wait_label = True
                game_state = "InGame"
                save_to_load_path = f"{saves_path}\Save_{choosed_save}"
                wait_label.work()
                pygame.display.update()
                break
            only_saves_dirs = []
            Game_Engune.close_window_check(False)
            pygame.display.update()
            clock.tick(fps)
    if game_state == "InGame":
        Game_Engune.load_save(save_to_load_path, main_path)
        exit_from_save = False
        wait_label = Label(screen, width_screen / 2, height_screen / 2, f"{os.getcwd()}" + "\Assets\panthera-monoletter.ttf", 128)
        wait_label.update_info((128, 128, 128), "WAIT A SECOND...")
        while not exit_from_save:
            pressed_key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if pressed_key[pygame.K_ESCAPE]:
                    wait_label.work()
                    pygame.display.update()
                    Game_Engune.save_world()
                    game_state = "MainMenu"
                    exit_from_save = True
            Game_Engune.close_window_check(True)
            Game_Engune.synchronize_offset_and_player_position(Player.move(block_scale))
            Game_Engune.do_lists_of_visibility(width_screen, height_screen, block_scale)
            Game_Engune.render_capture(width_screen, height_screen, screen, block_scale)
            Game_Engune.change_block_for_place()
            Game_Engune.change_world(width_screen, height_screen, block_scale)
            block_scale = Player.change_block_scale(block_scale)
            pygame.display.update()
            clock.tick(fps)
